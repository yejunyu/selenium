#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-7-27}

from random import Random

from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from adClick.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    rcode = random_str(16)
    email_record.code = rcode
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下边的连接激活您的账号: http://127.0.0.1:8000/active/{0}".format(rcode)

        send_status = send_mail(email_title,email_body, EMAIL_FROM,[email])
        if send_status:
            pass