from django.urls import path
from . import views

urlpatterns = [

    # CUENTAS
    path(
        '',
        views.lista_cuentas,
        name='lista_cuentas'
    ),

    path(
        'cuentas/nueva/',
        views.crear_cuenta,
        name='crear_cuenta'
    ),

    path(
        'cuentas/<int:cuenta_id>/editar/',
        views.editar_cuenta,
        name='editar_cuenta'
    ),

    path(
        'cuentas/<int:cuenta_id>/eliminar/',
        views.eliminar_cuenta,
        name='eliminar_cuenta'
    ),

    # TRANSACCIONES
    path(
        'transacciones/',
        views.lista_transacciones,
        name='lista_transacciones'
    ),

    path(
        'transacciones/nueva/',
        views.crear_transaccion,
        name='crear_transaccion'
    ),

    path(
        'transacciones/<int:transaccion_id>/editar/',
        views.editar_transaccion,
        name='editar_transaccion'
    ),

    path(
        'transacciones/<int:transaccion_id>/eliminar/',
        views.eliminar_transaccion,
        name='eliminar_transaccion'
    ),
]