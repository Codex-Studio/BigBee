from django.urls import path 

from apps.users.views import register, user_login, user_account


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('user/<int:id>/', user_account, name='user_account'),
]