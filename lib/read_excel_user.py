# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/23 15:19
# Author        : smart
# @File         :read_excel_user.py
# @Software     :PyCharm
import xlrd
# 打开文件
wb=xlrd.open_workbook("../data/user_data.xlsx")
# 打开工作簿
sti=wb.sheet_by_name("test_user_reg")
# 行
print(sti.nrows)
# 列
print(sti.ncols)
# 获取第一行第一列的数据
print(sti.cell(0, 0).value)
# 通过循环，把每一行的数据当列表输出
for  i in range(sti.nrows):
    print(sti.row_values(i))
# 获取第一行中的所有数据
print(sti.row_values(0))

# keys = sheet1.row_values(0)
# # 把两个列表 转换为字典
# dict1 =dict(zip(sheet1.row_values(0),sheet1.row_values(1)))
# print(dict1)
# list =[]
#
# # 通过循环 把每一行的数据当列表输出
# # 输出第二行开始的值
# for i in range(1,sheet1.nrows):
#    list.append(dict(zip(keys,sheet1.row_values(i))))
#
# print(list)





























# keys = sheet1.row_values(0)
# # 把两个列表 转换为字典
# dict1 =dict(zip(sheet1.row_values(0),sheet1.row_values(1)))
# print(dict1)
# list =[]
#
# # 通过循环 把每一行的数据当列表输出
# # 输出第二行开始的值
# for i in range(1,sheet1.nrows):
#    list.append(dict(zip(keys,sheet1.row_values(i))))
#
# print(list)







































