from django.core.validators import MinValueValidator
from django.db import models
from datetime import date





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
        verbose_name='Дата получения',
    )
    decommissioning_date = models.DateField(
        verbose_name='Дата ввода в эксп.',
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

class CartridgeCommissioning(models.Model):
    cartridge = models.OneToOneField(
        'Cartridge',
        on_delete=models.CASCADE,
        verbose_name='Картридж'
    )
    location = models.CharField(
        verbose_name='Место установки',
        max_length=100
    )
    date = models.DateField(
        verbose_name='Дата ввода',
        auto_now_add=True
    )
class CommissionedCartridge(models.Model):
    name = models.CharField(
        verbose_name='Наименование картриджа',
        max_length=50,
        default='Не указано'  # Добавляем
    )
    device_name = models.CharField(
        verbose_name='Наименование устройства',
        max_length=50,
        default='Не указано'  # Добавляем
    )
    acceptance_date = models.DateField(
        verbose_name='Дата получения',
        default=date.today  # Добавляем
    )
    decommissioning_date = models.DateField(
        verbose_name='Дата ввода в эксп.',
        default=date.today  # Добавляем
    )
    inventory_number = models.IntegerField(
        verbose_name='инвентарный номер',
        default=0  # Добавляем
    )
    is_functional = models.BooleanField(
        verbose_name='рабочий',
        default=True  # Добавляем
    )
    location = models.CharField(
        verbose_name='Место установки',
        max_length=100,
        default='Не указано'  # Добавляем
    )
    commission_date = models.DateField(
        verbose_name='Дата ввода',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Введённый в эксплуатацию картридж'
        verbose_name_plural = 'Введённые в эксплуатацию картриджи'