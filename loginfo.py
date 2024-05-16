# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/26 8:56
# Author        : smart
# @File         :loginfo.py
# @Software     :PyCharm
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='log/log.txt',
    # encoding='utf-8',
    filemode='a'
        )






if __name__ == '__main__':
    logging.info("接口测试")





