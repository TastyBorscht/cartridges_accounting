from django import forms
from .models import Cartridge

class CartridgeCreateForm(forms.ModelForm):
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
class CartridgeUpdateForm(forms.ModelForm):
    class Meta(CartridgeCreateForm.Meta):
        fields = [
            'name',
            'device_name',
            'acceptance_date',
            'inventory_number',
        ]