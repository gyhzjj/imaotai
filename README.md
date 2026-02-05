# i茅台智能抢购工具

基于Python + Playwright的极简抢购工具，通过访问i茅台H5移动端页面实现自动抢购，支持在手机Termux环境中运行。

## 环境要求

- Android手机
- Termux应用
- Python 3.8+
- 网络连接

## 安装步骤

### 1. 安装Termux
从F-Droid或GitHub下载Termux应用并安装

### 2. 更新Termux包管理器
```bash
pkg update && pkg upgrade
```

### 3. 安装Python
```bash
pkg install python
```

### 4. 安装依赖
```bash
pip install playwright
```

### 5. 安装Playwright浏览器
```bash
playwright install chromium
```

## 配置说明

编辑 `config.json` 文件，填写以下信息：

```json
{
  "user": {
    "phone": "你的手机号",
    "password": "你的验证码"
  },
  "products": [
    {
      "name": "飞天53%vol 500ml贵州茅台酒（带杯）",
      "url": "https://h5.moutai519.com.cn/...",
      "purchase_time": "09:00:00"
    }
  ],
  "settings": {
    "headless": false,
    "timeout": 30,
    "retry_times": 3,
    "advance_seconds": 2
  }
}
```

### 配置项说明

- `phone`: i茅台账号手机号
- `password`: 登录验证码（需要手动获取并更新到config.json）
- `name`: 商品名称（用于日志显示）
- `url`: i茅台H5商品页面URL
- `purchase_time`: 抢购时间（格式：HH:MM:SS）
- `headless`: 是否无头模式运行（建议设为false，方便观察）
- `retry_times`: 抢购失败重试次数
- `advance_seconds`: 提前多少秒准备抢购

## 使用方法

### 1. 运行程序
```bash
python main.py
```

### 2. 登录流程
- 程序会自动打开i茅台H5页面（https://h5.moutai519.com.cn/）
- 自动点击登录按钮
- 自动输入手机号
- 自动点击获取验证码
- **需要手动输入验证码到config.json的password字段**
- 程序会使用config.json中的验证码完成登录

### 3. 自动抢购
- 程序会在设定时间前2秒开始准备
- 自动访问商品页面
- 自动点击购买按钮
- 自动确认订单

## 获取商品URL

1. 在手机浏览器中访问 https://h5.moutai519.com.cn/
2. 登录i茅台账号
3. 找到"飞天53%vol 500ml贵州茅台酒（带杯）"商品
4. 进入商品详情页
5. 复制浏览器地址栏的URL到config.json

## 注意事项

1. **验证码问题**：i茅台使用短信验证码登录，程序会自动点击获取验证码，但需要手动将收到的验证码输入到config.json的password字段
2. **URL获取**：需要在i茅台H5页面获取商品页面URL
3. **网络延迟**：建议在抢购前测试网络速度
4. **账号安全**：请妥善保管账号信息，不要泄露
5. **首次使用**：建议设置 `headless: false` 观察运行情况

## 优化建议

1. 使用更快的网络环境
2. 提前测试登录流程
3. 根据实际情况调整 `advance_seconds` 参数
4. 首次使用建议设置 `headless: false` 观察运行情况
5. 在抢购前手动登录一次，确保账号状态正常

## 常见问题

### Q: Playwright安装失败
A: 确保网络连接正常，或使用国内镜像源

### Q: 浏览器启动失败
A: 运行 `playwright install chromium` 重新安装浏览器

### Q: 登录失败
A: 检查手机号和验证码是否正确，确保验证码已更新到config.json

### Q: 抢购失败
A: 可能是网络延迟或商品已售罄，可增加 `retry_times` 参数

### Q: 找不到购买按钮
A: 检查商品URL是否正确，确保在抢购时间内

## 项目结构

```
imaotai/
├── config.json       # 配置文件
├── main.py           # 主程序
├── login.py          # 登录模块
├── purchase.py       # 抢购模块
├── config.py         # 配置管理
├── test_browser.py   # 浏览器测试脚本
├── requirements.txt  # 依赖包
└── README.md         # 说明文档
```

## 免责声明

本工具仅供学习交流使用，请遵守i茅台平台规则，不要用于商业用途。使用本工具产生的任何后果由使用者自行承担。
