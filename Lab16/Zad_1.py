import sqlite3
import os

contact = sqlite3.connect("book.db")


class Contact_book:
    def __init__(self, imie, nazwisko, kontakt):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kontakt = kontakt

    def Create_Book(self):
        if not os.path.exists("book.db"):
            with contact:
                contact.execute(
                    "CREATE TABLE KONTAKTY("
                    "id INTEGER NOT NULL,"
                    "name TEXT NOT NULL,"
                    "lastname TEXT NOT NULL,"
                    "number INTEGER NOT NULL,"
                    "PRIMARY KEY('id' AUTOINCREMENT));"
                )
                contact.commit()
        else:
            with contact:
                contact.execute(
                    "CREATE TABLE IF NOT EXISTS KONTAKTY("
                    "id INTEGER NOT NULL,"
                    "name TEXT NOT NULL,"
                    "lastname TEXT NOT NULL,"
                    "number INTEGER NOT NULL,"
                    "PRIMARY KEY('id' AUTOINCREMENT));"
                )
                contact.commit()

    def Add_Contact(self):
        choise = int(input("Chcesz dodać nr tel czy możę dodać podany numer 1 - podany kontakt 2 - Wczytaj ?"))
        if choise == 1:
            with contact:
                contact.execute(
                    "INSERT INTO Kontakty VALUES(NULL, ?, ?, ?)",
                    (self.imie, self.nazwisko, self.kontakt),
                )
                print("\nDodano kursanta")
                contact.commit()
        else:
            add_name = input("Podaj imie:")
            add_last_name = input("Podaj nazwisko :")
            add_number = int(input("Podaj nr :"))
            with contact:
                contact.execute(
                    "INSERT INTO Kontakty VALUES(NULL, ?, ?, ?)",
                    (add_name, add_last_name, add_number),
                )
                print("\nDodano kursanta")
                contact.commit()

    def Delete_Number(self):
        choise = int(input("Podaj numer do usunięcia :"))
        with contact:
            contact.execute("DELETE FROM KONTAKTY WHERE id=?", (choise,))
            print("\nUsunieto kursanta")
            contact.commit()
    def Print_Base_Kontakt(self):
        with contact:
            cursor = contact.execute("SELECT * FROM KONTAKTY;")
            result = cursor.fetchall()
            for x in result:
                print("ID:", x[0], "|", x[1], x[2], x[3])
            contact.commit()


def Menu():
    Contacts = Contact_book("Paulina", "Śliwka", 12346789)
    while True:
        choise = int(input("1 - Stwórz ksiązke , 2 - Dodaj Kontakt, 3 - Usun numer, 4 - Pokaz Kontakty w Bazie , 5 - Wyjdz z programu "))
        if choise == 1:
            Contacts.Create_Book()
        elif choise == 2:
            Contacts.Add_Contact()
        elif choise == 3:
            Contacts.Delete_Number()
        elif choise == 4:
            Contacts.Print_Base_Kontakt()
        elif choise == 5:
            contact.close()
            break


Menu()