import math

class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __abs__(self):
        """zwraca odległośc punktu od początku układu współrzędnych (0,0)"""
        return math.sqrt(self.x**2+self.y**2)
    
    def __repr__(self):
        """zwraca czytelną reprezentację punktu."""
        return f"Punkt({self.x},{self.y})"
