from procesor import ProcesorPlatnosci

class PlatnoscKartaKredytowa(ProcesorPlatnosci):
    def autoryzuj(self):
        print("Autoryzacja karty kredytowej")

    def przetworz_platnosc(self, kwota):
        print(f"Przetwarzanie płatności kartą kredytową: {kwota} PLN")
