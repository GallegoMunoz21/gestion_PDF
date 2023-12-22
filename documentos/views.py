# documentos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import DocumentoPDF
from allauth.account.views import LoginView
from django.shortcuts import render
from .forms import DocumentoPDFForm
from django.contrib.auth import get_user_model
from .models import Usuario
from django.contrib.auth.decorators import user_passes_test
from .models import Documento
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
@login_required
def lista_documentos(request):
    documentos = DocumentoPDF.objects.all()
    return render(request, 'documentos/lista_documentos.html', {'documentos': documentos})


@login_required
def agregar_documento(request):
    if request.method == 'POST':
        form = DocumentoPDFForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            Usuario = get_user_model()
            documento.remitente = Usuario.objects.get(username=request.user.username)
            documento.save()
            return redirect('lista_documentos')
    else:
        form = DocumentoPDFForm()
    return render(request, 'documentos/agregar_documento.html', {'form': form})

@login_required
def eliminar_documento(request, documento_id):
    documento = get_object_or_404(DocumentoPDF, pk=documento_id, remitente=request.user)
    documento.delete()
    return redirect('lista_documentos')

@login_required
def detalle_documento(request, documento_id):
    documento = get_object_or_404(DocumentoPDF, pk=documento_id)
    return render(request, 'documentos/detalle_documento.html', {'documento': documento})

def custom_login_view(request):
    # Tu lógica personalizada aquí
    return render(request, 'registration/login.html')

def pagina_principal(request):
    return render(request, 'documentos/pagina_principal.html')
# Puedes agregar más vistas según sea necesario

@login_required
def perfil_usuario(request):
    return render(request, 'documentos/perfil_usuario.html')  # Ajusta la plantilla según tus necesidades


@user_passes_test(lambda u: u.is_superuser)
def aprobar_documento(request, documento_id):
    documento = get_object_or_404(DocumentoPDF, id=documento_id)

    if not documento.aprobado:
        # Actualizar el estado del documento
        documento.aprobado = True
        documento.aprobado_por = request.user
        documento.save()

        # Redirigir a la nueva plantilla
        return render(request, 'documentos/documento_aprobado.html', {'documento': documento})
    else:
        # Si el documento ya ha sido aprobado, mostrar un mensaje en la misma plantilla
        return render(request, 'documentos/documento_aprobado.html', {'documento': documento, 'ya_aprobado': True})
    
@user_passes_test(lambda u: u.is_superuser)
def documentos_pendientes_aprobacion(request):
    documentos_pendientes = DocumentoPDF.objects.filter(aprobado=False)
    context = {'documentos_pendientes': documentos_pendientes}
    return render(request, 'documentos/documentos_pendientes.html', context)
    

