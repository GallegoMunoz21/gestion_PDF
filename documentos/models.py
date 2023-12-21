# documentos/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
import random

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    # Agrega o cambia related_name en los siguientes campos
    groups = models.ManyToManyField(Group, verbose_name="grupos", blank=True, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, verbose_name="permisos", blank=True, related_name='usuarios')

class DocumentoPDF(models.Model):
    titulo = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='pdfs/')
    remitente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='documentos_enviados')
    aprobador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='documentos_aprobados', null=True, blank=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
    @staticmethod
    def obtener_aprobador_aleatorio():
        aprobadores = Usuario.objects.filter(groups__name='Aprobadores')
        return random.choice(aprobadores) if aprobadores else None

