"""
URL configuration for almurut_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from market.views import ProductListView, ProductDetailView, \
    SendProductFeedbackView, HomeView, ShopView, FaqView, FavoritesView

from users.views import UserRegistrationView, UserMakeRegistrationView, \
    LoginPageView, UserMakeLoginView, UserMakeLogoutView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='Home-url'),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail-url'),

    path('products/<int:pk>/send-feedback/', SendProductFeedbackView.as_view(), name='send-feedback-url'),

    path('registration/', UserRegistrationView.as_view(), name='registration-url'),
    path('login/', LoginPageView.as_view()),
    path('make-login/', UserMakeLoginView.as_view(), name='make-login-url'),

    path('make-logout', UserMakeLogoutView.as_view(), name='make-logout-url'),

    path('make-registration/', UserMakeRegistrationView.as_view(), name='make-registration-url'),
    path('shop/', ShopView.as_view(), name='Shop-url'),
    path('fag-page/', FaqView.as_view(), name='Faq-url'),
    path('favorites/', FavoritesView.as_view(), name='favorites-url'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)