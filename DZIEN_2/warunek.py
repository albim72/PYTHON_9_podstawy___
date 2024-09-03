#instrukcje warunkowe w języku python

#przykład 1

print("\n________ przykład 1_________")
liczba = 10
if liczba > 0:
    print("liczba jest dodatnia")

#przykład 2 - warunek z klauzulą else

print("\n________ przykład 2_________")
liczba = -5

if liczba > 0:
    print("liczba jest dodatnia")
else:
    print("liczba jest ujemna lub równa 0")


#przykład 3 - warunek z klauzulą else oraz elif (else if)

print("\n________ przykład 3_________")
liczba = 0

if liczba > 0:
    print("liczba jest dodatnia")
elif liczba < 0:
    print("liczba jest ujemna")
else:
    print("liczba jest równa 0")

#przykład 4 - zagnieżdzone instrukcje if

print("\n________ przykład 4_________")
liczba = -4
if liczba > 0:
    print("liczba jest dodatnia")
    if liczba % 2 == 0:
        print("liczba jest parzysta")
    else:
        print("liczba jest nieparzysta")
else:
    print("liczba jest ujmena lub równa 0")


#przykład 5 -> Ternary Operator (Operator trójskładnikowy)
print("\n________ przykład 5_________")
liczba = -3
wynik = "dodatnia" if liczba > 0 else "ujemna lub zerowa"
print(f"liczba jest {wynik}")

#przykład 6 -> Match ... case
print("\n________ przykład 6_________")
print("klasyfikator miast")

l_miesz = 340_000

match l_miesz:
    case n if n > 1_000_000:
        print(f"Miasto o liczbie mieszkańców powżej 1 mln")
    case n if 500_000 < n <= 1_000_000:
        print(f"Miasto o liczbie mieszkańców 500 tyś do 1 mln")
    case n if 200_000 < n <= 500_000:
        print(f"Miasto o liczbie mieszkańców 200 tyś do 500 tyś")
    case n if 100_000 < n <= 200_000:
        print(f"Miasto o liczbie mieszkańców 100 tyś do 100 tyś")
    case _:
        print(f"Miasto o liczbie mieszkańców mniejszej niż 100 tyś")




