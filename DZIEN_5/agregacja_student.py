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

student1 = Student(imie="Alicja",nazwisko="Kot", id_stud=5435)
student2 = Student(imie="Marek",nazwisko="Olin", id_stud=8534)
student3 = Student(imie="Leon",nazwisko="Nowak", id_stud=1268)

print(student1)
print(student2)
print(student3)

univ = Uniwersytet(nazwa_uczelni="Uniwersytet Marii Curie-Skłodowskiej w Lublinie")
univ.dodaj_studenta(student1)
univ.dodaj_studenta(student2)
univ.dodaj_studenta(student3)

univ.print_studenci()
