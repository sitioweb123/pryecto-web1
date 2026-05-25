from django.contrib import admin
from django.urls import path, include
from contactos import views  # ← Ajusta según donde pusiste la vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),  # Si usas DRF
    # ... tus otras URLs ...
    
    # ⚠️ AGREGA ESTA LÍNEA (temporal):
    path('_create-admin-temp/', views.create_admin_temp, name='create_admin_temp'),
]