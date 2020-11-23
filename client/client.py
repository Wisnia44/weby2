import requests
import json

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
print(response1.content)

#send request to sendemail
address2 = "http://sendemail:33302/sendemail"
data2 = {
	"recipient": "tttttttttttttt7@gmail.com",
	"subject": "Temat maila",
	"body": "Tresc maila"
}
data2_json = json.dumps(data2)
response2 = requests.post(address2, json=data2_json)
print(response2.content)

#send request to checkcompanyinfo
address3 = "http://checkcompanyinfo:33303/check/9121480498"
response3 = requests.get(address3)
print(response3.content)

#send request to ocr
address4 = "http://ocr:33305/ocr"
data4 = {"url":"https://drive.google.com/u/0/uc?id=11MDp5YpGtNKgja5LhPBz_SQs6HkMIXLY&export=download"}
data4_json = json.dumps(data4)
response4 = requests.post(address4, json=data4_json)
print(response4.content)
