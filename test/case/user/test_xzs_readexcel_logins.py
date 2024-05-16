import json, unittest,requests,ddt
from lib import read_excel
from lib.case_log import logs
import os,sys
from config.config import *
def read():
    r=read_excel.read_excel()
    l=r.excel_to_list(data_file,"TestUserLogin")
    t=[]
    for i in range(len(l)):
        t.append(l[i]["case_name"])
    return t

@ddt.ddt()
class MyTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) :
    #    cls.r=read_excel.read_excel()
    #    cls.l=cls.r.excel_to_list("user_data.xlsx","test_user_login")
    @ddt.data(*read())
    def test_login(self,name):
            r = read_excel.read_excel()
            l = r.excel_to_list(data_file, "TestUserLogin")
            t=r.get_test_data(l,name)
            url=t.get("url")
            args=t.get("args")
            exp=t.get("expect_res")
            data=json.loads(args)
            r=requests.post(url,json=data)
            logs(name,url,args,exp,r.text)
            self.assertIn(exp,r.text)
    # @classmethod
    # def setUpClass(cls):
    #     cls.li=read_excel().excel_to_list("./dome案例/user_data.xlsx",'test_user_login')
    # def test_reg_ok(self):
    #     case_data=read_excel().get_test_data(self.li,'login_ok')
    #     url=case_data.get('url')
    #     args=case_data.get('args')
    #     expect_res=case_data.get('expect_res')
    #     # a = json.loads(args).get("userName")
    #     # if cherk_user(name=a):
    #     #          del_user(a)
    #     res=requests.post(url=url,json=json.loads(args))
    #     self.assertIn(expect_res,res.text)
    #     # del_user(a)
    #
    # def test_reg_err1(self):
    #     case_data=read_excel().get_test_data(self.li,'login_err1')
    #     url=case_data.get('url')
    #     args=case_data.get('args')
    #     expect_res=case_data.get('expect_res')
    #     res=requests.post(url=url,json=json.loads(args))
    #     self.assertIn(expect_res,res.text)
    #
    # def test_reg_err2(self):
    #     case_data=read_excel().get_test_data(self.li,'login_err2')
    #     url=case_data.get('url')
    #     args=case_data.get('args')
    #     expect_res=case_data.get('expect_res')
    #     res=requests.post(url=url,json=json.loads(args))
    #     self.assertIn(expect_res,res.text)
    #
    # def test_reg_err3(self):
    #     case_data=read_excel().get_test_data(self.li,'login_err3')
    #     url=case_data.get('url')
    #     args=case_data.get('args')
    #     expect_res=case_data.get('expect_res')
    #     res=requests.post(url=url,json=json.loads(args))
    #     self.assertIn(expect_res,res.text)
if __name__ == '__main__':
    unittest.main()
