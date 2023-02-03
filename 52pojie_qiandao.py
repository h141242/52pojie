# -*- coding: utf-8 -*
'''
new Env('吾爱破解签到');
'''


import os
import datetime
from notify import send  # 导入青龙消息通知模块
import requests
from bs4 import BeautifulSoup

cookie = os.environ['Pojie52_COOKIE']
url1 = 'https://www.52pojie.cn/CSPDREL2hvbWUucGhwP21vZD10YXNrJmRvPWFwcGx5JmlkPTImcmVmZXJlcj0lMkY=?wzwscspd=MC4wLjAuMA=='
url2 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2F'
url3 = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}
r = requests.get(url1, headers=headers, allow_redirects=False)
s_cookie = r.headers['Set-Cookie']
print(s_cookie)
cookie = cookie + s_cookie
headers['Cookie'] = cookie
r = requests.get(url2, headers=headers, allow_redirects=False)
s_cookie = r.headers['Set-Cookie']
print(s_cookie)
cookie = cookie + s_cookie
headers['Cookie'] = cookie
r = requests.get(url3, headers=headers)
r_data = BeautifulSoup(r.text, "html.parser")
print(r_data)
jx_data = r_data.find("div", id="messagetext").find("p").text

if "您需要先登录才能继续本操作" in jx_data:
    sign_msg="❌Cookie 失效"
    print(sign_msg)
elif "恭喜" in jx_data:
    sign_msg="⭐签到成功"
    print(sign_msg)
elif "不是进行中的任务" in jx_data:
    sign_msg="💔今日已签到"
    print(sign_msg)
else:
    sign_msg="⚡签到失败"
    print(sign_msg)

send('吾爱破解签到', sign_msg+'\n\n本通知 By HY-吾爱破解\n通知时间:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

