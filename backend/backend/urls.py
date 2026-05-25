from django.contrib import admin
from django.urls import path, include
from contactos import views  # ← Ajusta si tu vista está en otro lugar

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... tus otras URLs ...
    
    # ← AGREGA ESTA LÍNEA:
    path('_create-admin-temp/', views.create_admin_temp, name='create_admin_temp'),
]