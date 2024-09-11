from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from market.models import Product



class Page404View(TemplateView):
    template_name = '404.html'




class PageFagView(TemplateView):
    template_name = 'fag.html'




class PageFavoritesView(TemplateView):
    template_name = 'favorites.html'




class PageHomeView(TemplateView):
    template_name = 'index.html'




class ProductListView(TemplateView):
    template_name = 'product-list.html'




class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'




class ShopingCartView(TemplateView):
    template_name = 'shopping-cart.html'






