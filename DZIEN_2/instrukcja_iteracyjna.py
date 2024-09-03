#przykład 1
print("_"*60)
miasta = ["Warszawa","Lublin","Kraków","Gliwice","Toruń"]

print(miasta)

# miasto:str
for miasto in miasta:
    print(miasto)

print(miasta[3])
#przykład 2 - pętla for z użyciem funkcji range()
print("_"*60)

for i in range(1,21,2):
    print(f"wartośc i*3 = {i*3}")

#przykład 3 - pętla while
print("_"*60)
licznik = 1
while licznik <= 6:
    print(licznik)
    licznik += 1

# while True:
#     print(licznik)
#     licznik += 1

#przykład 4 - pętla for z użyciem funkcji enumerate()
print("_"*60)

# for miasto in miasta:
#     index = miasta.index(miasto)
#     print(f"index: {index}, miasto: {miasto}")

for index,miasto in enumerate(miasta,101):
    print(f"index: {index}, miasto: {miasto}")


#przykład 5 - pętla z użyciem 'break' i 'continue
print("_"*60)
for i in range(1,11):
    if i==6:
        continue
    if i==8:
        break
    print(i)
