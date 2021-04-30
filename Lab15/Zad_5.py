class Hotel:
    def __init__(self, liczba_pokoi, liczba_pieter):  # Liczba pokoi na petro
        self.liczba_pokoi = liczba_pokoi
        self.liczba_pieter = liczba_pieter
        self.pokoje = []
        nr_pokoju = 1
        for nr_pietra in range(self.liczba_pieter):  # tworzymy dla kazdego pietra okreslona ilosc pokoi
            for i in range(self.liczba_pokoi):  # wykonaj ta petle tyle razy ile trzeba stworzyc pokoi dla danego pietra
                self.pokoje.append(Pokoj(nr_pokoju=nr_pokoju, nr_pietra=nr_pietra))  # tworzy pokoj i dodaje go do listy
                nr_pokoju += 1

    def czy_wolny_pokoj(self):
        for pokoj in self.pokoje:  # przejdz po wszystkich pokojach
            if pokoj.czy_wolny():  # jesli pokoj jest wolnych to zwroc True
                return True
        return False  # jesli zaden z pokoi nie jest wolny to zwroc False

    def ile_wolnych_pokoi(self):
        ile = 0
        for pokoj in self.pokoje:  # przejdz po wszystkich pokojach
            if pokoj.czy_wolny():
                ile += 1  # jesli pokoj jest jest wolny to zwieksz licznik wolnych pokoi o 1
        return ile

    def pobierz_wolny_pokoj(self):
        for pokoj in self.pokoje:  # przejdz po wszystkich pokojach
            if pokoj.czy_wolny():  # jesli pokoj jest wolnych to go zwroc
                return pokoj

    def wynajmij_pokoj(self, osoba):
        pokoj = self.pobierz_wolny_pokoj()
        if pokoj != None:  # jesli udalo sie znalezc wolny pokoj
            pokoj.zajmij(osoba)
            return pokoj.nr_pokoju

    def czy_mozna_wynajac_2(self):
        for i in range(len(self.pokoje) - 1):  # iterujemy po indeksach wszystkich pooki poza ostatnim
            # poniewaz bedziemy brali pary pokoi do porownania (zakladamy ze pokoje w liscie sa poukadane numerem pokoju)
            if self.pokoje[i].czy_wolny() and self.pokoje[i + 1].czy_wolny() and self.pokoje[i].nr_pietra == \
                    self.pokoje[i + 1].nr_pietra:
                # sprawdzamy czy mamy dwa wolne pokoje obok siebie i czy sa na tym samym pietrze
                return self.pokoje[i].nr_pokoju

    def czy_osoba_wynajmuje(self, nazwisko):
        for p in self.pokoje:
            if not p.czy_wolny() and p.osoba.nazwisko == nazwisko:  # jesli mamy zajety pokoj i osoba ktora go zajmuje ma to nazwisko szukane
                return True
        return False

    def zwolnij_pokoje(self, nazwisko):
        for p in self.pokoje:
            if not p.czy_wolny() and p.osoba.nazwisko == nazwisko:  # jesli podany pokoj jest zajety przez to nazwisko
                p.zwolnij()


class Pokoj:
    def __init__(self, nr_pokoju, nr_pietra, osoba=None):
        self.nr_pokoju = nr_pokoju
        self.nr_pietra = nr_pietra
        self.osoba = osoba

    def czy_wolny(self):
        return self.osoba is None  # jesli nie ma wpisanej osoby (czyli siedzi None) to funkcja zwroci True

    def zwolnij(self):
        self.osoba = None

    def zajmij(self, osoba):
        self.osoba = osoba


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


hotel = Hotel(liczba_pokoi=4, liczba_pieter=5)
osoba = Osoba(imie="Jan", nazwisko="Kowalski")
hotel.wynajmij_pokoj(osoba)
hotel.wynajmij_pokoj(osoba)
hotel.wynajmij_pokoj(osoba)
print(hotel.czy_osoba_wynajmuje("Kowalski"))
hotel.zwolnij_pokoje("Kowalski")
print(hotel.czy_osoba_wynajmuje("Kowalski"))

osoba2 = Osoba(imie="Katarzyna", nazwisko="Murarz")
hotel.wynajmij_pokoj(osoba2)
print(hotel.ile_wolnych_pokoi())
print(hotel.czy_mozna_wynajac_2())