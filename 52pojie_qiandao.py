# -*- coding: utf-8 -*
'''
new Env('吾爱破解签到');
'''

import os
import datetime
import requests
from bs4 import BeautifulSoup
from notify import send  # 导入青龙消息通知模块

def sign(cookie):
    result = ""
    headers = {
        "Cookie": cookie,
        "ContentType": "text/html;charset=gbk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2", headers=headers
    )
    fa = requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2", headers=headers
    )

    fb = BeautifulSoup(fa.text, "html.parser")
    fc = fb.find("div", id="messagetext").find("p").text

    if "您需要先登录才能继续本操作" in fc:
        result += "Cookie 失效"
    elif "恭喜" in fc:
        result += "签到成功"
    elif "不是进行中的任务" in fc:
        result += "今日已签到"
    else:
        result += "签到失败"
    return result 

def main():
    cookie = os.environ['Pojie52_COOKIE']
    sign_msg = sign(cookie=cookie)
    #print(sign_msg)

    send('吾爱破解签到', '⭐'+sign_msg+'\n\n本通知 By HY-吾爱破解\n通知时间:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    main()
