# Generated by Django 2.0.4 on 2018-06-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180627_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='db_pass',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
