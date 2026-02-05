from playwright.sync_api import sync_playwright
from config import Config
import time
from datetime import datetime


class Purchase:
    def __init__(self, config: Config, page):
        self.config = config
        self.page = page
        self.settings = config.get_settings()

    def wait_for_purchase_time(self, purchase_time):
        while True:
            now = datetime.now()
            target_time = datetime.strptime(purchase_time, '%H:%M:%S').replace(
                year=now.year,
                month=now.month,
                day=now.day
            )
            
            advance_seconds = self.settings.get('advance_seconds', 2)
            wait_time = (target_time - now).total_seconds() - advance_seconds
            
            if wait_time <= 0:
                print(f"抢购时间到！当前时间: {now.strftime('%H:%M:%S')}")
                break
            
            if wait_time > 60:
                print(f"等待抢购时间: {purchase_time}，还需等待 {int(wait_time // 60)} 分钟")
                time.sleep(60)
            else:
                print(f"即将开始抢购，还需等待 {int(wait_time)} 秒")
                time.sleep(1)

    def purchase_product(self, product):
        product_url = product.get('url', '')
        product_name = product.get('name', '')
        quantity = product.get('quantity', 1)
        
        if not product_url:
            print(f"商品 {product_name} 未配置URL，跳过")
            return False
        
        print(f"开始抢购商品: {product_name}")
        print(f"购买数量: {quantity} 瓶")
        print(f"访问商品页面: {product_url}")
        
        self.page.goto(product_url)
        time.sleep(2)
        
        print("查找购买按钮...")
        purchase_button = self.page.locator('button:has-text("立即申购")').first
        if not purchase_button.is_visible():
            purchase_button = self.page.locator('button:has-text("立即购买")').first
        if not purchase_button.is_visible():
            purchase_button = self.page.locator('button:has-text("申购")').first
        if not purchase_button.is_visible():
            purchase_button = self.page.locator('text=立即申购').first
        if not purchase_button.is_visible():
            purchase_button = self.page.locator('text=申购').first
        
        if purchase_button.is_visible():
            print("点击购买按钮")
            purchase_button.click()
            time.sleep(1)
            
            print("设置购买数量...")
            self._set_quantity(quantity)
            time.sleep(1)
            
            print("查找确认按钮...")
            confirm_button = self.page.locator('button:has-text("确认")').first
            if not confirm_button.is_visible():
                confirm_button = self.page.locator('button:has-text("提交")').first
            if not confirm_button.is_visible():
                confirm_button = self.page.locator('button:has-text("确定")').first
            
            if confirm_button.is_visible():
                print("点击确认订单")
                confirm_button.click()
                time.sleep(2)
                
                print("检查抢购结果...")
                success_text = self.page.locator('text=申购成功').first
                if not success_text.is_visible():
                    success_text = self.page.locator('text=申购成功').first
                if not success_text.is_visible():
                    success_text = self.page.locator('text=提交成功').first
                
                if success_text.is_visible():
                    print(f"✓ 商品 {product_name} 抢购成功！购买数量: {quantity} 瓶")
                    return True
            
            print(f"✗ 商品 {product_name} 抢购失败")
            return False
        else:
            print(f"未找到购买按钮，商品可能已售罄或未到抢购时间")
            print("提示：请检查商品URL是否正确")
            return False

    def _set_quantity(self, quantity):
        quantity_input = self.page.locator('input[type="number"]').first
        if not quantity_input.is_visible():
            quantity_input = self.page.locator('input[placeholder*="数量"]').first
        if not quantity_input.is_visible():
            quantity_input = self.page.locator('input[placeholder*="购买数量"]').first
        
        if quantity_input.is_visible():
            print(f"设置数量为: {quantity}")
            quantity_input.fill(str(quantity))
            return True
        
        plus_button = self.page.locator('button:has-text("+")').first
        minus_button = self.page.locator('button:has-text("-")').first
        
        if plus_button.is_visible() and minus_button.is_visible():
            print(f"使用加减按钮设置数量: {quantity}")
            current_quantity = 1
            while current_quantity < quantity:
                plus_button.click()
                current_quantity += 1
                time.sleep(0.1)
            return True
        
        print("未找到数量选择器，使用默认数量")
        return False

    def run_purchase(self):
        products = self.config.get_products()
        
        for product in products:
            purchase_time = product.get('purchase_time', '09:00:00')
            print(f"等待抢购时间: {purchase_time}")
            
            self.wait_for_purchase_time(purchase_time)
            
            retry_times = self.settings.get('retry_times', 3)
            for i in range(retry_times):
                print(f"第 {i + 1} 次尝试抢购")
                success = self.purchase_product(product)
                if success:
                    print("抢购成功，程序结束")
                    break
                time.sleep(0.5)
