from django import forms
<<<<<<< HEAD
from .models import Mail, Ocr
=======
from .models import Mail, Check
>>>>>>> 4a6afaeab0764dbb31e5a856eb52482b01ecbee0

class MailModelForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['recipient',
        	'subject',
            'body'
        	]

<<<<<<< HEAD
class OcrModelForm(forms.ModelForm):
    class Meta:
        model = Ocr
        fields = ['nip',
        	'regon',
            'krs'
        	]

=======
class CheckModelForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['nip']
>>>>>>> 4a6afaeab0764dbb31e5a856eb52482b01ecbee0
