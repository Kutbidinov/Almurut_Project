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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from market.views import Page404View, PageFagView, PageFavoritesView, PageHomeView, ProductListView,\
    ProductDetailView, ShopingCartView

from users.views import UserRegisterView, LoginView, UserMakeRegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('404_error/', Page404View.as_view(), name='page_404_url'),
    path('page_fag/', PageFagView.as_view(), name='fag_page)url'),
    path('favoriets_page/', PageFavoritesView.as_view(), name='favoriets_url'),
    path('home/', PageHomeView.as_view(), name='home_url'),
    path('Login_page/', LoginView.as_view(), name='login_url'),
    path('produts/', ProductListView.as_view(), name='products_url'),
    path('products_detail/', ProductDetailView.as_view(), name='detail_url'),
    path('register/', UserRegisterView.as_view(), name='register_url'),
    path('user_registration/', UserMakeRegistrationView.as_view(), name='make_registration_url'),
    path('shoping_page/', ShopingCartView.as_view(), name='shoping_url'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)