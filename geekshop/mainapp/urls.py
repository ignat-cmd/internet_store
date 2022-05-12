from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [

    path('', mainapp.products, name='main'),
    path('<int:category_id>/', mainapp.category, name='category'),
    path('<int:category_id>/<int:page>',
         mainapp.category, name='category_with_page'),
    path('product/<int:product_id>', mainapp.product, name='product'),
    path('product/<int:product_id>', mainapp.product, name='product')

    path('', mainapp.index, name='index'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
]

# Хостим папку media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

