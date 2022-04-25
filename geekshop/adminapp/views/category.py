from django.http.response import HttpResponseRedirect
from django.urls import reverse
from turtle import title
from django.shortcuts import get_object_or_404, render
from mainapp.models import ProductCategory
from adminapp.utils import superuser_requared
from adminapp.forms import ProductCategoryAdminForm


@superuser_requared
def category_create(request):
    title = 'Создание пользователя'

    if request.method == 'POST':
        form = ProductCategoryAdminForm(
            request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategoryAdminForm()

    return render(request, 'adminapp/category/edit.html', context={
        'form': form,
        'title': title,
    })


@superuser_requared
def categories(request):
    title = 'Категории'

    categories = ProductCategory.objects.all().order_by('id')

    return render(request, 'adminapp/category/categories.html', context={
        'title': title,
        'objects': categories,
    })


@superuser_requared
def category_update(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    title = 'Создание пользователя'

    if request.method == 'POST':
        form = ProductCategoryAdminForm(
            request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategoryAdminForm(instance=category)

    return render(request, 'adminapp/category/edit.html', context={
        'form': form,
        'title': title,
    })


@superuser_requared
def category_delete(request):
    pass
