import json
from django.shortcuts import render

# Create your views here.

MENU_LINKS = [
    {'url': 'index', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]


def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'главная',
        'menu_links': MENU_LINKS,

    })


def products(request):
    with open('./menu_product.json', 'r') as file:
        menu_product = json.load(file)
    return render(request, 'mainapp/products.html', context={
        'title': 'продукты',
        'menu_links': MENU_LINKS,
        'menu_product': menu_product,
    })


def contact(request):

    return render(request, 'mainapp/contact.html', context={
        'title': 'контакты',
        'menu_links': MENU_LINKS,
    })
