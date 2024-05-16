import unittest,requests,json,os,sys,ast
from config.config import *
from lib.read_excel import *
from lib.case_log import logs
sys.path.append("../..")

class BaseCase(unittest.TestCase):
    r=read_excel()
    @classmethod
    def setUpClass(cls):
        if cls.__name__!="BaseCase":
            cls.data_list=cls.r.excel_to_list(data_file,cls.__name__)
    def get_case_data(self,case_name):
        return self.r.get_test_data(self.data_list,case_name)
    def send_request(self,case_data):
        case_name=case_data.get('case_name')
        url=case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')
        if method.upper()=='GET':
            res=requests.get(url=url,params=json.loads(args))

        elif data_type.upper()=='FORM':
            headers=json.loads(headers)
            res=requests.post(url=url,json=json.loads(args),headers=headers)
            logs(case_name,url,args,expect_res,res.text)
            self.assertIn(expect_res,res.text)
        elif data_type.upper()=='JSON':
            res=requests.post(url=url,json=json.loads(args),headers=headers)
            logs(case_name,url,args,expect_res,res.json())
            self.assertIn(expect_res,res.text)




