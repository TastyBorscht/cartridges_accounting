from django import forms
from .models import Cartridge

class CartridgeForm(forms.ModelForm):
    class Meta:
        model = Cartridge
        fields = [
            'name',
            'device_name',
            'acceptance_date',
            'inventory_number',
        ]
        widgets = {
            'acceptance_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
