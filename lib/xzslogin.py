# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/17 9:43
# Author        : smart
# @File         :xzslogin.py
# @Software     :PyCharm
import requests
class login():
    def slogin(self,us,ps):
        ur="http://192.168.55.31:8000/api/user/login"
        # data={"userName":"s2","password":"123456","remember":False}
        data = {"userName": us, "password": ps, "remember": False}
        f=requests.post(ur,json=data)
        # print(f.text)
        return f




if __name__ == '__main__':
    s=login()
    print(s.slogin("s2", "123456").text)




























