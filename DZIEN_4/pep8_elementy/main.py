# pierszy blok - importy standardowe
import os
import sys

# drugi blok - biblioteki zewnętrzne
import requests

# trzeci blok - biblioteki wewnętrzne(własne)
from klasa import Zwierze
from funkcja import przywitaj_program


# stała powinna byc pisana wielkimi literami
MAKSYMALNY_WIEK = 20


# funckje,parametry i zmienne - małe litery z podkreślnikami
def oblicz_wiek_lata_zwierze(wiek, lata):
    """Oblicz wiek zwierzęcia w przyszłych latach"""
    return wiek + lata


if __name__ == '__main__':
    moj_pies = Zwierze(imie="Ludvik", wiek=3, gatunek="pies")

    # wywołanie funckji
    moj_pies.przedstaw_sie()

    # Zgodnie z pep8 odstępy wokół operatorów są zalecane
    przyszly_wiek = oblicz_wiek_lata_zwierze(wiek=moj_pies.wiek, lata=2)
    print(f"za 2 lata {moj_pies.imie} będzie miał {przyszly_wiek} lat")
