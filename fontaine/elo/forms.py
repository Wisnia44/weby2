from django import forms
from .models import Mail

class MailModelForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['recipient',
        	'subject',
            'body'
        	]
