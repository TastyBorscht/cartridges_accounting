# Generated by Django 3.2.16 on 2025-07-10 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cartridges', '0005_alter_cartridge_decommissioning_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartridge',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Добавил'),
        ),
    ]
