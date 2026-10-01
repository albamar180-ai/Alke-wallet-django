from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cuenta, Transaccion
from .forms import CuentaForm, TransaccionForm


# =========================================================
# CRUD DE CUENTAS
# =========================================================

@login_required
def lista_cuentas(request):
    cuentas = Cuenta.objects.select_related('usuario').all()

    return render(
        request,
        'gestion/lista_cuentas.html',
        {'cuentas': cuentas}
    )


@login_required
def crear_cuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_cuentas')
    else:
        form = CuentaForm()

    return render(
        request,
        'gestion/form_cuenta.html',
        {
            'form': form,
            'titulo': 'Crear cuenta'
        }
    )


@login_required
def editar_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)

    if request.method == 'POST':
        form = CuentaForm(request.POST, instance=cuenta)

        if form.is_valid():
            form.save()
            return redirect('lista_cuentas')
    else:
        form = CuentaForm(instance=cuenta)

    return render(
        request,
        'gestion/form_cuenta.html',
        {
            'form': form,
            'titulo': 'Editar cuenta'
        }
    )


@login_required
def eliminar_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)

    if request.method == 'POST':
        cuenta.delete()
        return redirect('lista_cuentas')

    return render(
        request,
        'gestion/confirmar_eliminar.html',
        {'cuenta': cuenta}
    )


# =========================================================
# CRUD DE TRANSACCIONES
# =========================================================

@login_required
def lista_transacciones(request):
    transacciones = Transaccion.objects.select_related(
        'cuenta_origen',
        'cuenta_destino',
        'moneda'
    ).order_by('-fecha')

    return render(
        request,
        'gestion/lista_transacciones.html',
        {'transacciones': transacciones}
    )


@login_required
def crear_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm()

    return render(
        request,
        'gestion/form_transaccion.html',
        {
            'form': form,
            'titulo': 'Nueva transacción'
        }
    )


@login_required
def editar_transaccion(request, transaccion_id):
    transaccion = get_object_or_404(
        Transaccion,
        id=transaccion_id
    )

    if request.method == 'POST':
        form = TransaccionForm(
            request.POST,
            instance=transaccion
        )

        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm(instance=transaccion)

    return render(
        request,
        'gestion/form_transaccion.html',
        {
            'form': form,
            'titulo': 'Editar transacción'
        }
    )


@login_required
def eliminar_transaccion(request, transaccion_id):
    transaccion = get_object_or_404(
        Transaccion,
        id=transaccion_id
    )

    if request.method == 'POST':
        transaccion.delete()
        return redirect('lista_transacciones')

    return render(
        request,
        'gestion/confirmar_eliminar_transaccion.html',
        {'transaccion': transaccion}
    )