# Generated by Django 2.1.2 on 2018-10-09 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20181006_2106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dumptruck',
            options={'verbose_name': 'самосвал', 'verbose_name_plural': 'Самосвалы в работе'},
        ),
        migrations.AlterModelOptions(
            name='dumptruckmodel',
            options={'verbose_name': 'Характеристики модели самосвала', 'verbose_name_plural': 'Характеристики моделелей самосвалов'},
        ),
    ]
