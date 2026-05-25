from django.contrib import admin
from .models import Contacto  # ← Cambia "Contacto" por el nombre real de tu modelo

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'email')  # ← Ajusta a tus campos
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_creacion',)