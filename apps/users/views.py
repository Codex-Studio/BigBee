from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from apps.settings.models import Setting
from apps.users.models import User

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        user = authenticate(username = username, password = password)
        login(request, user)
        user = User.objects.get(username=username)
        return redirect('user_account', user.id)
        # return redirect('index')
    return render(request, 'users/register.html', locals())

def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        user = User.objects.get(username=username)
        return redirect('user_account', user.id)
    return render(request, 'users/login.html', locals())

def user_account(request, id):
    setting = Setting.objects.latest('id')
    return render(request, 'users/account.html', locals())