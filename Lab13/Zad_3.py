class Smartphone:
    def __init__(self, name, model, price, bateria, nr_tel, memory, os, charged):
        self.name = name
        self.model = model
        self.price = price
        self.bateria = bateria
        self.nr_tel = nr_tel
        self.memory = os
        self.charged = charged

    def IsCharged(self):
        print(self.name, self.model, "jest ")
        if self.charged > 80:
            print("naladowany")
        elif 80 > self.charged >= 50:
            print("niezbyt Naładowany")
        else:
            print("Rozładowany")

    def BasicStaff(self):
        print(self.name, " ", self.model)

    def Charge(self, charged):
        how_much = 0
        while how_much != charged:
            how_much += 5
            print("Naładowany , ", how_much, "Procent")

    def SaveNumber(self):
        tab = []
        an = int(input("By sprawdzić swój numer wybierz opcje 1 by dodac numer wybierz opcje 2 :"))
        if an == 1:
            return f"Oto Twój numer : {self.nr_tel}"
        elif an == 2:
            number = input("Podaj jaki chcesz nr tel dodac , pamietaj 9 liczb !:")
            if len(number) == 9:
                tab.append(self.nr_tel)
                tab.append(number)
                return tab
            else:
                return "Podano nieprawidłową ilość liczb "
        else:
            return "chyba jakiś missclick"

    def __def__(self):
        print("Wyrzuciłes ", self.name, self.model)


smartfon1 = Smartphone("Nokia", "3310 ", 0, 1600, "159434132", "32 ", "Symbian", 100)
smartfon2 = Smartphone("Samsung", "Galaxy Note 7 ", 500, 3500, "259434132", "64 ", "Android", 20)
smartfon3 = Smartphone("Xiaomi", "Redmi Note 8t ", 800, 4000, "359434132", "64 ", "Android", 0)


smartfon3.IsCharged()
smartfon2.BasicStaff()
smartfon3.Charge(80)
smartfon2.__def__()
print(smartfon1.SaveNumber())