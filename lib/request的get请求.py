# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/15 8:56
# Author        : smart
# @File         :request的get请求.py
# @Software     :PyCharm
import requests

ur=requests.get("http://127.0.0.1")
print(ur.text)
print(ur.content)
print(ur.url)
print(ur.encoding)
print(ur.cookies)






