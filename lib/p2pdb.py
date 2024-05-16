# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/19 11:13
# Author        : smart
# @File         :p2pdb.py
# @Software     :PyCharm
import pymysql

import sys
sys.path.append('..')
# 创建链接
def con():
    con = pymysql.connect(host="localhost",user="root",
                        password="root",port=3306,
                        database="p2p",charset="utf8")
    return con
#创建sql查询
def cursor(sql):
    # 创建连接
    conm = con()
    # 创建游标
    cur = conm.cursor()
    # 执行sql语句
    cur.execute(sql)
    a = cur.fetchall()
    return a
def change_db(sql):
    conm = con()
    cur = conm.cursor()
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交操作
        conm.commit()
    except Exception as a:
        # 回滚
        conm.rollback()
    finally:
        # 关闭连接
        cur.close()
        # 关闭游标
        conm.close()
#     查询
def check_user(proNum):
    sql = "SELECT * FROM product WHERE proNum = '{}'".format(proNum)
    # 执行sql语句
    a = cursor(sql)
    return True if a else False
#  添加

def add_user(proNum,proName,proLimit,annualized):
    sql = "insert into product(proNum,proName,proLimit,annualized) values ({}','{}','{}','{}')".format(proNum,proName,proLimit,annualized)
    # 执行添加sql语句
    print(sql)
    a = change_db(sql)
    return True if a else False
# 删除
def del_user(proNum):
    # 执行删除sql语句
    sql = "delete from product where id = '{}'".format(proNum)
    a = change_db(sql)
    return True if a else False



# import pymysql
# # 建立数据库连接
# def coon():
#     cond=pymysql.connect(
#         host="localhost",port=3306,
#         user="root",password="root",
#         database="p2p",charset='utf8'
#     )
#     return cond
#
# # 封装数据库的查询操作
# def quedb(sql):
#     cods=coon()
#     csr=cods.cursor()
#     csr.execute(sql)
#     rst=csr.fetchall()
#     return rst
#
# # 封装数据库的更改操作
# def change_db(sql):
#     cosn=coon()
#     cur=cosn.cursor()
#     try:
#         cur.execute(sql)
#         cosn.commit()
#     except Exception as e:
#         cosn.rollback()
#     finally:
#         cur.close()
#         cosn.close()
#
# # 封装常用的数据库操作
# def cherk_user(name):
#     sql="select * from product where proNum = '{}'".format(name)
#     rust=quedb(sql)
#     return True if rust else False
#
# def add_user(proNum,proName,proLimit,annualized):
#     sql="insert into product(proNum,proName,proLimit,annualized) values('{}','{}','{}','{}') ".format(proNum,proName,proLimit,annualized)
#     change_db(sql)
#
# def del_user(name):
#     sql="delete from product where proNum = '{}'".format(name)
#     change_db(sql)