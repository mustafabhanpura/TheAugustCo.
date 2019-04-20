from django.contrib import admin
from django.urls import path, include
from . import views
app_name='cart'
urlpatterns = [
   path('search/',views.search,name='search'),
   path('search/<int:product_id>',views.detail,name='detail'),
   path('search/cart/',views.cart,name='add_cart'),
   path('search/cart/<int:order_id>',views.det,name='add'),
   path('search/cart/delete/<int:order_id>',views.delete,name='delete'),
   path('search/cart/form',views.form,name='form'),
]