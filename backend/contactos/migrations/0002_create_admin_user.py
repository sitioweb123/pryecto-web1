from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    # Creamos el usuario solo si no existe (para evitar errores si se ejecuta 2 veces)
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@tuweb.com',
            password='admin123'  # 👈 ¡CAMBIA ESTO por una contraseña segura!
        )
        print("✅ Superusuario 'admin' creado exitosamente")

class Migration(migrations.Migration):

    # ⚠️ IMPORTANTE: Asegúrate de que el segundo nombre coincida con 
    # el archivo ANTERIOR a este (usualmente '0001_initial').
    # Mira en la carpeta migrations/ para confirmar el nombre exacto.
    dependencies = [
        ('contactos', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]