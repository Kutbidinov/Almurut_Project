import datetime

from django.http import Http404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from market.models import Product, ProductUserRating


class HomeView(TemplateView):
    template_name = 'index.html'






class ProductListView(TemplateView):
    template_name = 'product-list.html'

    def get_context_data(self, **kwargs):
        context = {
            'product_list': Product.objects.all(),
            'now': datetime.datetime.now().date()
        }
        return context



class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['pk'])
        except Product.DoesNotExist:
            raise Http404

        context = {
            'product': product
        }
        return context


class SendProductFeedbackView(View):
    """Вью для сохранения отзыва пользователя для конкретного товара"""

    def post(self, request, *args, **kwargs):
        data = request.POST
        rating_value = data['rating_value']

        product = Product.objects.get(id=kwargs['pk'])
        user = request.user
        if user.is_authenticated:
            ProductUserRating.objects.create(
                rating=rating_value,
                product=product,
                user=user,
            )
            return redirect(f'products/{product.id}/')
        else:
            return redirect('/login/')