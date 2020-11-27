import requests
import json
import time
time.sleep(10)
"""
#send request to comparecompanyinfo
address1 = "http://comparecompanyinfo:33301/companyinfocorectness"
data1 = {
    "nip1": "9121480498",
    "krs1": "0000305240",
    "name1": "ARTIM SAFETY KRZYSZTOF NIEŚCIOR SPÓŁKA JAWNA",
    "regon1": "930959027",
    "nip2": "9121480498",
    "krs2": "0000305240",
    "name2": "ARTIM SAFETY KRZYSZTOF NIEŚCIOR SPÓŁKA JAWNA",
    "regon2": "930959027"
}
data1_json = json.dumps(data1)
response1 = requests.post(address1, json=data1_json)
#print(response1.content)

#send request to sendemail
address2 = "http://sendemail:33302/sendemail"
data2 = {
	"recipient": "martfab@tutanota.com",
	"subject": "Temat maila",
	"body": "Tresc maila"
}
data2_json = json.dumps(data2)
response2 = requests.post(address2, json=data2_json)
url = "http://localhost:44355/api/files/test.pdf"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)print(response2.content)

#send request to checkcompanyinfo
address3 = "http://checkcompanyinfo:33303/check/9121480498"
response3 = requests.get(address3)
#print(response3.content)

#send request to ocr
address4 = "http://ocr:33305/ocr"
data4 = {"url":"https://drive.google.com/u/0/uc?id=11MDp5YpGtNKgja5LhPBz_SQs6HkMIXLY&export=download"}
data4_json = json.dumps(data4)
#response4 = requests.post(address4, json=data4_json)
#print(response4.content)

#send request to Dane_kup
address5 = "http://dane_kup:33306/vendorinfo"
data5 = {
    'vat_number':'9121480498',
    "vendor": {
        "address": "polna 2",
        "category": "",
        "email": "biuro@jajcarz.com",
        "fax_number": "123456789",
        "name": "Integral Group Sp.k. Sp. Z O.o.",
        "phone_number": "680500 700",
        "raw_name": "integral Group Sp.k. Sp. z o.o.",
        "vendor_logo": "https://cdn.veryfi.com/logos/tmp/007614202.png",
        "vendor_reg_number": "123456789",
        "vendor_type": "",
        "web": ""
    }
}
data5_json = json.dumps(data5)
response5 = requests.post(address5, json=data5_json)
#print(response5.content)

#send request to tag
address6 = "http://tag:33307/tags"
data6 = {   
    "bill_to_name": "INTEGRAL GROUP SPÓŁKA Z OGRANICZONĄ",
    "bill_to_vat_number": "7532451385",
    "created": "2020-11-10 11:26:52",
    "invoice_number": "FV02312/06/2020",
    "total": 94.5
}
data6_json = json.dumps(data6)
response6 = requests.post(address6, json=data6_json)
#print(response6.content)

#send request to tax_cal
address7 = "http://tax_cal:33308/taxcal"
data7 = {"line_items": [
    {
      "date": "",
      "description": "JAJA SPOŻ. \"L\" (1A)\nSZT",
      "discount": 0,
      "id": 28123638,
      "order": 0,
      "price": 100,
      "quantity": 300,
      "reference": "",
      "sku": "01.47.21.0",
      "tax": 4.5,
      "tax_rate": 5,
      "total": 120,
      "type": "product",
      "unit_of_measure": ""
    },
    {
      "date": "",
      "description": "HOTEL METRO BOGUSZYN 79B\nSZT.",
      "discount": 0,
      "id": 28123639,
      "order": 1,
      "price": 90,
      "quantity": 1,
      "reference": "",
      "sku": "",
      "tax": 0,
      "tax_rate": 0,
      "total": 94.5,
      "type": "service",
      "unit_of_measure": ""
    }
  ]}
data7_json = json.dumps(data7)
response7 = requests.post(address7, json=data7_json)
#print(response7.content)
"""
#send request to download
address8 = "http://weby2_fileswebdepot_1:33309/api/files/test.pdf"
payload8={}
headers8 = {}
response8 = requests.request("GET", address8, headers=headers8, data=payload8)
print(response8.text)

#send request to upload
"""address9 = "http://fileswebdepot:33309/api/files"
payload9={}
files9=[
  ('file',('test.pdf',open('./client/test.pdf','rb'),'application/pdf'))
]
headers9 = {}
response9 = requests.request("POST", address9, headers=headers9, data=payload9, files=files9)
print(response9.text)
"""
while True: 
  pass
print("blalal") 