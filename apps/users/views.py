# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm
from tools import email_send
# Create your views here.
# 重载用户认证,默认只能用用户名和密码登录
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 逗号代表and
            # user = UserProfile.objects.get(Q(username=username)|Q(email=username),Q(password=password))
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form":register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email","")
            pass_word = request.POST.get("password","")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(password=pass_word)
            user_profile.is_active = False
            user_profile.save()

            email_send.send_register_email(user_name, "register")
            return render(request, 'login.html')
        else:
            return render(request, 'register.html' ,{"register_form":register_form})

class LoginView(View):
    def get(self, request):
        login_form = LoginForm(request.POST)
        return render(request, "login.html", {"login_form":login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", '')
            pass_word = request.POST.get("password", '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user = UserProfile.objects.get(username=user_name)
                    return render(request, 'base.html', {"user":{'id':user.id,'username':user.username}})
                else:
                    return render(request, "login.html", {"err_msg": "用户名未激活"})
            else:
                return render(request, "login.html", {"err_msg": "用户名或密码错误!"})
        else:
            print (login_form.errors)
            return render(request, "login.html", {"login_form":login_form,"err_msg":login_form.errors})

@login_required(login_url='login')
def index(request):
    return render(request, 'base.html')