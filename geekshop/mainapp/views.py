import json
from queue import Empty
from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

MENU_LINKS = [
    {'url': 'index', 'active': ['index'], 'name': 'домой'},
    {'url': 'products:main', 'active': [
        'products:main', 'products:category'], 'name': 'продукты'},
    {'url': 'contact', 'active': ['contact'], 'name': 'контакты'},
]


def index(request):
    products = Product.objects.all()
    return render(request, 'mainapp/index.html', context={
        'title': 'главная',
        'menu_links': MENU_LINKS,
        'products': products,

    })


def get_hot_product(queryset):
    return random.choice(queryset)


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    hot_product = get_hot_product(products)
    return render(request, 'mainapp/products.html', context={
        'title': 'продукты',
        'products': products.exclude(pk=hot_product.pk)[:4],
        'hot_product': hot_product,
        'menu_links': MENU_LINKS,
        'categories': categories,
    })


def category(request, category_id, page=1):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, id=category_id)
    products = Product.objects.filter(category=category)
    hot_product = get_hot_product(products)

    # Определяем обьект paginator и передаем внутрь QwerySet и количество выводимых объектов
    paginator = Paginator(products.exclude(pk=hot_product.pk), 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    return render(request, 'mainapp/products.html', context={
        'title': 'продукты',
        'hot_product': get_hot_product(products),
        'products': products_paginator,
        'category': category,
        'menu_links': MENU_LINKS,
        'categories': categories,
    })


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = ProductCategory.objects.all()
    return render(request, 'mainapp/product.html', context={
        'title': 'продукты',
        'product': product,
        'menu_links': MENU_LINKS,
        'categories': categories,
    })


def contact(request):

    return render(request, 'mainapp/contact.html', context={
        'title': 'контакты',
        'menu_links': MENU_LINKS,
    })
