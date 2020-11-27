from django import forms
from .models import Mail, Check

class MailModelForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['recipient',
        	'subject',
            'body'
        	]

class CheckModelForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['nip']
