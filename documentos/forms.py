# documentos/forms.py
from django import forms
from .models import DocumentoPDF

class DocumentoPDFForm(forms.ModelForm):
    class Meta:
        model = DocumentoPDF
        fields = ['titulo', 'archivo', ]
        exclude = ['remitente', 'aprobado', 'aprobador']
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Oculta el campo aprobador para el público
        if 'aprobador' in self.fields:
            self.fields['aprobador'].widget = forms.HiddenInput()


