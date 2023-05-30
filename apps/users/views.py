from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from apps.settings.models import Setting
from apps.users.models import User

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create(username=email, email=email)
        user.set_password(password)
        user.save()
        return redirect('index')
    return render(request, 'users/register.html', locals())
