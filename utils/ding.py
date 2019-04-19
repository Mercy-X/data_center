"""
author: Mercy
version: 1.0 | 2019-04-19
description:
    钉钉机器人消息发送模块
    WEB_HOOK_URL设置为钉钉的webhook，详见 https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq
version_description:
    1.0: 初始版本
"""

import json
import requests

WEB_HOOK_URL = ''


def __send(send_data, url=None):
    """
    发送post请求
    :param url:
    :param send_data: DICT
    :return:
    """

    if url is None:
        url = WEB_HOOK_URL
    requests.post(
        url=url,
        data=json.dumps(send_data),
        headers={
            'Content-Type': 'application/json;charset=UTF-8',
        }
    )


def send_msg(msg, at=None, url=None):
    """
    发送信息
    :param msg: STR 消息
    :param at: LIST 需要at的手机号码
    :param url STR WEBHOOK_URL
    :return:
    """

    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }
    if at is not None:
        data['at'] = {
            "atMobiles": at
        }
    return __send(data, url)


def send_markdown(title, text, at=None, url=None):
    """
    发送markdown信息
    :param title: STR 标题
    :param text: STR 内容
    :param at: LIST at对象
    :param url: STR WEBHOOK_URL
    :return:
    """

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": text
        }
    }
    if at is not None:
        data['at'] = {
            "atMobiles": at
        }
    return __send(data, url)


def send_card(title, text, btns, btn_orientation='0', url=None):
    """
    发送卡片信息
    :param title:
    :param text:
    :param btns:
    :param btn_orientation:
    :param url:
    :return:
    """

    data = {
        "msgtype": "actionCard",
        "actionCard": {
            "title": title,
            "hideAvatar": "0",
            "btnOrientation": btn_orientation,
            "text": text,
            "btns": btns
        }
    }
    return __send(data, url)
