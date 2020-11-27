from django import forms
from .models import Mail, Ocr

class MailModelForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['recipient',
        	'subject',
            'body'
        	]

class OcrModelForm(forms.ModelForm):
    class Meta:
        model = Ocr
        fields = ['nip',
        	'regon',
            'krs'
        	]

