import json
from turtle import title
from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product

# Create your views here.

MENU_LINKS = [
    {'url': 'index', 'name': 'домой'},
    {'url': 'products:main', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]


def index(request):
    title = 'Главная'
    products_site = Product.objects.all()
    return render(request, 'mainapp/index.html', context={
        'title': title,
        'menu_links': MENU_LINKS,
        'products_site': products_site,

    })


def products(request, pk=None):
    print(pk)

    if pk is not None:
        if pk == 0:
            products_site = Product.objects.all()
            category = ProductCategory.objects.all()
        else:
            category = ProductCategory(pk=pk)
            products_site = Product.objects.filter(category=category)

            return render(request, 'mainapp/products_list.html', context={
                'title': 'продукты',
                'menu_links': MENU_LINKS,
                'category': category,
                'products_site': products_site,
            },
            )

    category = ProductCategory.objects.all()
    products_site = Product.objects.all()

    return render(request, 'mainapp/products.html', context={
        'title': 'продукты',
        'menu_links': MENU_LINKS,
        'category': category,
        'products_site': products_site,
    },
    )


def contact(request):

    return render(request, 'mainapp/contact.html', context={
        'title': 'контакты',
        'menu_links': MENU_LINKS,
    })


def category(request, pk=None):
    print(pk)
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category=category)

            return render(request, 'mainapp/products.html', context={
                'title': title,
                'links_menu': links_menu,
                'category': category,
                'products': products,
            })
    '''same_products = Product.objects.all()[3:5]

    return render(request, 'mainapp/products.html', context={
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    })'''
