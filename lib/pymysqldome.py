# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/18 17:00
# Author        : smart
# @File         :pymysql.py
# @Software     :PyCharm
import pymysql
try:
    con=pymysql.connect(host="localhost",port=3306,
                        user="root",password="root",
                        database="p2p",charset='utf8'
    )
    cur=con.cursor()
    cur.execute("select * from user")
    data=cur.fetchone()
    print(data)
except Exception as e:
    print("出错了,错误信息为{}".format(e))
finally:
    if cur:cur.close()
    if con:con.close()

























