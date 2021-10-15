from django.contrib import admin
from .models import Domanda,Categoria,Risposta
# Register your models here.

admin.site.register(Domanda)
admin.site.register(Categoria)
admin.site.register(Risposta)