import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from market.models import Product




class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'Product': Product.objects.all(),
        }
        return context




class FaqView(TemplateView):
    template_name = 'faq.html'


class Error404View(TemplateView):
    template_name = '404.html'


class FavoritesView(TemplateView):
    template_name = 'favorites.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class ProductListView(TemplateView):
    template_name = 'product-list.html'


    def get_context_data(self, **kwargs):
        context = {
            'product_list': Product.objects.all(),
            'now': datetime.datetime.now().date(),

        }

        return context




class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'



