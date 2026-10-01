from django.contrib import admin
from .models import Cuenta, Moneda, Transaccion


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('numero_cuenta', 'usuario', 'saldo', 'fecha_creacion')
    search_fields = ('numero_cuenta', 'usuario__username')


@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cuenta_origen',
        'cuenta_destino',
        'moneda',
        'monto',
        'fecha'
    )
    search_fields = (
        'cuenta_origen__numero_cuenta',
        'cuenta_destino__numero_cuenta'
    )
    list_filter = ('moneda', 'fecha')