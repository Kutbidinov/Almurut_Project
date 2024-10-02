import datetime

from django.http import Http404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from market.models import Product, ProductUserRating


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'Product': Product.objects.all(),
        }
        return context





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

        user = self.request.user

        # вычисляем поставленный пользователем рейтинг
        try:
            my_product_rating = ProductUserRating.objects.get(product=product, users=user)
            rating = my_product_rating.rating
        except ProductUserRating.DoesNotExist:
            rating = 0

        # вычисляем средний рейтинг
        product_rating_list = ProductUserRating.objects.filter(product=product)
        total_value = 0
        for product_rating in product_rating_list:
            total_value += product_rating.rating
        if len(product_rating_list) == 0:
            average_rating = 0
        else:
            average_rating = total_value / len(product_rating_list)
        # альтернативный способ (*сделать и если что извиниться)
        # try:
        #     average_rating = total_value / len(product_rating_list)
        # except ZeroDivisionError:
        #     average_rating = 0

        product_category = product.category
        category_other_product_list = (
            Product.objects
            .filter(category=product_category)
            .exclude(id=product.id)
        )

        context = {
            'product': product,
            'rating': rating,
            'average_rating': average_rating,
            'other_products': category_other_product_list,
            'now': datetime.datetime.now().date(),
            'other_products_len': len(category_other_product_list)
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



class ShopView(TemplateView):
    template_name = 'shopping-cart.html'


class FaqView(TemplateView):
    template_name = 'faq.html'


class FavoritesView(TemplateView):
    template_name = 'favorites.html'
