from django.urls import path
from .views import lista_documentos, detalle_documento, custom_login_view, pagina_principal, agregar_documento, eliminar_documento
from .models import Usuario
urlpatterns = [
     path('', pagina_principal, name='pagina_principal'),  # Agrega esta línea para manejar la URL raíz
    path('lista/', lista_documentos, name='lista_documentos'),
     path('agregar/', agregar_documento, name='agregar_documento'),
    path('eliminar/<int:documento_id>/', eliminar_documento, name='eliminar_documento'),
    path('<int:documento_id>/', detalle_documento, name='detalle_documento'),
    path('login/', custom_login_view, name='custom_login_view'),
    path('pagina_principal/', pagina_principal, name='pagina_principal'),
    
    # Puedes agregar más patrones de URL según sea necesario
]
