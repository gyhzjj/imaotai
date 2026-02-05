# 安卓手机运行指南

本指南详细介绍如何在安卓手机上使用Termux运行i茅台智能抢购工具。

## 一、准备工作

### 1. 安装Termux

#### 方法一：从F-Droid安装（推荐）
1. 在手机浏览器访问：https://f-droid.org/packages/com.termux/
2. 下载并安装Termux应用

#### 方法二：从GitHub安装
1. 访问：https://github.com/termux/termux-app/releases
2. 下载最新的APK文件
3. 在手机上安装APK

### 2. 授予Termux存储权限
首次打开Termux后，运行以下命令：
```bash
termux-setup-storage
```
选择"允许"授予存储权限。

## 二、安装Python环境

### 1. 更新包管理器
```bash
pkg update && pkg upgrade
```

### 2. 安装Python
```bash
pkg install python
```

### 3. 验证Python安装
```bash
python --version
```
应该显示Python 3.8或更高版本。

## 三、安装项目文件

### 方法一：使用Git克隆（推荐）

1. 安装Git
```bash
pkg install git
```

2. 克隆项目（如果有Git仓库）
```bash
git clone <你的仓库地址>
cd imaotai
```

### 方法二：手动传输文件

1. 在电脑上打包项目文件
2. 通过以下方式传输到手机：
   - USB数据线传输
   - 微信/QQ文件传输
   - 云盘（百度网盘、阿里云盘等）

3. 将文件复制到Termux可访问的目录
```bash
cd ~/storage/downloads
```

4. 解压或复制文件到工作目录
```bash
mkdir -p ~/imaotai
cp -r ~/storage/downloads/imaotai/* ~/imaotai/
cd ~/imaotai
```

## 四、安装Python依赖

### 1. 升级pip
```bash
python -m pip install --upgrade pip
```

### 2. 安装Playwright
```bash
pip install playwright
```

### 3. 安装Chromium浏览器
```bash
playwright install chromium
```

注意：这一步可能需要较长时间，请确保网络连接稳定。

## 五、配置程序

### 1. 编辑配置文件
```bash
nano config.json
```

### 2. 填写配置信息
```json
{
  "user": {
    "phone": "你的手机号",
    "password": ""
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

### 3. 保存并退出
- 按 `Ctrl + O` 保存
- 按 `Enter` 确认
- 按 `Ctrl + X` 退出

## 六、获取商品URL

1. 在手机浏览器访问：https://h5.moutai519.com.cn/
2. 登录i茅台账号
3. 找到"飞天53%vol 500ml贵州茅台酒（带杯）"商品
4. 进入商品详情页
5. 复制浏览器地址栏的URL
6. 将URL填入config.json的url字段

## 七、运行程序

### 1. 运行主程序
```bash
python main.py
```

### 2. 登录流程
- 程序会自动打开浏览器窗口
- 自动点击登录按钮
- 自动输入手机号
- 自动点击获取验证码
- 收到短信后，手动编辑config.json，将验证码填入password字段
- 重新运行程序完成登录

### 3. 自动抢购
- 程序会等待到设定的抢购时间
- 自动访问商品页面
- 自动点击购买按钮
- 自动确认订单

## 八、常用命令

### 查看文件列表
```bash
ls
```

### 编辑配置文件
```bash
nano config.json
```

### 查看日志
```bash
python main.py 2>&1 | tee run.log
```

### 后台运行
```bash
nohup python main.py > run.log 2>&1 &
```

### 查看后台进程
```bash
ps aux | grep python
```

### 停止后台进程
```bash
pkill -f "python main.py"
```

## 九、常见问题

### Q1: Termux安装失败
A: 确保从官方渠道下载Termux，不要使用Google Play商店的版本（已停止维护）。

### Q2: pip安装速度慢
A: 使用国内镜像源：
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple playwright
```

### Q3: Playwright安装Chromium失败
A: 确保网络连接稳定，或使用代理：
```bash
export PLAYWRIGHT_DOWNLOAD_HOST=https://playwright.azureedge.net
playwright install chromium
```

### Q4: 浏览器无法启动
A: Termux可能需要额外依赖：
```bash
pkg install libllvm
```

### Q5: 程序运行时闪退
A: 查看错误日志：
```bash
python main.py 2>&1 | tee error.log
```

### Q6: 键盘输入不方便
A: 安装Termux:API和额外键盘：
```bash
pkg install termux-api
```
然后在设置中启用Termux键盘。

### Q7: 存储空间不足
A: 清理不必要的文件：
```bash
pkg clean
```

### Q8: 如何保持Termux后台运行
A: 使用Termux:Boot或nohup命令：
```bash
nohup python main.py > run.log 2>&1 &
```

## 十、优化建议

### 1. 提高网络速度
- 使用5G或WiFi网络
- 关闭其他占用网络的应用
- 避免在网络高峰期抢购

### 2. 优化Termux性能
- 关闭不必要的后台应用
- 使用性能模式运行
- 定期清理缓存

### 3. 提前测试
- 在抢购前测试登录流程
- 测试网络速度
- 验证配置文件正确性

### 4. 监控运行状态
- 使用日志记录运行情况
- 定期检查程序状态
- 及时处理异常情况

## 十一、安全建议

1. 不要将config.json上传到公共仓库
2. 定期更换密码
3. 不要在公共网络下运行
4. 及时更新Termux和Python版本

## 十二、项目文件清单

确保以下文件都在工作目录中：
```
imaotai/
├── config.json       # 配置文件
├── main.py           # 主程序
├── login.py          # 登录模块
├── purchase.py       # 抢购模块
├── config.py         # 配置管理
├── test_browser.py   # 浏览器测试脚本
├── requirements.txt  # 依赖包
├── README.md         # 说明文档
└── ANDROID_GUIDE.md  # 安卓运行指南（本文件）
```

## 十三、快速开始

如果你已经熟悉Termux，可以快速开始：

```bash
# 1. 安装依赖
pkg update && pkg upgrade
pkg install python git

# 2. 克隆项目（如果有仓库）
git clone <仓库地址>
cd imaotai

# 3. 安装Python包
pip install playwright
playwright install chromium

# 4. 配置程序
nano config.json

# 5. 运行程序
python main.py
```

## 十四、联系支持

如果遇到问题，请：
1. 查看本文档的常见问题部分
2. 检查错误日志
3. 确认所有依赖都已正确安装
4. 验证配置文件格式正确

---

**祝您抢购成功！**
