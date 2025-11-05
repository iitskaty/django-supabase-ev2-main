from django.contrib import admin
from .models import Contacto

#Registar el modelo de contactos en admin 
@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    search_fields = ('nombre', 'correo')
