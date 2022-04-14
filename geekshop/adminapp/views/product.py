from pyexpat import model
from turtle import title
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from mainapp.models import Product, ProductCategory
from adminapp.utils import superuser_requared
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from adminapp.utils import superuser_requared
from django.views.generic.detail import DetailView


# Create Product in Category
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'  # Django makes form auto
    template_name = 'adminapp/product/edit.html'

    @method_decorator(superuser_requared)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {
            'category': self.get_category()
        }

    def get_success_url(self):
        return reverse('admin:products', kwargs=self.kwargs)

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.get(pk=self.kwargs['pk'])
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/product/products.html'

    @method_decorator(superuser_requared)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {
            'category': self.get_category(),
            'product': self.get_product()
        }

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_product(self):
        return Product.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        products = Product.objects.filter(
            category=category).order_by('id')
        context = super().get_context_data(**kwargs)
        context = {
            'category': category,
            'objects': products
        }
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product/product_read.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product/product_updata.html'
    success_url = reverse_lazy('admin:users')
    fields = '__all__'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product/product_delete.html'
    success_url = reverse_lazy('admin:products')

    def Delete(self, request, *args, **kwarga):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
