"""payment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from transition import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('buy_order/<int:order_pk>', views.buy_order, name='buy_order'),
    path('buy/<int:item_pk>', views.buy, name='buy'),
    path('item/<int:item_pk>/', views.item, name='item'),
    path('create_order', views.create_order, name='create_order'),
    path('order/<int:order_pk>/', views.get_order, name='get_order'),
]
