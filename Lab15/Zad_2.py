# class Sklep:
#     def __init__(self, cena, opinie):
#         self.cena = cena
#         self.opinie = []


# class Bar(Sklep):
#     def __init__(self, cena, opinie):
#         super().__init__(cena,opinie)

#     def Sprawdz_wiek(self, wiek):
#         print("Czekaj czekaj , Sprawdźmy ile masz lat ")
#         if wiek >= 18:
#             return True
#         else:
#             return False


# class Beer(Bar):
#     def __init__(self, stezenie, cena, opinie):
#         self.katerogie = ("Ciemne", "Jasne", "Pełnoziarniste")
#         self.stezenie = stezenie
#         super().__init__(cena, opinie)

#     def Wybierz_Piwko(self, Wiek):
#         if Wiek:
#             print("Okey Udało ci się jesteś pełnoletni")
#             i = 0
#             print("Witaj Oto Menu Piwek :")
#             for type_ in self.katerogie:
#                 print(i + 1, ".", type_)
#                 i += 1
#             choise = int(input("Masz na coś ochotę (1,2,3)? :"))

#             return self.katerogie[choise - 1]
#         else:
#             print("No sorki niestety nie sprzedamy ci piwka..;/")
#     def Sprawdz_Czy_Piwko_Jest_W_Lodowie(self):
#         choise = input("Siemka w czym mogę pomóc może piwko ? Tylko powiedz jakie chcesz a powiem ci czy jest dostępne :")

#         if choise in self.katerogie:
#             print("Jasne mamy takie piwko na stanie")
#         else:
#             print("Niestety niema, weź wybierz jakieś inne pokaże ci co mamy :")
#             print(self.katerogie)


#     def __str__(self):
#         return f"Twoje piwko ma {self.stezenie} i kosztuje {self.cena}"


# piwko1 = Beer("5.0%", 4.99, 5)
# piwko2 = Beer("5.0%", 4.99, 6)
# piwko3 = Beer("0.5%", 6.99, 7)

# piwko1.Sprawdz_Czy_Piwko_Jest_W_Lodowie()
# wiek = piwko1.Sprawdz_wiek(18)
# piwko = piwko1.Wybierz_Piwko(wiek)

# print("Wybrałes :", piwko)
# print(piwko1)


class Beer:
    def __init__(self, name, voltage, price, rating, comment):
        self.name = name
        self.voltage = voltage
        self.price = price
        self.rating = rating
        self.comment = comment


class Sklep(Beer):
    def __init__(self, list_of_beers):
        self.list_of_beers = list_of_beers

    def sort_by_name(self):
        print("Sortowanie po nazwie:")
        name_list = []
        for beer in list_of_beers:
            name_list.append(beer.name)

        name_list.sort()

        for name in name_list:
            for beer in list_of_beers:
                if beer.name == name:
                    print("nazwa:", beer.name, "%:", beer.voltage, "cena:", beer.price, "zł", "ocena:", beer.rating,
                          "opinia:", beer.comment)

    def sort_by_rating(self):
        print("Sortowanie po ocenie:")
        rating_list = []
        for beer in list_of_beers:
            rating_list.append(beer.rating)

        rating_list.sort(reverse=True)

        for rating in rating_list:
            for beer in list_of_beers:
                if beer.rating == rating:
                    print("nazwa:", beer.name, "%:", beer.voltage, "cena:", beer.price, "zł", "ocena:", beer.rating,
                          "opinia:", beer.comment)


b1 = Beer("Lech", 5, 3.5, 2, "Takie see")
b2 = Beer("Perła", 6, 3, 10, "Niech będzie")
b3 = Beer("Dębowe", 9, 2, 5, "Fajnie kopie i tanie")
list_of_beers = [b1, b2, b3]

s1 = Sklep(list_of_beers)
s1.sort_by_name()
s1.sort_by_rating()