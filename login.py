from playwright.sync_api import sync_playwright
from config import Config
import time


class Login:
    def __init__(self, config: Config):
        self.config = config
        self.browser = None
        self.context = None
        self.page = None

    def start_browser(self):
        playwright = sync_playwright().start()
        settings = self.config.get_settings()
        
        self.browser = playwright.chromium.launch(
            headless=settings.get('headless', False)
        )
        self.context = self.browser.new_context(
            viewport={'width': 375, 'height': 812},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
        )
        self.page = self.context.new_page()
        return self.page

    def login(self):
        phone = self.config.get_phone()
        password = self.config.get_password()
        
        if not phone:
            raise ValueError("请先在config.json中配置手机号")

        print("正在访问i茅台H5页面...")
        self.page.goto('https://h5.moutai519.com.cn/')
        
        time.sleep(3)
        
        print("查找登录按钮...")
        login_button = self.page.locator('text=登录').first
        if not login_button.is_visible():
            login_button = self.page.locator('text=我的').first
        
        if login_button.is_visible():
            print("点击登录按钮")
            login_button.click()
            time.sleep(2)
        
        print("查找手机号输入框...")
        phone_input = self.page.locator('input[type="tel"]').first
        if not phone_input.is_visible():
            phone_input = self.page.locator('input[placeholder*="手机"]').first
        
        if phone_input.is_visible():
            print("输入手机号")
            phone_input.fill(phone)
            time.sleep(1)
            
            print("查找验证码按钮...")
            code_button = self.page.locator('button:has-text("获取验证码")').first
            if not code_button.is_visible():
                code_button = self.page.locator('text=获取验证码').first
            
            if code_button.is_visible():
                print("点击获取验证码")
                code_button.click()
                time.sleep(2)
                
                print(f"请输入收到的验证码（当前密码字段: {password}）")
                print("提示：如果需要手动输入验证码，请在config.json中更新password字段")
                
                code_input = self.page.locator('input[placeholder*="验证码"]').first
                if code_input.is_visible():
                    code_input.fill(password)
                    time.sleep(1)
                    
                    submit_button = self.page.locator('button:has-text("登录")').first
                    if not submit_button.is_visible():
                        submit_button = self.page.locator('button:has-text("确认")').first
                    
                    if submit_button.is_visible():
                        print("点击登录")
                        submit_button.click()
                        time.sleep(3)
                        
                        print("登录流程完成")
                        return True
        
        print("登录流程完成（可能已登录或需要手动操作）")
        return True

    def close(self):
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
