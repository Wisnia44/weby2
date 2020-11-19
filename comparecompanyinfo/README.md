# Mikroserwis RestAPI do porównywania danych o firmie z 2 źródeł

autor: Tomasz Wiśniewski

**Instrukcja instalacji:**

1. Sklonuj repozytorium za pomocą polecenia: `$git clone https://github.com/Wisnia44/comparecompanyinfo.git`;
2. Przejdź do katalogu comparecompanyinfo: `$cd comparecompanyinfo`;
3. Upewnij się, że jesteś w katalogu comparecompanyinfo: `$pwd`;
4. Zbuduj obraz dockera: `$docker build -t comparecompanyinfo .`;
5. Uruchom kontener: `$docker-compose up`;
6. Serwer jest uruchomiony!


**Instrukcja użycia:**

Pod adres `http://0.0.0.0:33301/companyinfocorectness` wysyłamy zapytanie metodą POST o części body w formacie json o zadanej strukturze:

```
{
    "nip1": "<nip firmy z źródła A>",
    "krs1": "<numer wpisu do krs firmy z źródła A>",
    "name1": "<nazwa firmy z źródła A>",
    "regon1": "<regon firmy z źródła A>",
    "nip2": "<nip firmy z źródła B>",
    "krs2": "<numer wpisu do krs firmy z źródła B>",
    "name2": "<nazwa firmy z źródła B>",
    "regon2": "<regon firmy z źródła B>"
}
```

W odpowiedzi powinniśmy otrzymać podobnego jsona:

```
{
    "response": "True"
}
```

Przykładowo kod w Pythonie wysyłający takie zapytanie wygląda następująco:
```
import requests
import json

address = "http://0.0.0.0:33301/companyinfocorectness"
data = {
    "nip1": "9121480498",
    "krs1": "0000305240",
    "name1": "ARTIM SAFETY KRZYSZTOF NIEŚCIOR SPÓŁKA JAWNA",
    "regon1": "930959027",
    "nip2": "9121480498",
    "krs2": "0000305240",
    "name2": "ARTIM SAFETY KRZYSZTOF NIEŚCIOR SPÓŁKA JAWNA",
    "regon2": "930959027"
}
data_json = json.dumps(data)
response = requests.post(address, json=data_json)
print(response.content)
```
