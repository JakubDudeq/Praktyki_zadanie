Do odpalenia projektu podstawowego wymagany jest pip
0: włączyć pusty cmd
1: pip install requests
2: pip install currencyapicom

Do Wersji rozszerzonej trzeba:
0: włączyć pusty cmd (powinien mieć deafultową ścieżkę C:\Users\{User})
1: pip install fastapi
2: pip install uvicorn
3: cd Desktop
4: cd Waluty
5: uvicorn Wersja_rozszerzona:app --reload

INFO:
1: Nie wiem o co chodzi "W takiej sytuacji, będzie ona zawierać jeden endpoint", który na wejściu będzie przyjmował
następujące parametry:
  input_currency
  output_currencies
  amount
  date

2: Wszystko zajeło mi z 5-6h razem z szukaniem, tak długo bo API i JSONy miałem tylko na JS a routingi na Laravelu więc musiałem całkiem dużo szukać w internecie by to wszystko znaleść i zrobić bo jak wspominałem pythona miałem w szkole troche ale nie jest to główny język jaki mamy + pip mi nie działał przez jakieś 45 minut nie wiem czemu ale już działa.
Ale chyba wszystko jest zrobione całkiem poprawnie.