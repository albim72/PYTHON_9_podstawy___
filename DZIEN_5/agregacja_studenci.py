class Student:
    def __init__(self,imie,nazwisko,id_stud):
        self.imie = imie
        self.nazwisko = nazwisko
        self.id_stud = id_stud
        
class Uniwersytet:
    def __init__(self,nazwa_uczelni):
        self.nazwa_uczelni = nazwa_uczelni
        self.studenci = []
        
    def dodaj_studenta(self,student):
        self.studenci.append(student)
        
    def print_studenci(self):
        print(f"Studenci uczelni: {self.nazwa_uczelni}\n")
        for student in self.studenci:
            print(f" -> studnet {student.imie} {student.nazwisko} - id: {student.id_stud}")
