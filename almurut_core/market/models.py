from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProductCategory(models.Model):
    """Продукт для категории товара!    """
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = "Категория Товаров"
        verbose_name = "Категория Товара"

    def __str__(self):
        return self.name    


class Product(models.Model):
    """Модель Товаров!"""

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField(help_text="В сомах", verbose_name='Цена без скидки')
    sales_percent = models.PositiveSmallIntegerField(verbose_name="Само скидка",
                                                     null=True,
                                                     blank=True,
                                                     validators=[MaxValueValidator(100)])





    description = models.TextField()
    preview_image = models.ImageField(upload_to='products/preview_')

    new_expiry_date = models.DateField()


    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"

    def get_price_with_sales(self):
        """Возвращает цену с учётом скидки"""

        if self.sales_percent == 0:
            return self.price
        else:
            return int((self.price / 100) * (100 - self.sales_percent))

    def __str__(self):
        return self.name




class ProductGallery(models.Model):
    """Модель для Галереий"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='image_products')

    class Meta:
        verbose_name_plural = 'Товары с Изображениями'
        verbose_name = 'Товар с Изображениям'


class User(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    birth_date = models.DateField()











class ProductUserRating(models.Model):
    """Модель чтобы зафиксировать, что пользовател поставил оценку для товара!"""
    from users.models import CustomUser

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('users', 'product')









