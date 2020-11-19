# Mikroserwis RestAPI do sprawdzenia informacji o firmie

autor: Tomasz Wiśniewski

Program korzysta z API dostępnego pod adresem https://wl-api.mf.gov.pl/api/.

**Instrukcja instalacji:**

1. Sklonuj repozytorium za pomocą polecenia: `$git clone https://github.com/Wisnia44/checkcompanyinfo.git`;
2. Przejdź do katalogu checkcompanyinfo: `$cd checkcompanyinfo`;
3. Upewnij się, że jesteś w katalogu checkcompanyinfo: `$pwd`;
4. Zbuduj obraz dockera: `$docker build -t checkcompanyinfo .`;
5. Uruchom kontener: `$docker-compose up`;
6. Serwer jest uruchomiony!


**Instrukcja użycia:**

Pod adres `http://0.0.0.0:33303/check/{nr nip}` wysyłamy zapytanie metodą GET.

W odpowiedzi powinniśmy dostać podobnego jsona:

```
{
    "regon": "930959027",
    "krs": "0000305240",
    "name": "ARTIM SAFETY KRZYSZTOF NIEŚCIOR SPÓŁKA JAWNA"
}
```

Przykładowo kod w Pythonie wysyłający takie zapytanie wygląda następująco:
```
import requests

address = "http://0.0.0.0:33303/check/9121480498"
response = requests.get(address)
print(response.content)
```
