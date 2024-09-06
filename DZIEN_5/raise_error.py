def tylko_liczby_dodatnie(liczba):
    if liczba < 0:
        raise ValueError("Liczba powinna byc nieujemna!")
    else:
        print(f"liczba jest nieujemna i wynosi: {liczba}")

try:
    nb = int(input("podaj wartośc całkowitą dodatnią lub 0: "))
    tylko_liczby_dodatnie(nb)
except ValueError as ve:
    print(f"wystapił błąd: {ve}")

print("*"*50)

def podaj_miasto(miasto):
    if miasto == "Warszawa":
        raise ValueError("Warszawa jest stolicą! Podaj miasto które nie jest stolicą państwa")
    return f"Twoje miasto to {miasto}"

try:
    i = input("podaj nazwę miasta, które nie jest stolicą Polski.... ")
    print(podaj_miasto(i))
except ValueError as v:
    print(v)

