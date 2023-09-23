from django.urls import path 

from apps.settings.views import index, about, search


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
]