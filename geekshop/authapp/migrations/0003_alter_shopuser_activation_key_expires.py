# Generated by Django 4.0.4 on 2022-04-26 20:59

import authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_shopuser_activation_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=authapp.models.get_expire_reg_key),
        ),
    ]
