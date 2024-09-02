"""
Utworzenie listy kolorów

    Utwórz listę o nazwie kolory zawierającą 7 kolorów.
    Wydrukuj listę kolory.

Modyfikacje listy kolorów

    Dodaj nowy kolor na końcu listy.
    Dodaj nowy kolor na początku listy.
    Usuń trzeci kolor z listy.
    Zmień wartość ostatniego koloru na inny kolor.
    Wydrukuj zmodyfikowaną listę.

"""
# 1. Utworzenie listy z 7 kolorami
kolory = ["czerwony", "zielony", "niebieski", "żółty", "czarny", "biały", "fioletowy"]
print("Początkowa lista kolorów:", kolory)

# 2. Dodanie nowego koloru na końcu listy
kolory.append("pomarańczowy")
print("Po dodaniu koloru na końcu:", kolory)

# 3. Dodanie nowego koloru na początku listy
kolory.insert(0, "różowy")
print("Po dodaniu koloru na początku:", kolory)

# 4. Usunięcie trzeciego koloru z listy
del kolory[2]
print("Po usunięciu trzeciego koloru:", kolory)

# 5. Zmiana wartości ostatniego koloru na inny kolor
kolory[-1] = "brązowy"
print("Po zmianie ostatniego koloru:", kolory)
