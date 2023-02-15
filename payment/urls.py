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
