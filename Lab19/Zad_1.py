def zapisz_do_pliku(kod):
    try:
        with open("kody.txt", "a") as f: #a - tryb dopisywania
            f.write(f"{kod}\n")
    except FileNotFoundError:
        print("Blad pliku kody.txt")


def dodaj(kod):
    if len(kod) != 6 and kod[2] != '-':
        raise Exception("Niepoprawny kod")
    for i, num in enumerate(kod):
        if i == 2:
            continue #ignorujemy -, zostal sprawdzony wczesniej
        if not num.isnumeric():
            raise Exception("Niepoprawny kod")
    zapisz_do_pliku(kod)


kod = input("Podaj kod pocztowy w formacie XX-XXX")
try:
    dodaj(kod)
    print("OK")
except Exception as e:
    print(e)