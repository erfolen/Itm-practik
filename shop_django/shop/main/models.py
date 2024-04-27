from django.db import models
from .utils import ContentMixin


class Categories(ContentMixin, models.Model):
    parent_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Manufactures(ContentMixin, models.Model):

    class Meta:
        db_table = 'manufacture'
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Products(ContentMixin, models.Model):
    article = models.CharField(max_length=100, verbose_name='Артикул')
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Скидка в процентах')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name = 'Категория')
    manufacture = models.ForeignKey(to=Manufactures, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True,
                                    verbose_name='Производитель')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
