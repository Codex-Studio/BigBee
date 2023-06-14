from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from apps.settings.models import Setting
from apps.users.models import User, Partnership
from apps.products.models import Product

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
    user = User.objects.get(id=id)
    setting = Setting.objects.latest('id')
    user_products = Product.objects.filter(user=request.user)
    partners = Partnership.objects.filter(status=False)
    if request.method == "POST":
        if 'update' in request.POST:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            user = User.objects.get(id = id)
            user.username = username 
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone = phone 
            user.address = address 
            user.save()
            return redirect('user_account', user.id)
        if 'create' in request.POST:
            title = request.POST.get('title')
            description = request.POST.get('description')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            product = Product.objects.create(user=request.user, title=title, description=description, price=int(price), image=image)
            return redirect('product_detail', product.id)
        if 'partnership' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            partnership = Partnership.objects.create(user=request.user, name=name, email=email, phone=phone)
            return redirect('partnership')
    return render(request, 'users/account.html', locals())

def partnership(request):
    setting = Setting.objects.latest('id')
    partners = Partnership.objects.filter(status=False)
    return render(request, 'redirect/partnership.html', locals())