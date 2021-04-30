class Pojazd:
    def __init__(self, marka, model, cena, pojemnosc_silnika, rodzaj_paliwa, przebieg):
        self.marka = marka
        self.model = model
        self.cena = cena
        self.pojemnosc_silnika = pojemnosc_silnika
        self.rodzaj_paliwa = rodzaj_paliwa
        self.przebieg = przebieg


class Samochod(Pojazd):
    def __init__(
        self,
        marka,
        model,
        cena,
        pojemnosc_silnika,
        rodzaj_paliwa,
        przebieg,
        ilosc_drzwi,
        poj_bagaznika,
    ):
        super().__init__(marka, model, cena, pojemnosc_silnika, rodzaj_paliwa, przebieg)
        self.ilosc_drzwi = ilosc_drzwi
        self.poj_bagaznika = poj_bagaznika

    def __str__(self):
        return f" Marka:{self.marka} Model:{self.model} Cena:{self.cena} Pojemność:{self.pojemnosc_silnika} Rodzaj Paliwa:{self.rodzaj_paliwa} Przebieg:{self.przebieg} Pojemność Bagaznika:{self.poj_bagaznika}"
    def __del__(self):
        return print("Usuwam samochód")


class Motor(Pojazd):
    def __init__(
        self,
        marka,
        model,
        cena,
        pojemnosc_silnika,
        rodzaj_paliwa,
        przebieg,
        rodzaj_siodla,
        rodzaj_ramy,
    ):
        super().__init__(marka, model, cena, pojemnosc_silnika, rodzaj_paliwa, przebieg)
        self.rodzaj_siodla = rodzaj_siodla
        self.rodzaj_ramy = rodzaj_ramy
    def __str__(self):
        return f" Marka: {self.marka} Model:{self.model} Cena:{self.cena} Pojemność:{self.pojemnosc_silnika} Rodzaj Paliwa:{self.rodzaj_paliwa} Przebieg:{self.przebieg} Rodzaj Siodla:{self.rodzaj_siodla} Rodzaj Ramy:{self.rodzaj_ramy} "
    def __del__(self):
        return print("Usuwam Motor")


# lista Obiektów

samochod1 = Samochod(
    "Fiat ", " 124 ", " 13000 ", " 1.6 ", "Benzyna ", " 250 000", " 5 ", "300l"
)
motor1 = Motor(
    "Kawasaki ",
    " Ninja ",
    " 7000 ",
    " 650 ",
    "Benzyna ",
    " 40 000",
    " skurzane",
    " metalowa ",
)

print(samochod1)
print(motor1)