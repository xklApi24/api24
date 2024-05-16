# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/26 11:45
# Author        : smart
# @File         :emilbd.py
# @Software     :PyCharm
# smtplib 用于邮件的发信动作
import logging
import smtplib
from  email.mime.text import MIMEText
# 发带附件的邮件
from email.mime.multipart import MIMEMultipart
# 用于使用中文邮件主题
from email.header import Header
from config.config import *
def send_email(report_file):
    with open(report_file,encoding='utf-8') as f:
        email_body=f.read()
    # 发邮件
    msg=MIMEMultipart()
    msg.attach(MIMEText(email_body,'html','utf-8'))
    # 发件人
    msg['From']=sender
    # 收件人
    msg['To']=receiver
    # 邮件主题
    msg['Subject']=Header(subject,"utf-8")
    # 添加附件
    att1=MIMEText(
        open(report_file,'rb').read(),'base64','utf-8'
    )
    att1["Content-Type"]='application/octet-stream'
    att1["Content-Disposition"]='attachment;filename="report.html"'
    msg.attach(att1)

    try:
    # 创建一个smtp的链接
        smtp=smtplib.SMTP_SSL(smtp_server)
        # 登录发件箱
        smtp.login(smtp_user,smtp_ps)
        # 发送邮件
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.debug("邮件发送成功")
    except Exception as e:
        logging.error(str(e))
    # 退出 断开
    finally:
        smtp.quit()
if __name__ == '__main__':
    send_email('../report/report.html')














