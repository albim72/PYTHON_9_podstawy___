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
