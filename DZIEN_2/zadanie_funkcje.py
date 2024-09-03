def oblicz_srednia(lista_liczb):
    if not lista_liczb:
        return None
    suma = sum(lista_liczb)
    srednia = suma / len(lista_liczb)
    return srednia

def opisz_srednia(srednia, lista_liczb):
    if srednia is None:
        return "Lista jest pusta, nie można obliczyć średniej."
    return f"Średnia z liczb {lista_liczb} wynosi {srednia}"

# Przykładowe testy
liczby1 = [2, 4, 6, 8, 10]
srednia1 = oblicz_srednia(liczby1)
print(opisz_srednia(srednia1, liczby1))  # Średnia z liczb [2, 4, 6, 8, 10] wynosi 6.0

liczby2 = []
srednia2 = oblicz_srednia(liczby2)
print(opisz_srednia(srednia2, liczby2))  # Lista jest pusta, nie można obliczyć średniej.

liczby3 = [-5, 0, 5, 10]
srednia3 = oblicz_srednia(liczby3)
print(opisz_srednia(srednia3, liczby3))  # Średnia z liczb [-5, 0, 5, 10] wynosi 2.5

# liczby4 = [9,4,"trójka"]
# srednia4 = oblicz_srednia(liczby4)
# print(opisz_srednia(srednia4, liczby4))
