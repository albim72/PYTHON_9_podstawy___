print((lambda a:a+10)(12))
print((lambda a:a+10)(4.5))

def sumuj(a):
    return a+10

print(sumuj(12))

dodaj = lambda x,y:x+y
print(dodaj(3,7))

def multi(n):
    return lambda a:a*n

print(multi(6)(9))
print(multi(14)(0.66544))

#list comprehension
cube = [x**3 for x in range(1,2001) if x%2 == 0]
print(cube)
print(sum(cube))
