from django.shortcuts import render
from django.views import View
from django.urls import reverse
from .models import Mail
from .forms import MailModelForm
import requests


# Create your views here.
class SendEmailView(View):
	template_name='elo/sendemail.html'
	form_class = MailModelForm
	queryset = Mail.objects.all()

	def get (self, request, *args, **kwargs):
		form = MailModelForm()
		return render(request, self.template_name, {'form': form})

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

class CheckCompanyInfoView(View):
	template_name='checkinfo'
	pass

class CompareCompanyInfoView(View):
	template_name='compare'
	pass

class TagView(View):
	template_name='tag'
	pass

class TaxCalView(View):
	template_name='tax'
	pass

class DaneKupView(View):
	template_name='danekup'
	pass

class OcrView(View):
	template_name='ocr'
	pass

class DownloadView(View):
	template_name='download'
	pass

class UploadView(View):
	template_name='upload'
	pass

class HomeView(View):
	template_name='elo/home.html'
