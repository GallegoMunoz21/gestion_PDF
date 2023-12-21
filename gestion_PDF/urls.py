from django.contrib import admin
from django.urls import path, include
from documentos.views import pagina_principal, perfil_usuario, aprobar_documento
from allauth.account.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name='pagina_principal'),
    path('accounts/', include('allauth.urls')),
    path('documentos/', include('documentos.urls')),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
     path('aprobar_documento/<int:documento_id>/', aprobar_documento, name='aprobar_documento'),
]
