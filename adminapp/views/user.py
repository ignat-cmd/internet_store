from django.http.response import HttpResponseRedirect
from turtle import title
from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from adminapp.utils import superuser_requared
from adminapp.forms import ShopUserCreateAdminForm, ShopUserEditAdminForm
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator


class UsersCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserCreateAdminForm
    template_name = 'adminapp/user/edit.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(superuser_requared)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Changed users_view on CBV


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/user/users.html'

    @method_decorator(superuser_requared)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UsersUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserEditAdminForm
    template_name = 'adminapp/user/edit.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(superuser_requared)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'

        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user/delete.html'
    success_url = reverse_lazy('admin:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление пользователя'

        return context
