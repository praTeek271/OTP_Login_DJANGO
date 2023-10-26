from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('' , include('accounts.urls')),
    path('home' , include('cart.urls')),
    path('a+d+m+i+n/', admin.site.urls),
]
