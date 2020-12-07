from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.views.generic.edit import FormView
from .models import Mail, Check, Ocr, Compare, Tag, Tax, Danek
from .forms import MailModelForm, CheckModelForm, OcrModelForm, CompareModelForm, TagModelForm, TaxModelForm, DanekModelForm
import json
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect

#dane z ocr
nip1 = "7532451385"
regon1 = "xd"
krs1 = "hehe"
name1 = "elo"

#dane z ocr
billtoname1 =  "INTEGRAL GROUP SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ SPÓŁKA KOMANDYTOWA"
billtovat1 = "7532451385"
created1 = "2020-11-10 11:26:52"
number1 =  "FV02312/06/2020"
total1 = 94.5

#dane z ocr
description11 = "JAJA SPOŻ. \"L\" (1A)\nSZT"
price11 = 100
total11 = 120
description21 = "HOTEL METRO BOGUSZYN 79B\nSZT."
price21 = 90
total21 = 94.5

#dane z checkcompanyinfo
krs2 = ""
regon2 = "" 
name2 = ""
check_result = ""

#dane z tax
tax = 4.5

#dane do emaila


# Create your views here.
class SendEmailView(FormView):
	template_name='elo/sendemail.html'
	form_class = MailModelForm
	queryset = Mail.objects.all()

	def form_valid(self, form):
		recipient = form.cleaned_data['recipient']
		subject = "Informacje o firmie: "+ str(name1)
		body = "Dane firmy: " + "nip: " + str(nip1) + ";" + " regon: " + str(regon1) + ";" + " krs: " + str(krs1) + ";" + " Sprawdzenie danych: " + str(check_result) + ";" + " VAT z faktury dla: " + str(description11) + " to: "+ str(tax) 
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
		return reverse('sendemail')

class CheckCompanyInfoView(View):
	template_name='elo/checkinfo.html'
	form_class = CheckModelForm
	queryset = Check.objects.all()
		
	def post(self, request, *args, **kwargs):
		global nip1, krs2, regon2, name2
		address = "http://checkcompanyinfo:33303/check/" + nip1
		dane_check = requests.get(address)
		dane_check_json = dane_check.json()
		dane_check_dict = json.loads(dane_check_json)
		krs2 = dane_check_dict["krs"]
		regon2 = dane_check_dict["regon"]
		name2 = dane_check_dict["name"]
		return HttpResponseRedirect(reverse('checkinfo'))

	def get(self, request, *args, **kwargs):
		my_context = {}
		my_context["krs"] = krs2
		my_context["regon"] = regon2
		my_context["name"] = name2
		return render(request, self.template_name, my_context) 
		

class CompareCompanyInfoView(FormView):
	template_name='elo/compare.html'
	form_class = CompareModelForm
	queryset = Compare.objects.all()
	
	def post(self, request, *args, **kwargs):
		global check_result
		address = "http://comparecompanyinfo:33301/companyinfocorectness"
		data = {
    		"nip1": nip1,
    		"krs1": krs1,
    		"name1": name1,
    		"regon1": regon1,
    		"nip2": nip1,
    		"krs2": krs2,
    		"name2": name2,
    		"regon2": regon2
		}
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)
		response_json = response.json()
		response_dict = json.loads(response_json)
		check_result = response_dict["response"]
		return HttpResponseRedirect(reverse('compare'))

	def get(self, request, *args, **kwargs):
		my_context = {}
		my_context["nip1"] = nip1
		my_context["krs1"] = krs1
		my_context["regon1"] = regon1
		my_context["name1"] = name1
		my_context["nip2"] = nip1
		my_context["krs2"] = krs2
		my_context["regon2"] = regon2
		my_context["name2"] = name2
		my_context["check_result"] = check_result
		return render(request, self.template_name, my_context) 

class TagView(FormView):
	template_name='elo/tag.html'
	form_class = TagModelForm
	queryset = Tag.objects.all()

	def form_valid(self, form):
		#billtoname = form.cleaned_data['billtoname']
		#billtovat = form.cleaned_data['billtovat']
		#created = form.cleaned_data['created']
		#number = form.cleaned_data['number']
		#total = form.cleaned_data['total']
		billtoname = billtoname1
		billtovat = billtovat1
		created = created1
		number = number1
		total = total1
		address = "http://tag:33307/tags"

		data = {   
    		"bill_to_name": billtoname,
    		"bill_to_vat_number": billtovat,
    		"created": created,
    		"invoice_number": number,
    		"total": total
		}
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('home')

class TaxCalView(FormView):
	template_name='elo/tax.html'
	form_class = TaxModelForm
	queryset = Tax.objects.all()
	def form_valid(self, form):
		#description_1 = form.cleaned_data['description1']
		#price_1 = form.cleaned_data['price1']
		#total_1 = form.cleaned_data['total1']
		#description_2 = form.cleaned_data['description2']
		#price_2 = form.cleaned_data['price2']
		#total_2 = form.cleaned_data['total2']
		description_1 = description11
		price_1 = price11
		total_1 = total11
		description_2 = description21
		price_2 = price21
		total_2 = total21

		address = "http://tax_cal:33308/taxcal"
		data = {"line_items": [
   		 {
      		"description": description_1,
     		"price": price_1,
      		"total": total_1,
			  },
   		{
			"description": description_2,
			"price": price_2,
			"total": total_2
			}
		]}
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('home')

class DaneKupView(FormView):
	template_name='elo/danekup.html'
	form_class = DanekModelForm
	queryset = Danek.objects.all()

	def form_valid(self, form):
		#nip = form.cleaned_data['nip']
		#name = form.cleaned_data['name']
		nip =nip1
		name = name1
		address = "http://dane_kup:33306/vendorinfo"

		data = {
    		'vat_number':nip,
    			"vendor": {
       			"address": "polna 2",
        		"category": "",
        		"email": "biuro@jajcarz.com",
        		"fax_number": "123456789",
        		"name": name,
        		"phone_number": "680500 700",
        		"raw_name": "integral Group Sp.k. Sp. z o.o.",
        		"vendor_logo": "https://cdn.veryfi.com/logos/tmp/007614202.png",
        		"vendor_reg_number": "123456789",
        		"vendor_type": "",
        		"web": ""
   				}
		   	}
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)
		dane_check = requests.get(address)
		print(dane_check)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('home')

class OcrView(FormView):
	template_name='elo/ocr.html'
	form_class = OcrModelForm
	queryset = Ocr.objects.all()
	def form_valid(self, form):
		nip = form.cleaned_data["nip"]
		regon = form.cleaned_data["regon"]
		krs = form.cleaned_data["krs"]
		name = form.cleaned_data["name"]
		address = "http://ocr:33305/ocr"
		data = {"url":"https://drive.google.com/u/0/uc?id=11MDp5YpGtNKgja5LhPBz_SQs6HkMIXLY&export=download"}
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)
		dane_check = requests.get(address)
		print(dane_check)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('home')

class DownloadView(View):
	template_name='download'
	pass

class UploadView(View):
	template_name='upload'
	pass

class HomeView(View):
	template_name='elo/home.html'
