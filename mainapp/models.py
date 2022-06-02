from unicodedata import name
from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def active_items(self):
        return Product.objects.filter(is_active=True)

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    price = models.DecimalField(
        verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    color = models.IntegerField(verbose_name='цвет', default=0x000000)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(verbose_name="активный", default=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
