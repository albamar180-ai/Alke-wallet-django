from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Cuenta, Moneda, Transaccion
from .forms import TransaccionForm


class AlkeWalletTests(TestCase):

    def setUp(self):
        # Usuario utilizado para iniciar sesión durante las pruebas
        self.usuario_login = User.objects.create_user(
            username='tester',
            password='Test1234'
        )

        # Usuarios asociados a las cuentas
        self.usuario1 = User.objects.create_user(
            username='uno',
            password='Test1234'
        )

        self.usuario2 = User.objects.create_user(
            username='dos',
            password='Test1234'
        )

        self.usuario3 = User.objects.create_user(
            username='tres',
            password='Test1234'
        )

        # Cuentas de prueba
        self.cuenta1 = Cuenta.objects.create(
            usuario=self.usuario1,
            numero_cuenta='TEST001',
            saldo=Decimal('100000.00')
        )

        self.cuenta2 = Cuenta.objects.create(
            usuario=self.usuario2,
            numero_cuenta='TEST002',
            saldo=Decimal('50000.00')
        )

        # Moneda de prueba
        self.moneda = Moneda.objects.create(
            nombre='Peso Chileno',
            codigo='CLP'
        )

    def test_modelo_cuenta(self):
        """Comprueba la representación de una cuenta."""
        self.assertEqual(
            str(self.cuenta1),
            'TEST001 - uno'
        )

    def test_lista_cuentas_requiere_login(self):
        """Comprueba que las cuentas estén protegidas por login."""
        respuesta = self.client.get(
            reverse('lista_cuentas')
        )

        self.assertEqual(
            respuesta.status_code,
            302
        )

    def test_lista_cuentas_usuario_autenticado(self):
        """Comprueba que un usuario autenticado pueda ver las cuentas."""
        self.client.login(
            username='tester',
            password='Test1234'
        )

        respuesta = self.client.get(
            reverse('lista_cuentas')
        )

        self.assertEqual(
            respuesta.status_code,
            200
        )

        self.assertContains(
            respuesta,
            'TEST001'
        )

    def test_crear_cuenta(self):
        """Comprueba la creación de una cuenta mediante el formulario."""
        self.client.login(
            username='tester',
            password='Test1234'
        )

        respuesta = self.client.post(
            reverse('crear_cuenta'),
            {
                'usuario': self.usuario3.id,
                'numero_cuenta': 'TEST003',
                'saldo': '25000.00',
            }
        )

        self.assertEqual(
            respuesta.status_code,
            302
        )

        self.assertTrue(
            Cuenta.objects.filter(
                numero_cuenta='TEST003'
            ).exists()
        )

    def test_validacion_cuentas_diferentes(self):
        """
        Comprueba que una transacción no pueda tener
        la misma cuenta como origen y destino.
        """
        formulario = TransaccionForm(
            data={
                'cuenta_origen': self.cuenta1.id,
                'cuenta_destino': self.cuenta1.id,
                'moneda': self.moneda.id,
                'monto': '1000.00',
                'descripcion': 'Prueba',
            }
        )

        self.assertFalse(
            formulario.is_valid()
        )

        self.assertIn(
            'La cuenta de origen y destino deben ser diferentes.',
            formulario.non_field_errors()
        )

    def test_crear_transaccion(self):
        """Comprueba la creación de una transacción."""
        self.client.login(
            username='tester',
            password='Test1234'
        )

        respuesta = self.client.post(
            reverse('crear_transaccion'),
            {
                'cuenta_origen': self.cuenta1.id,
                'cuenta_destino': self.cuenta2.id,
                'moneda': self.moneda.id,
                'monto': '1000.00',
                'descripcion': 'Prueba automática',
            }
        )

        self.assertEqual(
            respuesta.status_code,
            302
        )

        self.assertEqual(
            Transaccion.objects.count(),
            1
        )