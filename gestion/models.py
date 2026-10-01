from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


# Cuenta digital asociada a un usuario de Django.
# Se utiliza OneToOneField porque cada usuario tendrá una cuenta principal.
class Cuenta(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cuenta'
    )
    numero_cuenta = models.CharField(
        max_length=20,
        unique=True
    )
    saldo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero_cuenta} - {self.usuario.username}"


# Monedas disponibles dentro de Alke Wallet.
class Moneda(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return self.codigo


# Registra las transferencias realizadas entre cuentas.
class Transaccion(models.Model):
    cuenta_origen = models.ForeignKey(
        Cuenta,
        on_delete=models.PROTECT,
        related_name='transacciones_enviadas'
    )
    cuenta_destino = models.ForeignKey(
        Cuenta,
        on_delete=models.PROTECT,
        related_name='transacciones_recibidas'
    )
    moneda = models.ForeignKey(
        Moneda,
        on_delete=models.PROTECT,
        related_name='transacciones'
    )
    monto = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"Transferencia #{self.id} - ${self.monto}"