class Restaurant:
    def __init__(self, nazwa, NIP, REGON, adres, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow,
                 oferujeDowoz):
        self.nazwa = nazwa
        self.NIP = NIP
        self.REGON = REGON
        self.adres = adres
        self.specjalizacja = specjalizacja
        self.wielkoscLokalu = wielkoscLokalu
        self.iloscPracownikow = iloscStolikow
        self.iloscPracownikow = iloscPracownikow
        self.oferujeDowoz = oferujeDowoz


class IceCreamStand(Restaurant):
    flavour = ["vanilla", "cherry", "kiwi", "chocolatte", "strawberry", "mango", "mascarpone", "pistace", "cream",
               "lemon", "watermelon", "melon", "coffeeEspresso", "coffeLatte", "whiteChocolatte"]

    def __init__(self, nazwa, NIP, REGON, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow, flavour):
        super().__init__(self, nazwa, NIP, REGON, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow)
        self.flavour = flavour

    def present(self):
        print(f"Tutaj pelna lista smaków: {self.flavour}")

    def numbersIce(self):
        rodzaj = input("Czy chcesz do kubka czy do różka? (Kubek / Rozek)")
        if rodzaj.capitalize() == "Kubek":
            num = int(input("Wybrałeś kubek. Możesz do niego poprosić maksymalnie trzy gałki. Ile chcesz? "))
        elif rodzaj.capitalize() == "Rozek":
            num = int(input("Wybrałeś rożek. Ile chcesz gałek? "))
        return num


class CoffeShop(Restaurant):
    coffeTypes = ["latte", "americano", "cappuccino", "flatWhite", "mocca", "latteMacchiato", "espresso"]

    def __init__(self, coffeTypes):
        super().__init__()
        self.coffeTypes = coffeTypes

    def AddCofeeType(self):
        newCoffe = input("Podaj nazwe nowej kawy")
        exists = False
        for item in CoffeShop.coffeTypes:
            if newCoffe == item:
                exists = True
        if exists == False:
            CoffeShop.coffeTypes.append(newCoffe)

    def availableCoffes(self):
        for items in CoffeShop.coffeTypes:
            print(items)

    def orderCoffe(self):
        print(CoffeShop.availableCoffes())
        order = input("Wybierz kawę: ")
        if order in CoffeShop.coffeTypes:
            addEspresso = input(("Wzmocnić kawę dodatkowym espresso?"))
            if addEspresso.upper() == "TAK":
                print(order + "double espresso")
            elif addEspresso.upper() == "NIE":
                print(order)
            else:
                print("Nie posiadamy takiej kawy :c")


class Main:
    lokalneRestauracje = []

    def AddRestaurant(self):
        newRestaurant = input("Podaj nazwe nowej restauracji")
        Main.lokalneRestauracje.append(newRestaurant)

    def ShowLocalRestaurants(self):
        print(Main.lokalneRestauracje)