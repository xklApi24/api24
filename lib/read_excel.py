# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/23 16:21
# Author        : smart
# @File         :read_excel.py
# @Software     :PyCharm
import xlrd
class read_excel():
    def excel_to_list(self,filename,sheetname):
        # 打开excel文件
        wb=xlrd.open_workbook(filename)
        # 打开工作簿
        sh=wb.sheet_by_name(sheetname)
        # 创建一个空白列表
        list=[]
        # 根据第一行 获取key值
        keys=sh.row_values(0)
        for i in range(1,sh.nrows):
            v=sh.row_values(i)
            list.append(dict(zip(keys,v)))
        return list

    # 从全部用例数据中读取指定的用例数据
    def get_test_data(self,data_list,case_name):
        for case_data in data_list:
            # 如果字典数据中case_name与参数一致
            if case_name ==case_data['case_name']:
                # 如果查询不到会返回None
                return case_data
if __name__ == '__main__':
    r=read_excel()
    l=r.excel_to_list("user_data.xlsx",'test_user_login')
    print(l)
    print(r.get_test_data(l, 'login_ok'))













