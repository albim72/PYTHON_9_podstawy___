#funkcja mapująca wartości "starej listy" na "nową listę" w taki sposób żeby każdy element nowej listy
#był wartością -> st**3-3

def nowa_lista(stara_lista):
    return list(map(lambda x:x**3-3,stara_lista))
