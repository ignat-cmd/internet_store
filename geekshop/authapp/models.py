from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.

# Определяет годность ссылки

def get_expire_reg_key():
    return now() + timedelta(hours=48)

class ShopUser(AbstractUser):
    age = models.PositiveBigIntegerField(verbose_name='возраст')
    avatar = models.ImageField(
        verbose_name='аватар', upload_to='users_avatars', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default = get_expire_reg_key)
    
    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True