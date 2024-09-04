class LadowyPojazd:
    def __init__(self,liczba_kol):
        self.liczna_kol = liczba_kol

    def jedz(self):
        return f"jedzie po lądzie na {self.liczna_kol} kołach"


class WodnyPojazd:
    def __init__(self, typ_silnika):
        self.typ_silnika = typ_silnika

    def plywaj(self):
        return f"pływa po wodzie używając {self.typ_silnika}."

class Amfibia(LadowyPojazd,WodnyPojazd):
    def __init__(self, liczba_kol, typ_silnika):
        LadowyPojazd.__init__(self,liczba_kol)
        WodnyPojazd.__init__(self,typ_silnika)

    def przemieszczaj_sie(self):
        return f"{self.jedz()}, {self.plywaj()}"

#przykładowe użycie
amfibia = Amfibia(4,"silnika spalinowego")
print(amfibia.przemieszczaj_sie())
