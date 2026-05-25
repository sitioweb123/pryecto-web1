from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

@csrf_exempt
def create_admin_temp(request):
    """Endpoint temporal para crear superusuario - ¡ELIMINAR DESPUÉS DE USAR!"""
    # Solo procesar si es POST o GET (para pruebas fáciles)
    if request.method not in ['GET', 'POST']:
        return HttpResponse("Método no permitido", status=405)
    
    username = "admin"
    email = "admin@tu-dominio.com"
    password = "Admin123!Seguro"  # ← CÁMBIALA después
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse(f"✅ Superusuario '{username}' creado. Usuario: {username} | Contraseña: {password}")
    return HttpResponse(f"⚠️ El usuario '{username}' ya existe. Intenta login en /admin")