# 💳 Alke Wallet

## Proyecto Módulo 7 - Acceso a Datos en Aplicaciones Python Django

**Estudiante:** Alba Moreno  
**Bootcamp:** Full Stack Python  
**Framework:** Django 5.2  
**Base de datos de desarrollo:** SQLite  

---

## 📌 Descripción del proyecto

Alke Wallet es una aplicación web desarrollada con Django para administrar cuentas digitales y registrar transacciones entre usuarios.

El proyecto permite trabajar con una base de datos relacional utilizando el ORM de Django, migraciones, formularios, autenticación, panel de administración, consultas personalizadas y operaciones CRUD.

---

## 🎯 Objetivo

Desarrollar una aplicación web que permita administrar información financiera básica mediante Django y una base de datos relacional.

La aplicación permite:

- Administrar cuentas digitales.
- Registrar transacciones.
- Consultar movimientos.
- Trabajar con diferentes monedas.
- Crear, listar, editar y eliminar registros.
- Proteger las vistas mediante autenticación.
- Administrar los datos desde Django Admin.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Django 5.2
- SQLite
- HTML5
- CSS
- Django Templates
- Django ORM
- Visual Studio Code
- Git
- GitHub

---

## 📂 Estructura principal

```text
PROYECTO/
│
├── alke_wallet/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── gestion/
│   ├── migrations/
│   ├── static/
│   │   └── gestion/
│   │       └── style.css
│   ├── templates/
│   │   ├── gestion/
│   │   └── registration/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── capturas/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗄️ Modelo de datos

La aplicación utiliza tres modelos principales:

### Cuenta

Representa una cuenta digital.

Campos principales:

- Usuario
- Número de cuenta
- Saldo
- Fecha de creación

Cada cuenta se encuentra asociada a un usuario de Django.

### Moneda

Representa las monedas disponibles para realizar transacciones.

Campos:

- Nombre
- Código

Ejemplos utilizados:

- CLP
- USD
- EUR

### Transacción

Registra los movimientos entre cuentas.

Campos principales:

- Cuenta de origen
- Cuenta de destino
- Moneda
- Monto
- Fecha
- Descripción

---

## 🔗 Relaciones entre modelos

El proyecto utiliza relaciones proporcionadas por el ORM de Django.

### One-to-One

Cada usuario posee una cuenta principal:

```python
usuario = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='cuenta'
)
```

### Many-to-One

Una cuenta puede participar en múltiples transacciones.

Las relaciones se implementan mediante `ForeignKey`.

Ejemplo:

```python
cuenta_origen = models.ForeignKey(
    Cuenta,
    on_delete=models.PROTECT,
    related_name='transacciones_enviadas'
)
```

Esto permite consultar fácilmente las transacciones enviadas y recibidas por cada cuenta.

---

## 🔄 Migraciones

Después de crear los modelos se generaron y aplicaron las migraciones de Django.

```bash
python manage.py makemigrations
python manage.py migrate
```

Las migraciones permiten mantener sincronizada la estructura de los modelos con la base de datos.

---

## 📊 Datos de prueba

Para demostrar el funcionamiento de la aplicación se ingresaron datos de ejemplo.

### Cuentas

- ALK001 - ana
- ALK002 - luis
- ALK003 - maria
- ALK004 - pedro
- ALK005 - sofia

### Monedas

- CLP
- USD
- EUR

### Transacciones

Se registraron 8 transacciones de demostración entre las distintas cuentas y monedas.

Esto permite visualizar mejor el funcionamiento de consultas, relaciones y operaciones CRUD.

---

## 🔎 Consultas ORM

Se realizaron consultas utilizando el ORM de Django.

### Filter

Ejemplo para obtener cuentas con saldo superior a $600.000:

```python
Cuenta.objects.filter(saldo__gt=600000)
```

### Exclude

Ejemplo para excluir cuentas con saldo inferior a $500.000:

```python
Cuenta.objects.exclude(saldo__lt=500000)
```

### Annotate

También se realizaron consultas agregadas para calcular información relacionada con las transacciones:

```python
Cuenta.objects.annotate(
    total_enviado=Sum('transacciones_enviadas__monto'),
    cantidad_transacciones=Count('transacciones_enviadas')
)
```

---

## 🧾 Consulta SQL personalizada

Además del ORM, se utilizó una consulta SQL mediante `raw()`.

```python
consulta = """
SELECT *
FROM gestion_cuenta
WHERE saldo > 700000
"""

resultado = Cuenta.objects.raw(consulta)
```

Esto permite combinar las ventajas del ORM con consultas SQL personalizadas cuando sea necesario.

---

## ✏️ Operaciones CRUD

La aplicación implementa operaciones CRUD para cuentas y transacciones.

### Cuentas

- Crear cuenta
- Listar cuentas
- Editar cuenta
- Eliminar cuenta

### Transacciones

- Crear transacción
- Listar transacciones
- Editar transacción
- Eliminar transacción

Las rutas dinámicas permiten identificar los registros mediante su ID.

---

## 🔐 Autenticación

Se utiliza el sistema de autenticación incluido en Django.

Las principales vistas se encuentran protegidas mediante:

```python
@login_required
```

Un usuario debe iniciar sesión para acceder a la administración de cuentas y transacciones.

La aplicación también permite cerrar sesión de manera segura mediante una solicitud POST con protección CSRF.

---

## 🛡️ Protección CSRF

Los formularios utilizan:

```django
{% csrf_token %}
```

Esto permite utilizar la protección CSRF incorporada en Django para las solicitudes POST.

---

## ⚙️ Django Admin

Los modelos fueron registrados en el panel administrativo de Django.

Desde `/admin/` es posible administrar:

- Usuarios
- Grupos
- Cuentas
- Monedas
- Transacciones

También se configuraron opciones como:

- `list_display`
- `search_fields`
- `list_filter`

---

## 🎨 Archivos estáticos

El proyecto utiliza `django.contrib.staticfiles`.

Se creó el archivo:

```text
gestion/static/gestion/style.css
```

y se carga desde la plantilla base mediante:

```django
{% load static %}
```

y:

```html
<link rel="stylesheet" href="{% static 'gestion/style.css' %}">
```

---

## ✅ Validaciones

Se implementaron validaciones en los modelos y formularios.

Entre ellas:

- El saldo no puede ser negativo.
- El monto de una transacción debe ser superior a cero.
- El número de cuenta debe ser único.
- El código de moneda debe ser único.
- La cuenta de origen y destino de una transacción deben ser diferentes.

---

## 🧪 Pruebas automáticas

Se implementaron pruebas utilizando `django.test.TestCase`.

Para ejecutarlas:

```bash
python manage.py test
```

Resultado obtenido:

```text
Ran 6 tests

OK
```

Las pruebas verifican:

- Funcionamiento del modelo Cuenta.
- Protección de vistas mediante login.
- Acceso de usuarios autenticados.
- Creación de cuentas.
- Validación de cuentas de origen y destino.
- Creación de transacciones.

---

## 💾 Base de datos

Durante el desarrollo se utilizó SQLite debido a su integración directa con Django y facilidad de configuración.

Para un entorno de producción, el proyecto puede configurarse para utilizar PostgreSQL mediante la sección `DATABASES` de `settings.py` y el adaptador correspondiente.

---

## ▶️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/albamar180-ai/Alke-wallet-django
```

### 2. Entrar al proyecto

```bash
cd PROYECTO
```

### 3. Crear un entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual en Windows

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Aplicar migraciones

```bash
python manage.py migrate
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

### 8. Abrir la aplicación

En el navegador ingresar a:

```text
http://127.0.0.1:8000/
```

---

## 📸 Evidencias

La carpeta `capturas/` contiene evidencias del desarrollo y funcionamiento del proyecto.

Entre ellas:

- Migraciones aplicadas.
- Modelos registrados en Django Admin.
- Consultas ORM y SQL.
- CRUD de cuentas.
- CRUD de transacciones.
- Resultado de pruebas automáticas.

---

## 💡 Reflexión sobre el uso del ORM

El ORM de Django facilita el trabajo con bases de datos porque permite realizar consultas utilizando clases y métodos de Python sin escribir SQL para todas las operaciones.

También permite representar las relaciones entre las tablas directamente mediante los modelos.

---

## 💡 Reflexión sobre las migraciones

Las migraciones permiten controlar los cambios realizados en los modelos y aplicarlos posteriormente a la base de datos.

Esto facilita mantener organizada y actualizada la estructura del proyecto durante su desarrollo.

---

## 💡 Reflexión sobre consultas personalizadas

El ORM permite resolver gran parte de las consultas necesarias mediante métodos como `filter()`, `exclude()` y `annotate()`.

Sin embargo, Django también permite utilizar SQL personalizado mediante `raw()` cuando se necesita realizar una consulta más específica.

---

## 🚀 Conclusión

El desarrollo de Alke Wallet permitió aplicar los principales conceptos de acceso a datos con Django: creación de modelos, relaciones entre entidades, migraciones, ORM, consultas personalizadas, formularios, operaciones CRUD, autenticación, administración, archivos estáticos y pruebas automáticas.

El proyecto integra estos elementos en una aplicación web sencilla para administrar cuentas digitales y transacciones.

---

**Alba Moreno**  
Bootcamp Full Stack Python  
Proyecto Módulo 7 - Alke Wallet
