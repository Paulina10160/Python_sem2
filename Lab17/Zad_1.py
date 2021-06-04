import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

if os.path.exists('VOD.db'):
    os.remove('VOD.db')
# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///VOD.db')  # ':memory:'
# klasa bazowa
BazaModel = declarative_base()


# klasy temat, reżyster, aktorzy, miejsce do obejrzenia
# oraz relacje między nimi
class Title(BazaModel):
    __tablename__ = 'title'
    id = Column(Integer, primary_key=True)
    names = Column(String(100), nullable=False)
    VODs = relationship('Info', backref='title')


class Info(BazaModel):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    genre = Column(String(100), nullable=False)
    director = Column(String(100), nullable=False)
    actors = Column(String(1000), nullable=False)
    source = Column(String(20), nullable=False)
    title_id = Column(Integer, ForeignKey('title.id'))


# tworzymy tabele
BazaModel.metadata.create_all(baza)

# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()


# Sprawdzamy czy jest pusta
def check_if_empty():
    if not sesja.query(Title).count():
        print("Nie ma tytułów w bazie danych.\n Czy chcesz dodać nowy? Innaczej nie będzie na czym pracować.\n")
        print("1 Tak\n2 Nie")
        choice = int(input())
        if choice == 1:
            add_title()
        elif choice == 2:
            print("Nie mam na czym pracować, zakończę pracę programu.")
            exit()
        else:
            print("Nie ma takiej opcji... Kończę pracę programu...")
            exit()


# Dodajemy do tabelki bo nie możn apracować na pustej
def add_title():
    title_new = str(input("Podaj proszę tytuł filmu:\n"))
    sesja.add(Title(names=title_new))
    genre_new = str(input("Podaj prosze gatunek filmu:\n"))
    director_new = str(input("Podaj proszę imię i nazwisko reżysera filmu:\n"))
    actors_new = str(input("Podaj proszę imiona i nazwiska głównych aktorów filmu:\n"))
    source_new = str(input("Podaj proszę na jakiej platformie można obejrzeć film:\n"))
    title_info = sesja.query(Title).filter_by(names=title_new).one()
    sesja.add(
        Info(genre=genre_new, director=director_new, actors=actors_new, source=source_new, title_id=title_info.id))
    read()


# odczytujemy tabelkę
def read():
    for info in sesja.query(Info).join(Title).all():
        print(info.id, info.title.names, info.genre, info.director, info.source, info.actors)
    print()


# usuwamy z tabelki po nazwie filmu
def delete():
    nazwa = str(input("Podaj nazwę filmu do usunięcia"))
    sesja.query(Title).filter(Title.names == nazwa).delete(synchronize_session="evaluate")
    sesja.commit()
    read()


# zmienaimy wartości w tabelce na bazie tytułu filmu
def update():
    ajdi = str(input("Podaj proszę id, który chcesz edytować: \n"))
    updating_criteria = str(input(
        "Podaj co chcesz zmienić?\nDla odpowiedznich pól wpisz:\n Tytuł : names \n Gatunek : genre \n Reżyser : director \n Aktorzy : actors \n Platformę ogląania : source\n"))
    wartosc = str(input("Na wartość :\n"))
    if updating_criteria == "names":
        sesja.query(Title).filter(Title.id == ajdi).update({Title.names: wartosc}, synchronize_session="evaluate")
    elif updating_criteria == "genre":
        sesja.query(Info).filter(Info.title_id == ajdi).update({Info.genre: wartosc}, synchronize_session="evaluate")
    elif updating_criteria == "director":
        sesja.query(Info).filter(Info.title_id == ajdi).update({Info.director: wartosc}, synchronize_session="evaluate")
    elif updating_criteria == "actors":
        sesja.query(Info).filter(Info.title_id == ajdi).update({Info.actors: wartosc}, synchronize_session="evaluate")
    elif updating_criteria == "source":
        sesja.query(Info).filter(Info.title_id == ajdi).update({Info.source: wartosc}, synchronize_session="evaluate")
    read()


while True:
    check_if_empty()
    print("Menu:\n 1 Dodaj \n 2 Zmień \n 3 Usuń \n 4 Przejrzyj\n 5 Wyjdź")
    Z = int(input("Wybór: \n"))
    if Z == 1:
        add_title()
    elif Z == 2:
        update()
    elif Z == 3:
        delete()
    elif Z == 4:
        read()
    elif Z == 5:
        exit()
    else:
        print("Nie ma takiej opcji")