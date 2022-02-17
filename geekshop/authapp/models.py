from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ShopUser(AbstractUser):
    age = models.PositiveBigIntegerField(verbose_name='возраст')
    avatar = models.ImageField(
        verbose_name='аватар', upload_to='users_avatars', blank=True)
