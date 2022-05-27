# -*- coding: utf-8 -*-

# 第三方
import os
import sys
import json
import requests


def load_markdown_message(__message_path) -> str:
    """
    获取消息文件内容

    :param __message_path: 消息文件路径
    :type __message_path: str
    :returns: json
    :rtype: dict
    """
    __f = open(__message_path, 'r', encoding="utf-8")
    try:
        __text = __f.read()
    finally:
        __f.close()
    return __text


def get_mime_type(__file_path) -> str:
    """
    判断文件的mime_type

    :param __file_path: 文件路径
    :type __file_path: str
    :returns: mime_type
    :rtype: str
    """
    __mime_type_other = '*/*'
    __mime_type_mapping = {
        '.3gp': 'video/3gpp',
        '.apk': 'application/vnd.android.package-archive',
        '.asf': 'video/x-ms-asf',
        '.avi': 'video/x-msvideo',
        '.bin': 'application/octet-stream',
        '.bmp': 'image/bmp',
        '.c': 'text/plain',
        '.class': 'application/octet-stream',
        '.conf': 'text/plain',
        '.cpp': 'text/plain',
        '.doc': 'application/msword',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.xls': 'application/vnd.ms-excel',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        '.exe': 'application/octet-stream',
        '.gif': 'image/gif',
        '.gtar': 'application/x-gtar',
        '.gz': 'application/x-gzip',
        '.h': 'text/plain',
        '.htm': 'text/html',
        '.html': 'text/html',
        '.jar': 'application/java-archive',
        '.java': 'text/plain',
        '.jpeg': 'image/jpeg',
        '.jpg': 'image/jpeg',
        '.js': 'application/x-javascript',
        '.log': 'text/plain',
        '.m3u': 'audio/x-mpegurl',
        '.m4a': 'audio/mp4a-latm',
        '.m4b': 'audio/mp4a-latm',
        '.m4p': 'audio/mp4a-latm',
        '.m4u': 'video/vnd.mpegurl',
        '.m4v': 'video/x-m4v',
        '.mov': 'video/quicktime',
        '.mp2': 'audio/x-mpeg',
        '.mp3': 'audio/x-mpeg',
        '.mp4': 'video/mp4',
        '.mpc': 'application/vnd.mpohun.certificate',
        '.mpe': 'video/mpeg',
        '.mpeg': 'video/mpeg',
        '.mpg': 'video/mpeg',
        '.mpg4': 'video/mp4',
        '.mpga': 'audio/mpeg',
        '.msg': 'application/vnd.ms-outlook',
        '.ogg': 'audio/ogg',
        '.pdf': 'application/pdf',
        '.png': 'image/png',
        '.pps': 'application/vnd.ms-powerpoint',
        '.ppt': 'application/vnd.ms-powerpoint',
        '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        '.prop': 'text/plain',
        '.rc': 'text/plain',
        '.rmvb': 'audio/x-pn-realaudio',
        '.rtf': 'application/rtf',
        '.sh': 'text/plain',
        '.tar': 'application/x-tar',
        '.tgz': 'application/x-compressed',
        '.txt': 'text/plain',
        '.wav': 'audio/x-wav',
        '.wma': 'audio/x-ms-wma',
        '.wmv': 'audio/x-ms-wmv',
        '.wps': 'application/vnd.ms-works',
        '.xml': 'text/plain',
        '.z': 'application/x-compress',
        '.zip': 'application/x-zip-compressed',
        '': __mime_type_other
    }
    __file_extension = os.path.splitext(__file_path)
    __file_mime_type = __mime_type_mapping.get(__file_extension[1])
    if __file_mime_type is None:
        __file_mime_type = __mime_type_other
    return __file_mime_type


def upload_media_file(__file_name, __file_path, __mime_type) -> str:
    """
    上传apk文件

    :param __file_name: 文件名
    :type __file_name: str
    :param __file_path: 文件路径
    :type __file_path: str
    :param __mime_type: 文件mime_type
    :type __mime_type: str
    :returns: media_id
    :rtype: str
    """
    __upload_media_api = "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=" + wecom_bot_key + "&type=file"
    __headers = {
        "Accept": "application/json",
        "Content-Type": "multipart/form-data",
        "Cookie": "expire=1; LANGUAGE=zh-cn"
    }
    __payload = {
        'Content-Disposition': 'form-data',
        'Content-Type': 'application/octet-stream',
        'name': 'media',
        'filename': __file_name,
        'filelength': os.path.getsize(__file_path)
    }
    __files = [
        (
            'file',
            (__file_name, open(__file_path, 'rb'), __mime_type)
        )
    ]

    print('++ 开始调用上传文件接口...')
    __response = requests.post(__upload_media_api, headers=__headers, data=__payload, files=__files, timeout=10)
    if __response.status_code != 200:
        raise Exception('请求上传文件Http返回码错误: {}'.format(__response.status_code))
    __response_json = json.loads(__response.content)
    if __response_json['errcode'] != 0:
        raise Exception('请求上传文件接口返回码错误: {}'.format(__response_json.code))
    print('++ 调用上传文件接口成功。')

    return __response_json['media_id']


def send_media_message(__media_id) -> None:
    """
    发送Media消息

    :param __media_id: __media_id
    :type __media_id: str
    """
    __send_api = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + wecom_bot_key
    __headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": "expire=1; LANGUAGE=zh-cn"
    }
    __payload = {
        'msgtype': 'file',
        'file': {
            'media_id': __media_id
        }
    }

    print('++ 开始调用发送Media消息接口...')
    __response = requests.post(__send_api, headers=__headers, json=__payload, timeout=10)
    if __response.status_code != 200:
        raise Exception('请求发送Media消息Http返回码错误: {}'.format(__response.status_code))
    __response_json = json.loads(__response.content)
    if __response_json['errcode'] != 0:
        raise Exception('请求发送Media消息接口返回码错误: {}'.format(__response_json.code))
    print('++ 调用发送Media消息接口成功。')


def send_markdown_message(__message_text) -> None:
    """
    发送Markdown消息

    :param __message_text: Markdown消息文本
    :type __message_text: str
    """
    __send_api = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + wecom_bot_key
    __headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": "expire=1; LANGUAGE=zh-cn"
    }
    __payload = {
        'msgtype': 'markdown',
        'markdown': {
            'content': __message_text
        }
    }

    print('++ 开始调用发送Markdown消息接口...')
    __response = requests.post(__send_api, headers=__headers, json=__payload, timeout=10)
    if __response.status_code != 200:
        raise Exception('请求发送Markdown消息Http返回码错误: {}'.format(__response.status_code))
    __response_json = json.loads(__response.content)
    if __response_json['errcode'] != 0:
        raise Exception('请求发送Markdown消息接口返回码错误: {}'.format(__response_json.code))
    print('++ 调用发送Markdown消息接口成功。')


# Main
if __name__ == '__main__':
    # 接收参数
    if len(sys.argv) < 2:
        raise Exception('执行参数异常，参数格式: WeCom提供的Key、文件路径、Markdown消息文件路径')
    wecom_bot_key = sys.argv[1]
    file_path = sys.argv[2]

    # 存在markdown消息时获取
    if len(sys.argv) > 3:
        message_path = sys.argv[3]
        __message_text = load_markdown_message(message_path)
    else:
        message_path = None
        __message_text = None

    # 上传文件
    __file_name = os.path.basename(file_path)
    __mime_type = get_mime_type(file_path)
    __media_id = upload_media_file(__file_name, file_path, __mime_type)

    # 推送消息
    if message_path is not None:
        send_markdown_message(__message_text)
    send_media_message(__media_id)
