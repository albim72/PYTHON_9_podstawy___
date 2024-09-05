print("podaj swoje imię: ")
imie = input()
print(f"Witaj! {imie}")
print("_"*50)
wiek = input("Podaj wiek: ")
print(f"Użytkownik {imie}, wiek: {wiek} lat")
koszt = int(input("Podaj kwotę zakupów: "))
def rabat(kwota,procent):
    if kwota >= 1000:
        return kwota*(100-procent)/100
    else:
        return kwota

print(f"kwota do zapłaty: {rabat(koszt,15)}")

