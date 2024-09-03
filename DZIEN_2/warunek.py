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
