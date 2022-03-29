
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='main'),
    path('<int:category_id>/', mainapp.category, name='category'),
    path('product/<int:product_id>', mainapp.product, name='product')
]
