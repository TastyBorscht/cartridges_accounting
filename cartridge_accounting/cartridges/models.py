from django.core.validators import MinValueValidator
from django.db import models


class Cartridge(models.Model):
    name = models.CharField(
        verbose_name='Наименование картриджа',
        max_length=50
    )
    device_name = models.CharField(
        verbose_name='Наименование устройства',
        max_length = 50
    )
    acceptance_date = models.DateField(
        verbose_name='Дата ввода в эксп.',
    )
    decommissioning_date = models.DateField(
        verbose_name='Дата вывода из эксп.',
        null=True
    )
    inventory_number = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='инвентарный номер',
        unique=True,
    )
    is_functional = models.BooleanField(
        default=True,
        verbose_name='рабочий',
        null=True
    )
    class Meta:
        ordering = ('acceptance_date',)
        verbose_name = 'картридж'
        verbose_name_plural = 'картриджи'

    def __str__(self):
        return f'Картридж для устройства {self.device_name}'
