from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.urls import reverse

from .models import User, Administrator
import datetime, random, string

# Create your views here.

# def index_main(request):
#     lists = places.objects.all()
#     dict = {
#         "lists": lists,
#     }
#     return render(request,'main.html',context=dict)

import hashlib

def get_md5(sourcedata,random_code):
    obj = hashlib.md5()
    obj.update(sourcedata.encode('utf-8'))
    obj.update(random_code.encode('utf-8'))
    pwd = obj.hexdigest()
    return pwd


#登陆
def index_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        tag = request.POST.get('tag')
        if tag == 1: # 管理员
            user = Administrator.objects.filter(username=username)
        elif tag == 2: # 用户
            user = User.objects.filter(username=username)
        else:
            return render(request, 'login.html')
        if user.exists():
            md5_pwd = get_md5(password, user.random_code)
            if user.password == md5_pwd:
                if tag == 1:  # 管理员
                    return redirect(reverse('app:administrator_main'))
                else:
                    return redirect(reverse('app:main'))
            else:
                messages.error(request, "用户名或密码不正确！")
                return redirect(reverse('app:login'))

        else:
            messages.error(request, "用户名或密码不正确！")
            return redirect(reverse('app:login'))

#用户注册
def index_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        real_name = request.POST.get('real_name')
        tel = request.POST.get('tel')
        is_user = User.objects.filter(username=username)
        is_tel = User.objects.filter(tel=tel)

        if is_user.exists():
            messages.error(request, "用户名已存在！")
            return redirect(reverse('app:register'))

        if is_tel.exists():
            messages.error(request, "手机号已注册！")
            return redirect(reverse('app:register'))

        if username.strip() == '':
            messages.error(request, "用户名不可为空！")
            return redirect(reverse('app:register'))

        if password.strip() == '':
            messages.error(request, "密码不可为空！")
            return redirect(reverse('app:register'))


        if isinstance(tel, int) and len(tel)==11:
            # 随机生成字符串
            random_code = "".join([
                random.choice(string.ascii_letters)
                if random.randint(0, 1) else random.choice(string.digits)
                for i in range(10)
            ])

            user = User()
            user.username = username
            user.password = get_md5(password, random_code)
            user.tel = tel
            user.real_name = real_name
            user.random_code = random_code
            user.create_time = datetime.datetime.now()
            user.update_time = datetime.datetime.now()
            user.save()
            messages.error(request, "注册成功！")
            return redirect(reverse('app:login'))

        messages.error(request, "手机号不正确！")
        return redirect(reverse('app:register'))


#用户修改密码
def edit_pwd(request):
    if request.method == 'GET':
        return render(request, '修改密码.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        if new_password.strip() == '':
            messages.error(request, "新密码不可为空！")
            return redirect(reverse('app:register'))

        user = User.objects.filter(username=username)
        md5_pwd = get_md5(password, user.random_code)

        if user.password == md5_pwd:
            # 随机生成字符串
            random_code = "".join([
                random.choice(string.ascii_letters) if random.randint(
                    0, 1) else random.choice(string.digits)
                for i in range(10)
            ])

            user.password = get_md5(new_password, random_code)
            user.random_code = random_code
            user.update_time = datetime.datetime.now()
            user.save()

            messages.error(request, "密码修改成功，请重新登录！")
            return redirect(reverse('app:login'))

        messages.error(request, "旧密码错误！")
        return redirect(reverse('app:修改密码页'))


#管理员新增用户
def add_user(request):
    if request.method == 'GET':
        return render(request, '用户管理页.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        real_name = request.POST.get('real_name')
        tel = request.POST.get('tel')
        is_user = User.objects.filter(username=username)
        is_tel = User.objects.filter(tel=tel)

        if is_user.exists():
            messages.error(request, "用户名已存在！")
            return redirect(reverse('app:register'))

        if is_tel.exists():
            messages.error(request, "手机号已注册！")
            return redirect(reverse('app:register'))

        if username.strip() == '':
            messages.error(request, "用户名不可为空！")
            return redirect(reverse('app:register'))

        if password.strip() == '':
            messages.error(request, "密码不可为空！")
            return redirect(reverse('app:register'))


        if isinstance(tel, int) and len(tel)==11:
            # 随机生成字符串
            random_code = "".join([
                random.choice(string.ascii_letters)
                if random.randint(0, 1) else random.choice(string.digits)
                for i in range(10)
            ])

            user = User()
            user.username = username
            user.password = get_md5(password, random_code)
            user.tel = tel
            user.real_name = real_name
            user.random_code = random_code
            user.create_time = datetime.datetime.now()
            user.update_time = datetime.datetime.now()
            user.save()
            messages.error(request, "添加成功！")
            return redirect(reverse('app:用户管理页'))

        messages.error(request, "手机号不正确！")
        return redirect(reverse('app:register'))


# 删除用户
def delete(request):
    username = request.POST.get('username')
    user = Administrator.objects.filter(username=username)
    if user:
        user.delete()
        messages.error(request, "用户删除成功！")
        return redirect(reverse('app:用户管理页'))

    messages.error(request, "用户不存在")
    return redirect(reverse('app:用户管理页'))


# 重置密码
def resetpassword(request):
    username = request.POST.get('username')
    new_password = request.POST.get('new_password')

    if new_password.strip() == '':
        messages.error(request, "新密码不可为空！")
        return redirect(reverse('app:register'))

    user = Administrator.objects.filter(username=username)
    if user:
        # 随机生成字符串
        random_code = "".join([
            random.choice(string.ascii_letters) if random.randint(
                0, 1) else random.choice(string.digits)
            for i in range(10)
        ])

        user.password = get_md5(new_password, random_code)
        user.random_code = random_code
        user.update_time = datetime.datetime.now()
        user.save()

        messages.error(request, "密码重置成功！")
        return redirect(reverse('app:重置密码页'))

    messages.error(request, "用户不存在")
    return redirect(reverse('app:用户管理页'))


#修改基本信息
def edit_info(request):
    username = request.POST.get('username')

    new_tel = request.POST.get('tel')
    new_real_name = request.POST.get('real_name')

    tag = request.POST.get('tag')

    if tag == 1:  # 管理员
        user = Administrator.objects.filter(username=username)
        is_tel = Administrator.objects.filter(tel=new_tel)
    elif tag == 2:  # 用户
        user = User.objects.filter(username=username)
        is_tel = User.objects.filter(tel=new_tel)
    else:
        return render(request, '用户管理页.html')

    if is_tel.exists():
        messages.error(request, "手机号已注册！")
        return redirect(reverse('app:修改信息页'))

    if isinstance(new_tel, int) and len(new_tel) == 11:
        user.tel = new_tel
        user.real_name = new_real_name
        user.update_time = datetime.datetime.now()
        user.save()

        messages.error(request, "修改成功！")
        return redirect(reverse('app:修改信息页'))



#
# def index_list(request):
#     lists = places.objects.all()
#     dict = {
#         "lists":lists,
#     }
#
#     return render(request,"lists.html",context=dict)
#
#
# def index_left(request):
#     lists = places.objects.all()
#     dict = {
#         "lists": lists,
#     }
#     return render(request,"left.html",context=dict)
#
#
# def index_map(request):
#     lists = places.objects.all()
#     dict = {
#         "lists": lists,
#     }
#     return render(request,"map.html",context=dict)