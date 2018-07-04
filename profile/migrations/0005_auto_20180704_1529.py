# Generated by Django 2.0.6 on 2018-07-04 15:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_remove_database_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Название БД некорректно.', regex='^[a-zA-Z_]+$')]),
        ),
    ]
