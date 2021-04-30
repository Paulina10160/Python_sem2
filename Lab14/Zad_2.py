class Zwierze:
    def __init__(self, imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje):
        self.imie = imie
        self.gatunek = gatunek
        self.rodzaj_konczyn = rodzaj_konczyn
        self.ilosc_konczyn = ilosc_konczyn
        self.pokrycie_skory = pokrycie_skory
        self.zyje = zyje

    def CzyZyje(self):
        if self.zyje == True:
            print(f"{self.imie} żyje!!! Idziemy z nim na spacer")
        else:
            print(f"Nasz słodziak {self.gatunek} już nie żyje.. Jest nam bardzo smutno...")


class Bird(Zwierze):
    def __init__(self, imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje, latanie):
        super().__init__(self, imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje)
        self.latanie = latanie

    def Fly(self):
        print("Twoj ptak {} {} polecial i nie wrocil".format(gatunek, imie))

    def CzyZyje(self):
        if self.zyje == True:
            print(f"{self.imie} żyje!!! Idziemy z nim na spacer")
        else:
            print(f"Nasz słodziak {self.gatunek} już nie żyje.. Jest nam bardzo smutno...")


class Cat(Zwierze):
    def __init__(self, imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje, dom_dzik):
        super().__init__(self, imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje)
        self.dom_dzik = dom_dzik

    def Runner(self):
        print(f"{self.name} biega po całym mieszkaniu! Chowaj się!!!")

    def CzyZyje(self):
        if self.zyje == True:
            print(f"{self.imie} żyje!!! Idziemy z nim na spacer")
        else:
            print(f"Nasz słodziak {self.gatunek} już nie żyje.. Jest nam bardzo smutno...")


class Fish(Zwierze):
    def __init__(self, imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje, slonoWodna):
        super().__init__(self, imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje)
        self.slonoWodna = slonoWodna

    def Swimming(self):
        print("gul, gul, gul")

    def CzyZyje(self):
        if self.zyje == True:
            print(f"{self.imie} żyje!!! Idziemy z nim na spacer")
        else:
            print(f"Nasz słodziak {self.gatunek} już nie żyje.. Jest nam bardzo smutno...")


class Dog(Zwierze):
    def __init__(self, imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje, odglos):
        super().__init__(self.imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje)
        self.odglos = odglos

    def podaj_glos(self):
        print(f"Pies ma na imie {self.imie}. Po poleceniu robie {self.odglos}")

    def CzyZyje(self):
        if self.zyje == True:
            print(f"{self.imie} żyje!!! Idziemy z nim na spacer")
        else:
            print(f"Nasz słodziak {self.gatunek} już nie żyje.. Jest nam bardzo smutno...")


class Main:
    animals = []
    myAnimals = []

    def PrintMyAnimals():
        print(animals)

    def CreateAnimal():
        rodzaj = input("Jakie zwierze chcesz stworzyć? wybierz z: Bird, Cat, Dog, Fish")
        if rodzaj.capitalize() == "Bird":
            lata = input("Czy potrafi latać?")
            newAnimal = Bird(DeclareAnimalAtributes, latanie)
            animals.append(newAnimal)
        elif rodzaj.capitalize() == "Cat":
            dziki = input("Czy kot jest dziki czy domowy?")
            newAnimal = Cat(DeclareAnimalAtributes, dziki)
            animals.append(newAnimal)
        elif rodzaj.capitalize() == "Fish":
            slonoWodna = input("Czy ryba jest slonowodna?")
            newAnimal = Fish(DeclareAnimalAtributes, slonoWodna)
            animals.append(newAnimal)
        elif rodzaj.capitalize() == "Dog":
            odglos = input("Jaki ma odglos?")
            newAnimal = Dog(DeclareAnimalAtributes, odglos)
            animals.append(newAnimal)

    def DeclareAnimalAtributes():
        gatunek = input("Podaj gatunek")
        imie = input("Podaj imie")
        rodzaj_konczyn = input("Podaj rodzaj konczyn")
        ilosc_konczyn = input("Podaj ilosc konczyn")
        pokrycie_skory = input("Podaj rodzaj pokrycia skory")
        zyje = input("Czy jeszcze zyje?")
        return imie, gatunek, rodzaj_konczyn, ilosc_konczyn, pokrycie_skory, zyje
