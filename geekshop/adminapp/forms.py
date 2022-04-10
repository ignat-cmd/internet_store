from dataclasses import fields
from django import forms
from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


class ShopUserAdminForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

# Так как используем bootstrap нужно это:


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name, field in self.field.items():
        field.wiget.attrs['class'] = 'form_control'
        field.help_text = ''
