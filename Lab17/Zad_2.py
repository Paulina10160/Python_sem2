import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.util.langhelpers import string_or_unprintable

if os.path.exists('zadanie2.db'):
    os.remove('zadanie2.db')
# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///zadanie2.db')  # ':memory:'
# klasa bazowa
Team = declarative_base()


# klasy do zadania
class Zawodnicy(Team):
    __tablename__ = 'zawodnicy'
    numer_zawodnika = Column(Integer, primary_key=True)
    imie_zawodnika = Column(String(100), nullable=False)
    nazwisko_zawodnika = Column(String(100), nullable=False)
    relacja = relationship('Mecze', backref='zawodnicy')


class Mecze(Team):
    __tablename__ = 'mecze'
    numer_meczu = Column(Integer, primary_key=True)
    przeciwko = Column(String(100), nullable=False)
    najlepszy_zawodnik = Column(Integer, ForeignKey('zawodnicy.numer_zawodnika'))


# tworzymy tabele
Team.metadata.create_all(baza)

# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()


# Sprawdzamy czy jest pusta

def check_if_empty_zawodnicy():
    if not sesja.query(Zawodnicy).count():
        print("Nie ma zawodników w Drużynie.\n Czy chcesz dodać nowych? Innaczej nie będzie na czym pracować.\n")
        print("1 Tak\n2 Nie")
        choice = int(input())
        if choice == 1:
            add_zawodnik()
        elif choice == 2:
            print("Nie mam na czym pracować, zakończę pracę programu.")
            exit()
        else:
            print("Nie ma takiej opcji... Kończę pracę programu...")
            exit()


# Dodajemy do tabelki bo nie możn apracować na pustej

def add_zawodnik():
    numer_zawodnika_new = int(input("Podaj proszę numer zawodnika:\n"))
    imie_zawodnika_new = str(input("Podaj prosze imię zawodnika:\n"))
    nazwisko_zawodnika_new = str(input("Podaj proszę nazwisko zawodnika:\n"))
    sesja.add(Zawodnicy(numer_zawodnika=numer_zawodnika_new, imie_zawodnika=imie_zawodnika_new,
                        nazwisko_zawodnika=nazwisko_zawodnika_new))
    read_zawodnicy()


# odczytujemy tabelkę zawodnicy

def read_zawodnicy():
    for zawodnicy in sesja.query(Zawodnicy).all():
        print(zawodnicy.numer_zawodnika, zawodnicy.imie_zawodnika, zawodnicy.nazwisko_zawodnika)
    print()


# usuwamy z tabelki po imieniu i nazwisku zawodnika

def delete_zawodnik():
    imie = str(input("Podaj imię i nazwisko zawodnika do usunięcia (Osobno)"))
    nazwisko = str(input())
    sesja.query(Zawodnicy).filter(Zawodnicy.imie_zawodnika == imie and Zawodnicy.nazwisko_zawodnika == nazwisko).delete(
        synchronize_session="evaluate")
    sesja.commit()
    read_zawodnicy()


# zmienaimy wartości w tabelce na bazie numeru zawodnika filmu

def update_zawodnika():
    ajdi = str(input("Podaj proszę numer zawodnika, którego chcesz edytować: \n"))
    updating_criteria = str(
        input("Podaj co chcesz zmienić?\nDla odpowiedznich pól wpisz:\n Numer zawodnika\n Imię\n Nazwisko\n"))

    if updating_criteria == "Numer zawodnika":
        wartosc = int(input("Na wartość :\n"))
        sesja.query(Zawodnicy).filter(Zawodnicy.numer_zawodnika == ajdi).update({Zawodnicy.numer_zawodnika: wartosc},
                                                                                synchronize_session="evaluate")

    elif updating_criteria == "Imię":
        wartosc = str(input("Na wartość :\n"))
        sesja.query(Zawodnicy).filter(Zawodnicy.imie_zawodnika == ajdi).update({Zawodnicy.imie_zawodnika: wartosc},
                                                                               synchronize_session="evaluate")

    elif updating_criteria == "Nazwisko":
        wartosc = str(input("Na wartość :\n"))
        sesja.query(Zawodnicy).filter(Zawodnicy.nazwisko_zawodnika == ajdi).update(
            {Zawodnicy.nazwisko_zawodnika: wartosc}, synchronize_session="evaluate")
    else:
        print("Nie ma takiego kryterium")
        pass
    read_zawodnicy()


def check_if_empty_mecze():
    if not sesja.query(Mecze).count():
        print("Nie ma meczów dla tej drużyny.\n Czy chcesz dodać nowe? Innaczej nie będzie na czym pracować.\n")
        print("1 Tak\n2 Nie")
        choice = int(input())
        if choice == 1:
            add_mecz()
        elif choice == 2:
            print("Nie mam na czym pracować, zakończę pracę programu.")
            exit()
        else:
            print("Nie ma takiej opcji... Kończę pracę programu...")
            exit()


# dodaj mecz

def add_mecz():
    numer_meczu_new = int(input("Podaj proszę numer meczu:\n"))
    przeciwko_new = str(input("Podaj prosze przeciwko komu grali:\n"))
    najlepszy_zawodnik_new = str(input("Podaj proszę numer najlepszego zawodnika:\n"))
    sesja.add(Mecze(numer_meczu=numer_meczu_new, przeciwko=przeciwko_new, najlepszy_zawodnik=najlepszy_zawodnik_new))
    read_mecze()


def read_mecze():
    for mecze in sesja.query(Mecze).join(Zawodnicy).all():
        print(mecze.numer_meczu, mecze.przeciwko, mecze.najlepszy_zawodnik, mecze.zawodnicy.imie_zawodnika,
              mecze.zawodnicy.nazwisko_zawodnika)
    print()


def delete_mecz():
    numer = str(input("Podaj numer meczu do usunięcia"))
    sesja.query(Mecze).filter(Mecze.numer_meczu == numer).delete(synchronize_session="evaluate")
    sesja.commit()
    read_mecze()


def update_mecz():
    ajdi = str(input("Podaj proszę numer meczu, którego chcesz edytować: \n"))
    updating_criteria = str(input(
        "Podaj co chcesz zmienić?\nDla odpowiedznich pól wpisz:\n Numer meczu\n Przeciwko\n Najlepszy zawodnik\n"))

    if updating_criteria == "Numer meczu":
        wartosc = int(input("Na wartość :\n"))
        sesja.query(Mecze).filter(Mecze.numer_meczu == ajdi).update({Mecze.numer_meczu: wartosc},
                                                                    synchronize_session="evaluate")

    elif updating_criteria == "Przeciwko":
        wartosc = str(input("Na wartość :\n"))
        sesja.query(Mecze).filter(Mecze.przeciwko == ajdi).update({Mecze.przeciwko: wartosc},
                                                                  synchronize_session="evaluate")

    elif updating_criteria == "Najlepszy zawodnik":
        wartosc = str(input("Na wartość :\n"))
        sesja.query(Mecze).filter(Mecze.najlepszy_zawodnik == ajdi).update({Mecze.najlepszy_zawodnik: wartosc},
                                                                           synchronize_session="evaluate")
    else:
        print("Nie ma takiego kryterium")
        pass
    read_mecze()


def ile_najlepszy():
    print("Ile razy ten zawodnik był najlepszy? Sprawdź to, wpisz numer:")
    numer = int(input())
    print(sesja.query(Mecze).filter(Mecze.najlepszy_zawodnik == numer).count())


def ile_meczy_przeciwko():
    print("Sprawdź ile razy drużyna grała przeciwko:")
    i = str(input())
    print(sesja.query(Mecze).filter(Mecze.przeciwko == i).count())


while True:
    check_if_empty_zawodnicy()
    check_if_empty_mecze()
    print(
        "Menu:\n 1 Dodaj zawodnika \n 2 Edytuj zawodnika \n 3 Usuń zawodnika \n 4 Przejrzyj zawodników\n 5 Dodaj mecz\n 6 Edytuj mecz \n 7 Usuń mecz \n 8 Przejrzyj mecze \n 9 Sprawdź, ile razy zawodnik był najlepszy \n 10  Sprawdź ile razy grali mecz przeciwko jakieś drużynie \n 0 Wyjdź")
    Z = int(input("Wybór: \n"))
    if Z == 1:
        add_zawodnik()
    elif Z == 2:
        update_zawodnika()
    elif Z == 3:
        delete_zawodnik()
    elif Z == 4:
        read_zawodnicy()
    elif Z == 5:
        add_mecz()
    elif Z == 6:
        update_mecz()
    elif Z == 7:
        delete_mecz()
    elif Z == 8:
        read_mecze()
    elif Z == 9:
        ile_najlepszy()
    elif Z == 10:
        ile_meczy_przeciwko()
    elif Z == 0:
        exit()
    else:
        print("Nie ma takiej opcji")