# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/3/22 9:58
# Author        : smart
# @File         :run_all.py
# @Software     :PyCharm
import time,pickle,sys
import unittest,logging
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suits import get_suit

def discover():
    return unittest.defaultTestLoader.discover(test_case_path,'test*.py')

def run(suite):
    logging.info("===============开始测试=====================")
    with open(report_file,'wb') as f:
        result= HTMLTestRunner(
                stream=f,  # 相当于f.write(报告)
                title='接口测试报告',
                description='接口登录和注册测试报告',
                verbosity=2  # 为每个测试用例生成测试报告
            ).run(suite)
        if result.failures:
            save_failures(result,last_fails_file)
    logging.info("===============测试结束=====================")
    if sender_email_enable:
        send_email(report_file)
        logging.info("***************发送邮件**********************")



def run_suite(suite_name):
     suite=get_suit(suite_name)
     if isinstance(suite,unittest.TestSuite):
         run(suite)
     else:
         print("TestSuite不存在")

def run_all():
    run(discover())



def collect():
    suite=unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() !=0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
    return suite

def collect_only():
    t0=time.time()
    i = 0
    for case in collect():
        i+=1
        print("{}.{}".format(str(i),case.id()))
    print("-------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time() - t0))

def make_suit_list(list_file):
    with open(list_file,'r')as f:
        suit_list=f.readlines()
    suit_list=[x.strip() for x in suit_list if not x.startswith("#")]
    suit=unittest.TestSuite()
    all_suit=collect()
    for case in all_suit:
        if case.id().split(".")[-1] in suit_list:
            suit.addTest(case)
    return suit



def makesuit_by_tag(tag):
    suit=unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:
            suit.addTest(case)
    return  suit



def save_failures(result,file):
    suite=unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])
    with open(file,'wb')as f:
        pickle.dump(suite,f)



def rerun_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb')as f:
        suite=pickle.load(f)
    return (suite)

def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.tag:
        run(makesuit_by_tag(options.tag))
    else:
        run_all()


if __name__ == '__main__':
    run_all()
    # run_suite("smoke_suit")
    # collect_only()
    # suit=make_suit_list(testlist_file)
    # run(suit)
    # suit=makesuit_by_tag("level1")
    # run(suit)
    # rerun_fails()
    # main()



































































































# if __name__ == '__main__':
#     # now=time.strftime("%Y_%m_%d_%H_%M_%S")
#     logging.info("============run_all开始测试================")
#     fe=open(report_file,'wb')
#     runner=HTMLTestRunner(
#         stream=fe,  # 相当于f.write(报告)
#         title='xzs测试报告',
#         description='xzs登录和注册测试报告',
#         verbosity=2  # 为每个测试用例生成测试报告
#     )
#     suit=unittest.defaultTestLoader.discover(prj_path,'test*.py')
#     runner.run(suit)
#     fe.close()
#     send_email(report_file)
#     logging.info("============run_all测试结束================")




