# Generated by Django 5.0.2 on 2024-03-04 06:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('digital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model_product',
        ),
    ]