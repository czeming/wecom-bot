# wecom-bot

## Describe
The toolkit for the wecom bot.

## References

[What's Wecom](https://work.weixin.qq.com/)

[Wecom webhook](https://developer.work.weixin.qq.com/document/path/91770)

[PyInstaller Manual](https://pyinstaller.org/en/stable/)

[Why PyInstaller](https://docs.python-guide.org/shipping/freezing/#comparison-of-freezing-tools)

## How to Build

### Install requirements
```shell
pip install -r requirements.txt
```

### Pack executables

**Mac / Linux** 
```shell
pyinstaller -F send_file.py -n send_file_$(uname | awk '{print tolower($1)}')_$(arch)
```

## How to Use

**Mac**

If you need to explain the information before sending the file.
```shell
WECOM_WEBHOOK_KEY="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
dist/send_file_darwin_arm64 $WECOM_WEBHOOK_KEY test/hello.txt test/message.md
```

only file
```shell
WECOM_WEBHOOK_KEY="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
dist/send_file_darwin_arm64 $WECOM_WEBHOOK_KEY test/hello.txt
```

## Be careful

> PyInstaller is tested against Windows, MacOS X, and Linux. However, it is not a cross-compiler; to make a Windows app you run PyInstaller on Windows, and to make a Linux app you run it on Linux, etc.