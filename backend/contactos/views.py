from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

User = get_user_model()

@require_http_methods(["POST"])  # Solo permite POST por seguridad
def create_admin_temp(request):
    """Endpoint temporal para crear superusuario - ¡ELIMINAR DESPUÉS DE USAR!"""
    # ⚠️ Cambia estas credenciales por unas seguras
    username = "admin"
    email = "admin@tu-dominio.com"
    password = "TuPasswordSeguro123!"  # ← CÁMBIALA
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse(f"✅ Superusuario '{username}' creado exitosamente")
    return HttpResponse(f"⚠️ El usuario '{username}' ya existe")