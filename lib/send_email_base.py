# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/27 15:15
# Author        : smart
# @File         :send_email_base.py
# @Software     :PyCharm
import smtplib
from  email.mime.text import MIMEText
# 发邮件
msg=MIMEText('邮件内容','plain','utf-8')
# 发件人
msg['From']='2180444756@qq.com'
# 收件人
msg['To']='2180444756@qq.com'
# 邮件主题
msg['Subject']="测试报告主题"
# 创建一个smtp的链接
smtp=smtplib.SMTP_SSL('smtp.qq.com')
# 登录发件箱
smtp.login('2180444756@qq.com','cczokyfqgyyydigi')
# 发送邮件
smtp.sendmail('2180444756@qq.com','2180444756@qq.com',msg.as_string())
# 退出 断开
smtp.quit()






