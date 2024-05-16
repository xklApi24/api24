# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/19 9:02
# Author        : smart
# @File         :db.py
# @Software     :PyCharm
import logging
import pymysql
from config.config import *


# 建立数据库连接
def coon():
    cond=pymysql.connect(
        host=db_host,port=db_port,
        user=db_user,password=db_password,
        database=db,charset='utf8'
    )
    return cond

# 封装数据库的查询操作
def quedb(sql):
    cods=coon()
    csr=cods.cursor()

    csr.execute(sql)
    rst=csr.fetchall()
    return rst

# 封装数据库的更改操作
def change_db(sql):
    cosn=coon()
    cur=cosn.cursor()
    try:
        cur.execute(sql)
        cosn.commit()
    except Exception as e:
        cosn.rollback()
    finally:
        cur.close()
        cosn.close()

# 封装常用的数据库操作
def cherk_user(name):
    sql="select * from t_user where user_name = '{}'".format(name)
    rust=quedb(sql)
    return True if rust else False

def add_user(name,password):
    sql="insert into t_user(user_name,password) values('{}','{}') ".format(name,password)
    change_db(sql)

def del_user(name):
    sql="delete from t_user where user_name = '{}'".format(name)
    change_db(sql)














