from django.http.response import HttpResponseRedirect
from turtle import title
from django.shortcuts import render, get_object_or_404
from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from authapp.models import ShopUser
from adminapp.utils import superuser_requared
from adminapp.forms import ShopUserAdminForm
from django.urls import reverse
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator


@superuser_requared
def user_create(request):
    title = 'Создание пользователя'

    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(
            request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        edit_form = ShopUserRegisterForm()

    return render(request, 'adminapp/user/edit.html', context={
        'form': edit_form,
        'title': title,
    })


@superuser_requared
def users(request):
    title = 'пользователи'

    users = ShopUser.objects.all().order_by('id')

    return render(request, 'adminapp/user/users.html', context={
        'title': title,
        'objects': users,
    })


@superuser_requared
def user_update(request, pk):
    title = 'Редактирование пользователя'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminForm(
            request.POST, request.FILES, instance=user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        edit_form = ShopUserAdminForm(instance=user)

    return render(request, 'adminapp/user/edit.html', context={
        'form': edit_form,
        'title': title,
    })


@superuser_requared
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    return render(request, 'adminapp/user/delete.html', context={
        'title': title,
        'user_to_delete': user,
    })
