import unittest,requests
from lib.db import *

name='student'
noname='petr'


class MyTestCase(unittest.TestCase):
    url="http://127.0.0.1:8000/api/student/user/register"
    def test_reg_ok(self):
        if cherk_user(name=name):
            del_user(noname)
        data={"userName":noname,"password":"123456","userLevel":1}
        r=requests.post(url=self.url,json=data)
        resu={"code":1,"message":"成功","response":None}
        self.assertDictEqual(r.json(),resu)
        self.assertTrue(cherk_user(noname))
        del_user(noname)

    def test_reg_err(self):
        if not cherk_user(name):
            add_user(name,"123")
        data={"userName":name,"password":"123456","userLevel":1}
        r=requests.post(url=self.url,json=data)
        rssu={"code":2,"message":"用户已存在","response":None}
        self.assertDictEqual(r.json(), rssu)


# import json
# import unittest,requests
# from read_excel import *
# from db import *
#
#
# class MyTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.li =read_excel().excel_to_list("test_user_data.xlsx",'test_user_reg')
#     def test_reg_ok(self):
#         case_data =read_excel().get_test_data(self.li,'reg_ok')
#         # case_data['url']
#         url = case_data.get('url')  # 从字典中取数据,excel中的标题也必须是小写url
#         args = case_data.get('args')  # 字符串格式,需要用json.loads(str)转为字典格式
#         expect_res = case_data.get('expect_res')  # 期望数据
#         a = json.loads(args).get("userName")
#         if check_user(name=a):
#             # 如果已经注册过了 就删除
#             del_user(a)
#         res = requests.post(url=url, json=json.loads(args))  # 表单请求,数据转为字典格式
#         self.assertIn(expect_res, res.text)  # 改为assertIn断言
#         del_user(a)
#     def test_reg_err(self):
#         case_data = read_excel().get_test_data(self.li, 'reg_err')
#         # case_data['url']
#         url = case_data.get('url')  # 从字典中取数据,excel中的标题也必须是小写url
#         args = case_data.get('args')  # 字符串格式,需要用json.loads(str)转为字典格式
#         expect_res = case_data.get('expect_res')  # 期望数据
#         res = requests.post(url=url, json=json.loads(args))  # 表单请求,数据转为字典格式
#         self.assertIn(expect_res, res.text)  # 改为assertIn断言
#
#
# if __name__ == '__main__':
#     unittest.main()























if __name__ == '__main__':
    unittest.main()
