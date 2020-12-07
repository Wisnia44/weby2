# FilesWebDepot

## Instrukcja uruchamiania dockera

1. Sklonować repozytorium `https://github.com/paulinach98/FilesWebDepot.git`
2. Wejść w główny folder repozytorium za pomocą np. konsoli PowerShell.
3. Uruchomić: `docker-compose build`
4. Uruchomić `docker-compose up`

## Pobieranie pliku

Zapytanie GET wysłane na adres `http://localhost:44355/api/files/{nazwa_pliku}` powinno zwrócić nam plik. Jeżeli nie jest to prosty plik tekstowy to należy go zapisać.

Przykładowy kod w języku Python wykonujący zapytanie o plik `test.pdf`:

```py
import requests

url = "http://localhost:44355/api/files/test.pdf"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

## Wysyłanie pliku

Plik możemy wrzucić za pomocą zapytania POST wysłanego pod adres `http://localhost:44355/api/files`.

Przykładowy kod w języku Python wysyłający plik `test.pdf` ze ścieżki `/C:/Users/<user_name>/Desktop/test.pdf`:

```python
import requests

url = "http://localhost:44355/api/files"

payload={}
files=[
  ('file',('test.pdf',open('/C:/Users/<user_name>/Desktop/test.pdf','rb'),'application/pdf'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

W odpowiedzi otrzymujemy nazwę pod jaką został zapisany plik na serwerze. Można jej potem użyć do pobrania pliku za pomocą GETa.

## Rozwiązywanie problemów

### Ports are not available

Zmień port 44355 w pliku `docker-compose-override.yml` na jakiś inny i spróbuj ponownie. Prawdopodobnie jakaś aplikacja (może jakiś kontener) korzysta już z tego portu.
