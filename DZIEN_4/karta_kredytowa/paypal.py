from procesor import ProcesorPlatnosci

class PaltnoscPayPal(ProcesorPlatnosci):
    def autoryzuj(self):
        print("Logowanie do konta PayPal")

    def przetworz_platnosc(self, kwota):
        print(f"Przetwarzanie płatności PayPal: {kwota} PLN")
