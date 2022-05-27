# wecom-bot

## 说明
因为个人需要写的企业微信群机器人对接工具，用于ci构建（因shell解析json响应做防范代码较麻烦），未必会增加其他功能。

## 引用

[企业微信](https://work.weixin.qq.com/)

[群机器人技术文档](https://developer.work.weixin.qq.com/document/path/91770)

[PyInstaller 官方文档](https://pyinstaller.org/en/stable/)

[为什么选择 PyInstaller](https://docs.python-guide.org/shipping/freezing/#comparison-of-freezing-tools)

## 如何构建

### 安装依赖
```shell
# 如因连接外网问题无法直接install
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

pip install -r requirements.txt
```

### 打包可执行文件

**Mac / Linux**
```shell
pyinstaller -F send_file.py -n send_file_$(uname | awk '{print tolower($1)}')_$(arch)
```

## 如何使用

**Mac**

如果需要在文件发送前推送信息说明
```shell
WECOM_WEBHOOK_KEY="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
dist/send_file_darwin_arm64 $WECOM_WEBHOOK_KEY test/hello.txt test/message.md
```

只需要发送文件的场景
```shell
WECOM_WEBHOOK_KEY="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
dist/send_file_darwin_arm64 $WECOM_WEBHOOK_KEY test/hello.txt
```

## 注意
通过`PyInstaller`构建的可执行文件只能在与构建环境相似的平台才能执行。