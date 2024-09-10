"""
URL configuration for almurut_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from market.views import (HomeView, Custom404View, FaqView,
                          FavoritesView, LoginView, ProductDetailView,
                          ProductListView,  ShoppingCartView,)


from users.views import (UserRegisterView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('404_error/', Custom404View.as_view(), name = '404_error'),
    path('faq_page/', FaqView.as_view(), name = 'faq_page'),
    path('favorites/', FavoritesView.as_view(), name = 'favorites_list'),
    path('home/', HomeView.as_view(), name = 'home'),
    path('login_page/', LoginView.as_view(), name = 'login_page'),
    path('product_detail/', ProductDetailView.as_view(), name = 'product_detail_list'),
    path('product_list/', ProductListView.as_view(), name = 'product_list'),
    path('register_page/', UserRegisterView.as_view(), name = 'register_page'),
    path('shopping_cart/', ShoppingCartView.as_view(), name = 'shopping_cart_list' ),
    path('make-registration')
]