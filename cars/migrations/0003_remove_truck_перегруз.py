# Generated by Django 2.1.2 on 2018-10-05 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20181005_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='перегруз',
        ),
    ]
