# 🧪 Informe de Pruebas - Alke Wallet

## Proyecto Módulo 7 - Acceso a Datos en Aplicaciones Python Django

**Estudiante:** Alba Moreno  
**Proyecto:** Alke Wallet  
**Framework:** Django 5.2  
**Tipo de pruebas:** Pruebas automatizadas con Django TestCase

---

## 1. Objetivo

El objetivo de las pruebas es verificar el correcto funcionamiento de los principales componentes de la aplicación Alke Wallet, especialmente los modelos, autenticación, operaciones de creación y validaciones implementadas.

---

## 2. Herramientas utilizadas

Las pruebas fueron desarrolladas utilizando el sistema de pruebas incorporado en Django:

```python
from django.test import TestCase
```

Para ejecutar las pruebas se utilizó:

```bash
python manage.py test
```

Django genera una base de datos temporal para ejecutar las pruebas sin modificar los datos reales de la aplicación.

---

## 3. Pruebas realizadas

Se implementaron 6 pruebas automáticas.

### Prueba 1: Modelo Cuenta

**Objetivo:** comprobar que el modelo Cuenta representa correctamente el número de cuenta y el usuario asociado.

**Resultado:** Aprobada.

---

### Prueba 2: Protección de vistas mediante autenticación

**Objetivo:** comprobar que un usuario que no ha iniciado sesión no pueda acceder directamente al listado de cuentas.

**Resultado esperado:** redirección al inicio de sesión.

**Resultado:** Aprobada.

---

### Prueba 3: Acceso de usuario autenticado

**Objetivo:** comprobar que un usuario autenticado pueda acceder correctamente al listado de cuentas.

**Resultado esperado:** respuesta HTTP 200 y visualización de las cuentas registradas.

**Resultado:** Aprobada.

---

### Prueba 4: Creación de cuenta

**Objetivo:** comprobar que el sistema permita crear una nueva cuenta mediante el formulario correspondiente.

**Validaciones realizadas:**

- Usuario asociado.
- Número de cuenta.
- Saldo inicial.
- Registro correcto en la base de datos.

**Resultado:** Aprobada.

---

### Prueba 5: Validación de transacciones

**Objetivo:** comprobar que una transacción no pueda utilizar la misma cuenta como origen y destino.

El formulario debe rechazar una operación cuando:

```text
Cuenta origen = Cuenta destino
```

**Resultado:** Aprobada.

---

### Prueba 6: Creación de transacción

**Objetivo:** comprobar que una transacción válida pueda ser registrada correctamente.

La prueba utiliza:

- Cuenta de origen.
- Cuenta de destino.
- Moneda.
- Monto.
- Descripción.

Posteriormente se verifica que la transacción haya sido almacenada en la base de datos de prueba.

**Resultado:** Aprobada.

---

## 4. Resultado de ejecución

Al ejecutar:

```bash
python manage.py test
```

se obtuvo:

```text
Ran 6 tests in 8.422s

OK
```

Esto indica que las 6 pruebas implementadas fueron ejecutadas correctamente sin errores.

---

## 5. Comprobación adicional del proyecto

También se ejecutó:

```bash
python manage.py check
```

Resultado:

```text
System check identified no issues (0 silenced).
```

Esta comprobación permite verificar que Django no detecta problemas en la configuración general del proyecto.

---

## 6. Evidencia

La evidencia visual del resultado de las pruebas se encuentra almacenada en:

```text
capturas/006_tests_ok.png
```

Además, la carpeta `capturas` contiene evidencias del funcionamiento de:

- Migraciones.
- Consultas personalizadas.
- CRUD de cuentas.
- Django Admin.
- CRUD de transacciones.
- Pruebas automáticas.

---

## 7. Conclusión

Las pruebas realizadas permiten comprobar el funcionamiento de los componentes principales de Alke Wallet.

Los resultados obtenidos muestran que el sistema responde correctamente en las funcionalidades evaluadas, incluyendo autenticación, creación de cuentas, creación de transacciones y validaciones de formularios.

Las 6 pruebas automáticas finalizaron correctamente con resultado `OK`.

---

**Alba Moreno**  
Bootcamp Full Stack Python  
Proyecto Módulo 7 - Alke Wallet
