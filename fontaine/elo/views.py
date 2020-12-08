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
nip1 = ""
regon1 = ""
krs1 = ""
name1 = ""

#dane z ocr
#billtoname1 =  "INTEGRAL GROUP SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ SPÓŁKA KOMANDYTOWA"
#billtovat1 = "7532451385"
#created1 = "2020-11-10 11:26:52"
#number1 =  "FV02312/06/2020"
#total1 = 94.5
billtoname1 = ""
billtovat1 = ""
created1 = ""
number1 =  ""
total1 = 0

#dane z ocr
#description11 = "JAJA SPOŻ. \"L\" (1A)\nSZT"
#price11 = 100
#total11 = 120
#description21 = "HOTEL METRO BOGUSZYN 79B\nSZT."
#price21 = 90
#total21 = 94.5
description11 = ""
price11 = 0
total11 = 0
description21 = ""
price21 = 0
total21 = 0
response_ocr = {}

#dane z checkcompanyinfo

nip2 = ""
krs2 = ""
regon2 = "" 
name2 = ""
check_result = ""

#dane z tax
tax = 4.5

#dane do emaila

#dane z tags
tag_list=""
#dane z tax
tax1=""
tax2=""
#dane z danekup
nipd=""
addressd=""
named=""


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

class TagView(View):
	template_name='elo/tag.html'
	form_class = TagModelForm
	queryset = Tag.objects.all()

	def post(self, request, *args, **kwargs):
		global tag_list
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
		response_json = response.json()
		response_dict = json.loads(response_json)
		tag_list="Tagi: "
		for i in response_dict:
			tag_list+=str(i)
			tag_list+=", "
		return HttpResponseRedirect(reverse('tag'))

	def get(self, request, *args, **kwargs):
		my_context = {}
		my_context["tag"] = tag_list
		return render(request, self.template_name, my_context) 

class TaxCalView(View):
	template_name='elo/tax.html'
	form_class = TaxModelForm
	queryset = Tax.objects.all()
	def post(self, request, *args, **kwargs):
		global tax1,tax2
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
		response_json = response.json()
		response_dict = json.loads(response_json)
		tax1 = response_dict[description11]
		tax2 = response_dict[description21]
		return HttpResponseRedirect(reverse('tax'))

	def get(self, request, *args, **kwargs):
		my_context = {}
		my_context["desc1"] = description11+": "
		my_context["tax1"] = tax1
		my_context["desc2"] = description21+": "
		my_context["tax2"] = tax2
		return render(request, self.template_name, my_context) 

class DaneKupView(FormView):
	template_name='elo/danekup.html'
	form_class = DanekModelForm
	queryset = Danek.objects.all()

	def post(self, request, *args, **kwargs):
		global nipd, named, addressd
		nip = nip1
		name = name1
		address = "http://dane_kup:33306/vendorinfo"
		data = response_ocr
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)
		response_json = response.json()
		response_dict = json.loads(response_json)
		nipd=response_dict["nip"]
		named=response_dict["name"]
		addressd=response_dict["address"]
		dane_check = requests.get(address)
		return HttpResponseRedirect(reverse('danekup'))

	def get(self, request, *args, **kwargs):
		my_context = {}
		my_context["nip"] = nipd
		my_context["name"] = named
		my_context["address"] = addressd
		my_context["ocr"] = response_ocr
		return render(request, self.template_name, my_context) 

class OcrView(FormView):
	template_name='elo/ocr.html'
	form_class = OcrModelForm
	queryset = Ocr.objects.all()
	
	def post(self, request, *args, **kwargs):
		global nip1, regon1, krs1, name1, billtoname1, billtovat1, number1, total1
		global description11, price11, price21, total11, total21, description21
		global response_ocr
		
		address = "http://ocr:33305/ocr"
		data = {"url":"https://drive.google.com/u/0/uc?id=1NQ4M5o-REBVzyfSyuV9ywSVXdN98Ce94&export=download"}
		data_json = json.dumps(data)
		response = requests.post(address, json=data_json)
		
		response_json = response.json()
		response_dict = json.loads(response_json)
		response_dict = response_dict["response"]
		response_ocr = response_dict

		nip1 = response_dict["vat_number"]
		regon1 = "38203259600000"
		krs1 = "0000762310"
		name1 = response_dict["vendor"]["name"]
		billtoname1 = response_dict['vendor']['name']
		billtovat1 = response_dict["bill_to_vat_number"]
		number1 = response_dict["invoice_number"]
		total1 = response_dict["total"]
		
		total11 = response_dict["line_items"][0]["total"]
		description11 = response_dict["line_items"][0]["description"]
		price11 = response_dict["line_items"][0]["price"]
		total21 = response_dict["line_items"][1]["total"]
		description21 = response_dict["line_items"][1]["description"]
		price21 = response_dict["line_items"][1]["price"]
		
		return HttpResponseRedirect(reverse('ocr'))

	def get(self, request, *args, **kwargs):
		my_context = {}
		my_context["ocr"] = response_ocr
		return render(request, self.template_name, my_context) 

class DownloadView(View):
	template_name='download'
	pass

class UploadView(View):
	template_name='upload'
	pass

class HomeView(View):
	template_name='elo/home.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {}) 
