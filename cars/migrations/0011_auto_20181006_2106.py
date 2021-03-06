# Generated by Django 2.1.2 on 2018-10-06 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20181006_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dumptruck',
            options={'verbose_name': 'новый самосвал', 'verbose_name_plural': 'Самосвалы в работе'},
        ),
        migrations.AlterModelOptions(
            name='dumptruckmodel',
            options={'verbose_name': 'Характеристики новой моделели самосвала', 'verbose_name_plural': 'Характеристики моделелей самосвалов'},
        ),
        migrations.RemoveField(
            model_name='dumptruck',
            name='model',
        ),
        migrations.AddField(
            model_name='dumptruck',
            name='track_model',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cars.DumpTruckModel'),
        ),
        migrations.AlterField(
            model_name='dumptruck',
            name='current_weight',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Текущий вес'),
        ),
    ]
