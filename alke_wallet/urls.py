from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticación de Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Aplicación Alke Wallet
    path('', include('gestion.urls')),
]