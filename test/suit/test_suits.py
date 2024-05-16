# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/5/7 15:09
# Author        : smart
# @File         :test_suit.py
# @Software     :PyCharm
import unittest,sys
sys.path.append("../..")
from test.case.user.test_user_reg import TestUesrReg
from test.case.user.test_user_login import TestUserLogin

smoke_suit=unittest.TestSuite()
smoke_suit.addTests([TestUserLogin("test_login_success"),TestUesrReg("test_user_reg")])

def get_suit(suit_name):
    suit_name = unittest.TestSuite()
    suit_name.addTests([TestUserLogin("test_login_success"), TestUesrReg("test_user_reg")])
    return suit_name


unittest.TextTestRunner(verbosity=2).run(smoke_suit)


