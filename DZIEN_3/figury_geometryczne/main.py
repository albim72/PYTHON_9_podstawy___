from prostokat import Prostokat
from trojkat import Trojkat
from trapez import Trapez

pr = Prostokat(4.4,8.9)
print(f"pole figury {pr.__class__.__name__} wynosi: {pr.policz_pole():.2f} cm2")

tr = Trojkat(5.8,8.9)
print(f"pole figury {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2")

trp = Trapez(10,6.8,5.2)
print(f"pole figury {trp.__class__.__name__} wynosi: {trp.policz_pole():.2f} cm2")

