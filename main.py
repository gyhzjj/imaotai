from config import Config
from login import Login
from purchase import Purchase


def main():
    try:
        config = Config('config.json')
        
        login = Login(config)
        page = login.start_browser()
        
        if login.login():
            print("登录成功，开始监控商品...")
            
            purchase = Purchase(config, page)
            purchase.run_purchase()
        
        login.close()
        
    except FileNotFoundError as e:
        print(f"错误: {e}")
        print("请确保config.json文件存在并正确配置")
    except ValueError as e:
        print(f"配置错误: {e}")
    except Exception as e:
        print(f"程序运行出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
