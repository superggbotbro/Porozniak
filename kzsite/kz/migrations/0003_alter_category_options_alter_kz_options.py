# Generated by Django 4.0.6 on 2022-07-20 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kz', '0002_category_kz_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категорий'},
        ),
        migrations.AlterModelOptions(
            name='kz',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Казахстан', 'verbose_name_plural': 'Казахстан'},
        ),
    ]
