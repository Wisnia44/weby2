# Mikroserwis RestAPI do wysyłania emaila

autor: Tomasz Wiśniewski

**Instrukcja instalacji:**

1. Sklonuj repozytorium za pomocą polecenia: `$git clone https://github.com/Wisnia44/sendemail.git`;
2. Przejdź do katalogu sendemail: `$cd sendemail`;
3. Poproś autora o hasło do skrzynki Gmail i wklej je w linii `12` pliku `server.py`;
4. Zbuduj obraz dockera: `$docker build -t sendemail .`;
5. Uruchom kontener: `$docker-compose up`;
6. Serwer jest uruchomiony!


**Instrukcja użycia:**

Pod adres `http://0.0.0.0:33302/sendemail` wysyłamy zapytanie metodą POST o części body w formacie json o zadanej strukturze:

```
{
	"recipient": "<adres email adresata>",
	"subject": "<tytuł wiadomości>",
	"body": "<treść wiadomości>"
}
```

Aby przetestować działanie możesz wysłać maila do samego siebie.

Przykładowo kod w Pythonie wysyłający takie zapytanie wygląda następująco:
```
import requests
import json

address = "http://0.0.0.0:33302/sendemail"
data = {
	"recipient": "<<twoj adres email>>",
	"subject": "Temat maila",
	"body": "Tresc maila"
}
data_json = json.dumps(data)
response = requests.post(address, json=data_json)
print(response.content)
```
