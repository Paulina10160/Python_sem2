import random


class Student():
    def __init__(self, id_number, name, last_name, group, skill):
        self.id_number = id_number
        self.name = name
        self.last_name = last_name
        self.group = group
        self.skill = skill
        self.attempts = 2
        self.happiness = 100

    def learn_to_exam(self):
        print("Uczysz się nowych rzeczy")
        self.skill += 10
        self.happiness -= 10
        if self.happiness < 0:
            print("Od ciągłej nauki ześwirowałeś i wyrzucili Cię z uczelni :(")
            exit()
        self.print_stats()

    def party(self):
        print("Przespałeś poranny wykład, ale elegancko się wybawiłeś")
        self.skill -= 10
        self.happiness += 30
        self.print_stats()

    def write_exam(self):
        luck = random.randint(0, 10)
        if luck + self.skill > 50:
            print("Elegancko, zdałeś kolosa!")
            print("Ucz się do kolejnego..")
            self.skill = 0
            self.attempts = 2
            self.happiness += 20
        else:
            print("Nie zdałeś..")
            self.attempts -= 1
            if self.attempts == 0:
                print("Daj se spokój z tymi studiami..")
                exit()
        self.print_stats()

    def print_stats(self):
        print("wiedza", self.skill)
        print("szczęście", self.happiness)


s1 = Student(1, 'Tomek', 'Nowak', 'IT', 10)
while True:
    print()
    print("<1> Ucz się")
    print("<2> Baluj")
    print("<3> Napisz kolosa")
    choice = int(input("Wybierz:"))
    if choice == 1:
        print()
        s1.learn_to_exam()
    elif choice == 2:
        print()
        s1.party()
    elif choice == 3:
        print()
        s1.write_exam()