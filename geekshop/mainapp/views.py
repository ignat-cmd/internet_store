import json
from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.

MENU_LINKS = [
    {'url': 'index', 'name': 'домой'},
    {'url': 'products:main', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]


def index(request):
    products_site = Product.objects.all()
    return render(request, 'mainapp/index.html', context={
        'title': 'главная',
        'menu_links': MENU_LINKS,
        'products_site': products_site,

    })


def products(request, pk=None):
    print(pk)
    category = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context={
        'title': 'продукты',
        'menu_links': MENU_LINKS,
        'category': category[:4],
    })


def contact(request):

    return render(request, 'mainapp/contact.html', context={
        'title': 'контакты',
        'menu_links': MENU_LINKS,
    })
