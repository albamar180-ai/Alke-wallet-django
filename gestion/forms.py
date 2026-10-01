from django import forms
from .models import Cuenta, Transaccion


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['usuario', 'numero_cuenta', 'saldo']

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'numero_cuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = [
            'cuenta_origen',
            'cuenta_destino',
            'moneda',
            'monto',
            'descripcion'
        ]

        widgets = {
            'cuenta_origen': forms.Select(attrs={'class': 'form-control'}),
            'cuenta_destino': forms.Select(attrs={'class': 'form-control'}),
            'moneda': forms.Select(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        origen = cleaned_data.get('cuenta_origen')
        destino = cleaned_data.get('cuenta_destino')

        if origen and destino and origen == destino:
            raise forms.ValidationError(
                'La cuenta de origen y destino deben ser diferentes.'
            )

        return cleaned_data