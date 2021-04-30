class Book:
    def __init__(self, author, title, frame, pages, exampleText):
        self.title = title
        self.author = author
        self.frame = frame
        self.pages = pages
        self.exampleText = exampleText
    def SayMyName(self):
        print(self.author)
        print(self.title)
        print(self.frame)
        print(self.pages)
        print(self.exampleText)
nowaKsiazka = Book("Sapkowski Andrzej", "Wiedźmin - ostatnie rozszczenie", "hard", 300, "jakiś tekst")
books = []
def Main():
    books.append(nowaKsiazka)
    print("Witaj!")
    AnalizeChoice()
    while True:
        choice = input("Czy chcesz wykonać jeszcze jakąś operację? Tak / Nie")
        if choice == "Tak":
            AnalizeChoice()
        else:
            break
def AnalizeChoice():
    choice = input("Czy chcesz dodać nową książke lub wyświetlić listę obecnie istniejących książek? wybierz 1 lub 2")
    if (choice == "1"):
        AddBook()
    else:
        ShowBooks()
def AddBook():
    author = input("Podaj autora: Nazwisko Imie")
    title = input("Podaj tytuł")
    frame = input("Podaj rodzaj oprawy")
    pages = int(input("Podaj ilość stron"))
    exampleText = input("Podaj przykładowy fragment tekstu")
    book = Book(author, title, frame, pages, exampleText)
    print("Dodano nową książke!")
    books.append(book)
def ShowBooks():
    for i in books:
        i.SayMyName()
Main()