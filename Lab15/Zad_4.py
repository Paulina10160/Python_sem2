import random


class Deck:
    def __init__(self, numbers, Max_Round):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.Max_Round = Max_Round

    def War(self):
        Deck = self.Create_Deck()

        # Sortowanie
        self.Sortowanie(Deck)

        player1 = []
        player2 = []

        random.shuffle(Deck)

        half = len(Deck) / 2
        half = int(half)

        for x in range(0, half):
            player1.append(Deck[x])

        for x in range(half, len(Deck)):
            player2.append(Deck[x])

        roundCounter = 1
        while True:
            print("Round", roundCounter)

            if roundCounter == self.Max_Round:
                print("Ta wojna będzie się dłużyć w nieskończoność odpuśćmy co ?")
                break
            elif player1[0] > player2[0]:
                print("Player 1 wygrał tą runde ! !")
                self.WinnerOfPlayer1(player1, player2)

            elif player2[0] > player1[0]:
                print("Player 2 wygrał tą runde ! !")
                self.WinnerOfPlayer2(player1, player2)
            else:
                print("Wojna będzie ciekawie !!!!!!!")
                if player1[0] == player2[0]:

                    if (len(player1) >= 3 and len(player2) > 10) or (
                        len(player1) > 10 and len(player2) >= 3
                    ):

                        if player1[2] == player2[2]:
                            if (len(player1) >= 6 and len(player2) > 10) or (
                                len(player1) > 10 and len(player2) >= 6
                            ):

                                if player1[4] > player2[4]:
                                    print("Player 1 wygrał tą runde ! !")
                                    for _ in range(6):
                                        self.WinnerOfPlayer1(player1, player2)

                                elif player2[4] > player1[4]:
                                    print("Player 2 wygrał tą runde ! !")
                                    for _ in range(6):
                                        self.WinnerOfPlayer2(player1, player2)
                                else:
                                    print(
                                        "To jest praktycznie nie możliwe zacznijcie od nowa"
                                    )
                                    break
                            else:
                                if len(player1) <= 6:
                                    print(
                                        f"Wygrał gracz drugi poniewaz gracz pierwszy nie ma kart by brać udział w wojnie bądź ostatnia karta przełożyła szale zwycieztwa ;/ i musi oddac te karty  {player1}"
                                    )
                                    Length = len(player1)
                                    for _ in range(0, Length):
                                        self.WinnerOfPlayer2(player1, player2)
                                    print(
                                        f"A tu pokazuje ze kazdy zostały uczciwie oddane {player1}"
                                    )
                                    break

                                elif len(player2) <= 6:
                                    print(
                                        f"Wygrał gracz pierwszy poniewaz gracz drugi nie ma kart by brać udział w wojnie bądź ostatnia karta przełożyła szale zwycieztwa ;/ i musi oddac te karty   {player2}"
                                    )
                                    Length2 = len(player2)
                                    for _ in range(0, Length2):
                                        self.WinnerOfPlayer1(player1, player2)
                                    print(
                                        f"A tu juz pokazuje ze karty zostały uczciwie oddane  {player2}"
                                    )
                                    break

                        elif player1[2] > player2[2]:
                            print("Player 1 wygrał tą runde ! !")
                            for _ in range(3):
                                self.WinnerOfPlayer1(player1, player2)

                        elif player2[2] > player1[2]:
                            print("Player 2 wygrał tą runde ! !")
                            for _ in range(3):
                                self.WinnerOfPlayer2(player1, player2)

                    else:
                        if len(player1) == 1:
                            print(
                                f"Wygrał gracz drugi poniewaz gracz pierwszy nie ma kart by brać udział w wojnie ;/ i musi oddac te karty  {player1}"
                            )
                            self.WinnerOfPlayer2(player1, player2)
                            print(
                                f"A tu pokazuje ze kazdy zostały uczciwie oddane {player1}"
                            )
                            break
                        elif len(player2) == 1:
                            print(
                                f"Wygrał gracz pierwszy poniewaz gracz drugi nie ma kart by brać udział w wojnie ;/ i musi oddac te karty  {player2}"
                            )
                            self.WinnerOfPlayer1(player1, player2)
                            print(
                                f"A tu juz pokazuje ze karty zostały uczciwie oddane  {player2}"
                            )
                            break
                        elif len(player1) <= 3:
                            print(
                                f"Wygrał gracz drugi poniewaz gracz pierwszy nie ma kart by brać udział w wojnie ;/ i musi oddac te karty  {player1}"
                            )
                            Length = len(player1)
                            for _ in (1, Length):
                                self.WinnerOfPlayer2(player1, player2)
                            print(
                                f"A tu pokazuje ze kazdy zostały uczciwie oddane {player1}"
                            )
                            break

                        elif len(player2) <= 3:
                            print(
                                f"Wygrał gracz pierwszy poniewaz gracz drugi nie ma kart by brać udział w wojnie ;/ i musi oddac te karty   {player2}"
                            )
                            Length2 = len(player2)
                            for _ in (1, Length2):
                                self.WinnerOfPlayer1(player1, player2)
                            print(
                                f"A tu juz pokazuje ze karty zostały uczciwie oddane  {player2}"
                            )
                            break

                if not player1:
                    print("Wygrał drugi ponieważ pierwszy gracz juz niema kart :)  !")
                elif not player2:
                    print("Wygrał pierwszy ponieważ drugi gracz juz niema kart :)  ")

            print(player1)
            print("vs")
            print(player2)

            roundCounter += 1

            if not player1:
                print("Player 2 wins the game !")
                break
            elif not player2:
                print("Player 1 wins the game !")
                break

    def WinnerOfPlayer1(self, player1, player2):
        # Usuwanie i Dodawanie Kart
        player1.append(player2[0])
        player2.pop(0)
        player1.append(player1[0])
        player1.pop(0)

    def WinnerOfPlayer2(self, player1, player2):
        # Usuwanie i Dodawanie Kart
        player2.append(player1[0])
        player1.pop(0)
        player2.append(player2[0])
        player2.pop(0)

    def Create_Deck(self):
        print("Tworzymy talie 52 kart !")
        Deck = []
        x = 0
        while len(Deck) != 52:
            if x == 13:
                x = 0
            Deck.append(self.numbers[x])
            x += 1

        return Deck

    # Sortowanie widocznie na początku pętli
    def Sortowanie(self, Deck):
        Deck.sort()
        print(Deck)


Choise_Round_Of_Game = int(input("Podaj liczbę rund do rozegrania :"))
deck = Deck([], Choise_Round_Of_Game)
deck.War()