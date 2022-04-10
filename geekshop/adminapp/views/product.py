from turtle import title
from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from adminapp.utils import superuser_requared


@superuser_requared
def product_create(request):
    pass


@superuser_requared
def products(request, pk):
    title = 'Продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category).order_by('id')

    return render(request, 'adminapp/product/products.html', context={
        'title': title,
        'objects': products,
        'category': category,

    })


@superuser_requared
def product_read(request):
    pass


@superuser_requared
def product_update(request):
    pass


@superuser_requared
def product_delete(request):
    pass
