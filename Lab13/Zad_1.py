class Car:
    def __init__(self, brand, age, color, capacity, fuelType):
        self.brand = brand
        self.age = age
        self.color = color
        self.capacity = capacity
        self.fuelType = fuelType

    def Refueling(self):
        print("Zatankowano: {} {} litrów ".format(self.fuelType, self.capacity))

    def CarInfo(self):
        print("Marka:", self.brand)
        print("Wiek:", self.age)
        print("Kolor:", self.color)
        print("Pojemność baku:", self.capacity)
        print("Rodzaj paliwa:", self.fuelType)

    def ChangeColor(self, newColor):
        print("Zmieniono kolor z {} na {}".format(self.color, newColor))

    def Velocity(self):
        if (self.color == "red"):
            print("Bardzo szybki")
        else:
            print("Nie tak szybki jak czerwony")

    def CallService(self):
        print("Jesteś 10 w kolejce")


opelek = Car("Opel", 10, "Silver", 50, "diesel")
opelek.Refueling()
opelek.ChangeColor("blue")
opelek.CarInfo()
opelek.Velocity()
opelek.CallService()
