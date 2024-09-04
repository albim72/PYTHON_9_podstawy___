class Osoba:
    #uzupełnij według zadania
    pass

class Sportowiec:
    # uzupełnij według zadania
    pass

class Zawodnik(Osoba,Sportowiec):
    #zmodyfikuj konstrukotr żeby był spójny z dziedziczeniem - zgodnie z treścią zadania
    def __init__(self, imie, nazwisko, dyscyplina, wynik):
        self.imie = imie
        self.nazwisko = nazwisko
        self.dyscyplina = dyscyplina
        self.wynik = wynik

    def przedstaw_siebie(self):
        return f"{self.imie} {self.nazwisko}, dyscyplina: {self.dyscyplina}, wynik: {self.wynik}"

# Tworzenie dwóch obiektów klasy Zawodnik
zawodnik1 = Zawodnik("Anna", "Kowalska", "Lekkoatletyka", 12.34)
zawodnik2 = Zawodnik("Jan", "Nowak", "Pływanie", 54.21)

# Wyświetlanie przedstawień zawodników
print(zawodnik1.przedstaw_siebie())
print(zawodnik2.przedstaw_siebie())
