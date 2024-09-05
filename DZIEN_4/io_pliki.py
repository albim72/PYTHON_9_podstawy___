import os

f = open("dane.txt","r",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
print(f.closed)

print("_"*50)

f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()

print("_"*50)
f = open("dane.txt","r",encoding="utf-8")
for i in f:
    print(str(i))

print("_"*50)
g = open("message.txt","w",encoding="utf-8")
g.write("to jest pierwsza linia - ąąąłłł\n")
g.close()

print("_"*50)
g = open("info.txt","a",encoding="utf-8")
g.write("linia, kóra wporowadza nowe dane....\n")
g.close()

#usunięcie pliku z dysku
if os.path.exists("info.txt"):
    os.remove("info.txt")
    print("plik został usunięty!")
else:
    print("plik nie istnieje!")
