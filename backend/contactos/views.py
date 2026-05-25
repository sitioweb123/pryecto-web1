from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt  # ← AGREGA ESTE IMPORT

User = get_user_model()

@csrf_exempt  # ← AGREGA ESTE DECORADOR (justo antes de @require_http_methods)
@require_http_methods(["POST"])
def create_admin_temp(request):
    """Endpoint temporal para crear superusuario - ¡ELIMINAR DESPUÉS DE USAR!"""
    username = "admin"
    email = "admin@tu-dominio.com"
    password = "TuPasswordSeguro123!"  # ← CÁMBIALA por una segura
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse(f"✅ Superusuario '{username}' creado exitosamente")
    return HttpResponse(f"⚠️ El usuario '{username}' ya existe")