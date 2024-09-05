try:
    x = 12
    print(x)
except NameError as ne:
    print(f"x nie istnieje -> {ne}")
except Exception as exc:
    print(exc)
else:
    y = 5
    z = y*x-2
    print(f"wartośc z -> {z}")
finally:
    k = 19
    print(f'wartośc k -> {k}')

print("to jest ciąg dalszy programu...")
