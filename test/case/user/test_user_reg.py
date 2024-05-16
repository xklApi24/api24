# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/5/6 11:11
# Author        : smart
# @File         :test_user_reg.py
# @Software     :PyCharm
from test.case.BaseCase import BaseCase
from lib.db import *
import json

class TestUesrReg(BaseCase):
    def test_user_reg(self):
        case_data=self.get_case_data("reg_ok")
        userName=json.loads(case_data.get("args")).get('userName')
        if cherk_user(userName):
            del_user(userName)
        self.send_request(case_data)
        self.assertTrue(cherk_user((userName)))
        del_user(userName)

    def test_user_reg_exist(self):
        case_data = self.get_case_data("reg_err")
        userName = json.loads(case_data.get("args")).get('userName')
        # 环境检查
        if not cherk_user(userName):
            add_user(userName, '123456')
        # 发送请求
        self.send_request(case_data)


