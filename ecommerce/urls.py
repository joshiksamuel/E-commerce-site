"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from esite import views
from esite.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ,name='index'),
    path('product',views.product ,name='product'),
    path('about',views.about ,name='about'),
    path('contact',views.contact ,name='contact'),
    path('account',views.account ,name='account'),
    path('signup',views.signup ,name='signup'),
    path('login',views.login ,name='login'),
    path('logout',views.logoutpage,name='logout'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('buynow',views.buynow ,name='buynow'),
    path('checkout',views.checkout,name='checkout'),
    path('order/<int:product_id>/',views.order_item,name='order_item'),
    path('product/<int:product_id>/', views.productdetails, name='productdetails'),
    path('increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart',views.cart,name='cart')

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
