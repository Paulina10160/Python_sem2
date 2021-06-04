import sys

if len(sys.argv) == 3: #jesli podano dwa argumenty (z nazwami plikow) to laczna ilosc argumentow bedzie 3 bo argument 0 to sciezka skrypu
    plik1 = sys.argv[1] #pobieamy pierwszy argument z wywolania skrypu
    plik2 = sys.argv[2] #tutaj drugi
else:
    plik1 = input("Podaj nazwe pliku nr 1")
    plik2 = input("Podaj nazwe pliku nr 2")


def wczytaj(plik):
    wiersze = [] #oznaczam jako pusty na wypadek jak by sie nie wczytalo z pliku ponizej
    try:
        with open(plik, "r") as f:
            wiersze = f.readlines()
    except FileNotFoundError: #wyjatek wystapi jesli plik o podanej nazwie nie istnieje
        print(f"Brak pliku {plik}")
    return wiersze

wiersze1 = wczytaj(plik1)
wiersze2 = wczytaj(plik2)

#zapisujemy ktory plik ma wiecej wierszy
dl = len(wiersze1) if len(wiersze1) > len(wiersze2) else len(wiersze2)

for i in range(dl):
    if i < len(wiersze1):
        print(wiersze1[i], end="")
    if i < len(wiersze2):
        print(wiersze2[i], end="")