# Pobieranie wieku od użytkownika
wiek = -5

# Instrukcja warunkowa do klasyfikacji wieku
if wiek < 0:
    print("Wiek nie może być liczbą ujemną. Podaj poprawny wiek.")
elif wiek < 13:
    print("Jesteś dzieckiem.")
elif 13 <= wiek <= 17:
    print("Jesteś nastolatkiem.")
elif 18 <= wiek <= 64:
    print("Jesteś dorosłym.")
else:
    print("Jesteś seniorem.")
