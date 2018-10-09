from django.db import models

class  DumpTruckModel(models.Model):
    model = models.CharField('Модель', max_length=20)
    max_load = models.IntegerField('Максимальная грузоподъемность')

    class Meta:
        verbose_name = 'Характеристики модели самосвала'
        verbose_name_plural = 'Характеристики моделелей самосвалов'

    def __str__(self):
        return self.model


class  DumpTruck(models.Model):
    number = models.CharField('Бортовой номер', max_length=20)
    track_model = models.ForeignKey(DumpTruckModel, on_delete=models.CASCADE, default=0)
    current_weight = models.PositiveSmallIntegerField('Текущий вес', default=0)

    class Meta:
        verbose_name = 'самосвал'
        verbose_name_plural = 'Самосвалы в работе'

    def __str__(self):
        return self.number

    def overload(self):
        if self.current_weight - self.track_model.max_load > 0:
            return round(((self.current_weight - self.track_model.max_load)/self.track_model.max_load)*100, 1)
        else:
            return ''
