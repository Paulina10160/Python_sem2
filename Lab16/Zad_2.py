import sqlite3
import os

conn = sqlite3.connect("salary_database.db")

if not os.path.exists("salary_database.db"):
    with conn:
        conn.execute("CREATE TABLE Tabela_wyplat("
                     "id INTEGER NOT NULL,"
                     "name TEXT NOT NULL,"
                     "city TEXT NOT NULL,"
                     "surname TEXT NOT NULL,"
                     "salary INTEGER NOT NULL,"
                     "PRIMARY KEY('id' AUTOINCREMENT));")
        conn.commit()
else:
    with conn:
        conn.execute("CREATE TABLE IF NOT EXISTS Tabela_wyplat("
                     "id INTEGER NOT NULL,"
                     "name TEXT NOT NULL,"
                     "surname TEXT NOT NULL,"
                     "city TEXT NOT NULL,"
                     "salary INTEGER NOT NULL,"
                     "PRIMARY KEY('id' AUTOINCREMENT));")
        conn.commit()


class Salary_List:
    def __init__(self, name, surname, city, salary):
        self.name = name
        self.surname = surname
        self.city = city
        self.salary = salary

    def add_person(self):

        self.name = input("Wpisz imię: ")
        self.surname = input("Wpisz nazwisko: ")
        self.city = input("Wpisz miejscowość: ")
        self.salary = input("Wpisz wypłatę: ")
        conn.execute(
            f"INSERT INTO Tabela_wyplat (name,surname,city,salary) "
            f"VALUES('{self.name}','{self.surname}','{self.city}',{self.salary});"
        )
        conn.commit()
        print("Osoba dodana!")

    def sort(self):
        print()
        print("Posrtowane imionami")
        cursor = conn.execute(
            "SELECT * FROM Tabela_wyplat ORDER BY name;")
        result = cursor.fetchall()
        for row in result:
            print(row)

    def show_table(self):
        cursor = conn.execute(
            "SELECT * FROM Tabela_wyplat;")
        result = cursor.fetchall()
        for row in result:
            print(row)

    def highest_salary(self):
        print()
        print("Najlepiej zarabiający")
        cursor = conn.execute(
            "SELECT * FROM Tabela_wyplat ORDER BY salary DESC LIMIT 0,3;")
        result = cursor.fetchall()
        for row in result:
            print(row)

    def lowest_salary(self):
        print()
        print("Najgorzej zarabiający")
        cursor = conn.execute(
            "SELECT * FROM Tabela_wyplat ORDER BY salary LIMIT 0,3;")
        result = cursor.fetchall()
        for row in result:
            print(row)

    def delete_person(self):
        Salary_List.show_table(self)
        choice = input("Wpisz numer ID osoby do usunięcia: ")
        confirm = input(
            "Czy chcesz usunąć ten kontakt? Operacji nie można cofnąć! [y]Tak, [n]Nie: ")
        if confirm == "y" or confirm.lower == "y":
            conn.execute(f"DELETE FROM Tabela_wyplat WHERE id='{choice}';")
            conn.commit()
        else:
            print("Usunięcie cofnięte!")

    def update_salary(self):
        Salary_List.show_table(self)
        choice = input("Wpisz numer ID osoby do aktualizacji: ")
        self.salary = input("Podaj nową wypłatę tej osoby: ")
        conn.execute(
            f"UPDATE Tabela_wyplat SET salary='{self.salary}' WHERE id='{choice}'")
        print("Kontakt zaktualizowany!")
        conn.commit()

    def menu(self):
        while True:
            print()
            print("Witaj! Wybierz co chcesz zrobić: \n"
                  "[1]Dodaj osobę,\n"
                  "[2]Sortuj po imieniu,\n"
                  "[3]Największe zarobki,\n"
                  "[4]Najniższe zarbki,\n"
                  "[5]Usuń osobę,\n"
                  "[6]Zaktualizuj wypłatę,\n"
                  "[q]Wyjść: ")
            choice = input("Wybierz: ")

            if choice == "1":
                Salary_List.add_person(self)
            elif choice == "2":
                Salary_List.sort(self)
            elif choice == "3":
                Salary_List.highest_salary(self)
            elif choice == "4":
                Salary_List.lowest_salary(self)
            elif choice == "5":
                Salary_List.delete_person(self)
            elif choice == "6":
                Salary_List.update_salary(self)
            elif choice == "q" or choice.lower() == "q":
                conn.close()
                break
            else:
                print("Brak takiego wyboru.")
            print()


Salary_List.menu(Salary_List)