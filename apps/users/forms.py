#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-7-20}

from django import forms
from captcha.fields import CaptchaField


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=6)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class LoginForm(forms.Form):
    username = forms.CharField(label=u'用户名', required=True)
    password = forms.CharField(label=u'密码', required=True, min_length=8)
    captcha = CaptchaField(label=u'验证码', error_messages={"invalid": u"验证码错误"})
