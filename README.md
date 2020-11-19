# Aplikacja złożona z 3 mikroserwisów i ich klienta

**Instrukcja instalacji i użycia:**

1. Sklonuj repozytorium za pomocą polecenia: `$git clone https://github.com/Wisnia44/weby2.git`;
2. Przejdź do katalogu weby2: `$cd weby2`;
3. Poproś autora o hasło do skrzynki Gmail i wklej je w linii `12` pliku `sendemail/server.py`;
4. Wpisz swój adres email w linii `23` pliku `client/client.py`;
5. Zbuduj obraz dockera: `$docker-compose build`;
6. Uruchom kontener: `$docker-compose up`;
7. Serwer jest uruchomiony, a klient wysyła po jednym zapytaniu do każdego mikroserwisu!
