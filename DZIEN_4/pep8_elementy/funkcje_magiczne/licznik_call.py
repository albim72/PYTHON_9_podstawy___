class Licznikwywolan:
    def __init__(self):
        self.liczba_wywolan = 0

    def __call__(self, *args, **kwargs):
        """Zwiększa licznik i wykonuje zadaną akcję..."""
        self.liczba_wywolan += 1
        print(f"funkcja została wywołana {self.liczba_wywolan} razy")
