from playwright.sync_api import sync_playwright

def test_browser():
    try:
        print("正在启动浏览器...")
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            print("浏览器启动成功")
            
            page = browser.new_context(
                viewport={'width': 375, 'height': 812},
                user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
            ).new_page()
            
            print("正在访问i茅台H5页面...")
            page.goto('https://h5.moutai519.com.cn/')
            
            print("页面加载完成，等待3秒后关闭...")
            page.wait_for_timeout(3000)
            
            browser.close()
            print("测试成功！")
            
    except Exception as e:
        print(f"测试失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_browser()
