# flask_app
Flask application, implementing an artificial neural network that calculates CRF indicators

![photo](logoprojekt.ico)
# WSTĘP (cel aplikacyjny)
**Ocena zagrożenia zawałowego <br>
dla polskich kopalń rud miedzi** <br>
*z wykorzystaniem Sztucznych Sieci Neuronowych*

# APLIKACJA 
#### (wersja alfa)

Założeniem opracowania aplikacji desktopowej (`/d-jus/APP`), była obsługa aplikacji przez jednego pracownika, na jednym stanowisku pracy. Dane (wyniki prognoz) były zapisywane w pliku tekstowym lub pliku bazy bez serwerowej. Głównymi ograniczeniami tego rozwiązania (wynikającego z słabego wsparcia tworzenia apek desktopowych w Python), brak możliwości tworzenia kont użytkownika, ograniczony dostęp do bazy, centralna baza danych o ograniczonym dostępie, łatwość do wprowadzania zmian w kodzie aplikacji. Dlatego opracowano w maju 2023 r. (wersja alfa) implementację SSN w środowisku Flask, co umożliwia uruchomienie serwer w kontenerze Docker oraz dostęp do aplikacji webowej z sieci lokalnej. 
<br>
**Cechy wersji alfa**<br>
- dostęp poprzez sieć lokalną do serwera Flask,
- osadzenie aplikacji w kontenerze Docker,
- możliwość zdefiniowania parametrów uruchomienia serwera (Test, Developing, itp.),
- bezpieczne połączenia z serwerem,
- walidacja formularze,
- i wiele innych ...