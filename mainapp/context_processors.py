def menu_links(request):
    return {
        'menu_links': [
            {'url': 'index', 'active': ['index'], 'name': 'домой'},
            {'url': 'products:main', 'active': ['products:main', 'products:category'], 'name': 'продукты'},
            {'url': 'contact', 'active': ['contact'], 'name': 'контакты'},
        ]
    }