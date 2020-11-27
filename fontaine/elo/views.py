from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.views.generic.edit import FormView
from .models import Mail, Check
from .forms import MailModelForm, CheckModelForm
import requests
import json


body = ""

nip = ""

# Create your views here.
class SendEmailView(FormView):
	template_name='elo/sendemail.html'
	form_class = MailModelForm
	queryset = Mail.objects.all()

	def form_valid(self, form):
		recipient = form.cleaned_data['recipient']
		subject = form.cleaned_data['subject']
		body = form.cleaned_data['body']
		address = "http://sendemail:33302/sendemail"
		data = {
			"recipient": recipient,
			"subject": subject,
			"body": body
		}
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('home')

class CheckCompanyInfoView(FormView):
	template_name='elo/checkinfo.html'
	form_class = CheckModelForm
	queryset = Check.objects.all()
	
	def form_valid(self, form):
		nip = form.cleaned_data["nip"]
		print(nip)
		address = "http://checkcompanyinfo:33303/check/" + nip
		print(address)
		dane_check = requests.get(address)
		print(dane_check)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('home')

class CompareCompanyInfoView(View):
	template_name='elo/compare'
	pass

class TagView(View):
	template_name='elo/tag'
	pass

class TaxCalView(View):
	template_name='elo/tax'
	pass

class DaneKupView(View):
	template_name='elo/danekup'
	pass

class OcrView(View):
	def ocr(self):
		template_name='elo/ocr'
		address = "http://ocr:33305/ocr"
		data = {"url":"https://drive.google.com/u/0/uc?id=11MDp5YpGtNKgja5LhPBz_SQs6HkMIXLY&export=download"}
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)

	

class DownloadView(View):
	template_name='download'
	pass

class UploadView(View):
	template_name='upload'
	pass

class HomeView(View):
	template_name='elo/home.html'
