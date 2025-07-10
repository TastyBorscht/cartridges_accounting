from django import forms
from .models import Cartridge
from .models import CartridgeCommissioning

class CartridgeCreateForm(forms.ModelForm):
    class Meta:
        model = Cartridge
        fields = [
            'name',
            'device_name',
            'acceptance_date',
            'inventory_number',
            'added_by',
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
class CommissioningForm(forms.ModelForm):
    class Meta:
        model = CartridgeCommissioning
        fields = ['location']