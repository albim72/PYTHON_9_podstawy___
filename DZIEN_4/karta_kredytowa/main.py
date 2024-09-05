from karta import PlatnoscKartaKredytowa
from paypal import PaltnoscPayPal
from procesor import ProcesorPlatnosci

kwota_zakupu = 193
kwota_uslugi = 212.88

#funkcja opisująca przetwarzanie płatności
def dokonaj_platnosci(procesor_platnosci:ProcesorPlatnosci,kwota:float):
    print("_____ otwarcie płatności ____")
    procesor_platnosci.autoryzuj()
    procesor_platnosci.przetworz_platnosc(kwota)

#płatnośc za zakupy kartą kredytową
platnosc_karta = PlatnoscKartaKredytowa()
dokonaj_platnosci(platnosc_karta,kwota_zakupu)

print("\n")

#płatnosc paypal za usługi
platnosc_paypal = PaltnoscPayPal()
dokonaj_platnosci(platnosc_paypal,kwota_uslugi)
