import json
from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product

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


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    return render(request, 'mainapp/products.html', context={
        'title': 'продукты',
        'products': products,
        'menu_links': MENU_LINKS,
        'categories': categories,
    })


def category(request, pk):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'mainapp/products.html', context={
        'title': 'продукты',
        'products': products,
        'menu_links': MENU_LINKS,
        'categories': categories,
    })


def contact(request):

    return render(request, 'mainapp/contact.html', context={
        'title': 'контакты',
        'menu_links': MENU_LINKS,
    })
