from django.shortcuts import render

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from market.models import Product


class Custom404View(TemplateView):
    template_name = '404.html'



class FaqView(TemplateView):
    template_name = 'faq.html'



class FavoritesView(TemplateView):
    template_name = 'favorites.html'



class HomeView(TemplateView):
    template_name = 'index.html'



class LoginView(TemplateView):
    template_name = 'login.html'



class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'



class ProductListView(TemplateView):
    template_name = 'product-list.html'
    # def get_context_data(self, **kwargs):
    #     product = Product.objects.all()
    #     paginator = Paginator(product, 10)
    #     page_number = self.request.GET.get('page', 1)
    #     page_obj = paginator.get_page(page_number)
    #
    #     context = {
    #         'page_obj': page_obj
    #     }
    #     return context







class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'