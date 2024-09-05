class Zwierze:
    """Klasa reprezentująca zwierzę"""

    # każdy argument metody ma jedną spację po przecinku
    def __init__(self, imie, wiek, gatunek):
        self.imie = imie
        self.wiek = wiek
        self.gatunek = gatunek

    # Metody powinny byc oddzielone pustą linią
    def przedstaw_sie(self):
        """Wypisuje informacje o zwierzęciu"""
        print(f"Jestem {self.imie}, mam {self.wiek} lat, jestem {self.gatunek}")
