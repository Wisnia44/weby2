from django import forms
from .models import Mail, Ocr, Check, Compare, Tag, Tax, Danek

class MailModelForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['recipient'
        #,
        	#'subject',
            #'body'
        	]

class OcrModelForm(forms.ModelForm):
    class Meta:
        model = Ocr
        fields = ['nip',
        	'regon',
            'krs',
            'name'
        	]

class CheckModelForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['nip']

class CompareModelForm(forms.ModelForm):
    class Meta:
        model = Compare
        fields = ['nip1',
        	'regon1',
            'krs1',
            'name1',
            'nip2',
        	'regon2',
            'krs2',
            'name2',
        	]

class TagModelForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['billtoname',
        	'billtovat',
            'created',
            'number',
            'total'
        	]

class TaxModelForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = ['description1',
        	'price1',
            'total1',
            'description2',
            'price2',
            'total2'
        	]
class DanekModelForm(forms.ModelForm):
    class Meta:
        model = Danek
        fields = ['nip',
        	'name'
            ]
