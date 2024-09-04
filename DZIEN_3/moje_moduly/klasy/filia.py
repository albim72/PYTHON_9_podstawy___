from funkcje.bfunkcje import czytaj_slownik

class Filia:
    def __init__(self,nr,nazwa,adres):
        self.nr = nr
        self.nazwa = nazwa
        self.adres = adres
        
    def promocja(self,book):
        return f"promocja książki: {czytaj_slownik(book)}"
