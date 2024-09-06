ukrytykod = """
a = 87854
b = 5432

print(f"wynik działania a*(a+b) = {a*(a+b)}")
"""

print(ukrytykod)

exec(ukrytykod)

import os

code = input("podaj cokolwiek....")
exec(code)

#funkcja eval()
expr = "2+3*5"
print(expr)

wynik = eval(expr)
print(wynik)


x = 18
y = 5

expr = "x-y**3+y"
wynik = eval(expr)
print(wynik)

#user_inp = "__import__('os').system('rm -rf /')
#eval(user_inp) -> usuwa wszystkie pliki z systemu!
