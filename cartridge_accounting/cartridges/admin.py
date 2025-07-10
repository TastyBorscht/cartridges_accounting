from django.contrib import admin
from .models import Cartridge, CommissionedCartridge

# Register your models here.

admin.site.register(Cartridge)

@admin.register(CommissionedCartridge)
class CommissionedCartridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_name', 'location', 'commission_date')
    search_fields = ('name', 'device_name', 'location')