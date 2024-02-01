biblioteka = []

#print(biblioteka)

def _znajdz_ksiazke(nazwa):
    for i in range(len(biblioteka)):
        if biblioteka[i]["nazwa"] == nazwa:
            return(i,biblioteka[i])
#zwraca tupla
        
def dodaj_ksiazke(nazwa,ilosc_stron, ocena,autor,rok_wydania,stan):
    check = _znajdz_ksiazke(nazwa)
    if check is not None:
        print("Taka książka już istnieje.")
        return
    biblioteka.append({
"nazwa": nazwa,
"ilosc_stron": ilosc_stron,
"ocena": ocena,
"czy_dostępna": True,
"autor" : autor,
"rok wydania" : rok_wydania,
"stan" : stan,
"ilość wypożyczeń" : 0})
    print("Dodano nową książke.")
    
#dodaj_ksiazke("harry potter", 200, 9)
#print(biblioteka)

def usun_ksiazke(nazwa):
    ksiazka = _znajdz_ksiazke(nazwa)
    if ksiazka is None:
        print("Taka ksiażka nie istnieje")  
    elif ksiazka [1]["czy_dostępna"]:
        biblioteka.remove(ksiazka[1])
        print("Ksiażka została pomyślnie usunięta")
    else:
        print("Nie można usunąć ksiąki, ponieważ nie jest dostępna")


def wypożycz_ksiazke(nazwa):
    book = _znajdz_ksiazke(nazwa)
    if book is not None:
        book = book[1]
        if book["czy_dostępna"]:
            print("wypożyczono")
            book["czy_dostępna"] = False
            book["ilość wypożyczeń"] += 1
        else:
            print(f"Nie można wypożyczyć książki {nazwa}, ponieważ jest ona już wypożyczona przez kogoś innego.")
    else:
        print("Taka książka nie została znaleziona")

def zwroc_ksiazke(nazwa):
    book = _znajdz_ksiazke(nazwa)
    if book is None:
        print(f"ksiązka {nazwa} nie została odnalezniona w systemie")
    else:
        book = book[1]
        if book["czy_dostępna"]:
            print(f"nie można zwrócic książki {nazwa} ponieważ nie jest ona wypożyczona")
        else:
            book["czy_dostepna"] = True
            print(f"książka {nazwa} została zwrócona")

def sprawdz_ksiazke(nazwa):
    indeks,book = _znajdz_ksiazke(nazwa)
    if book is None:
        print(f"Przykro nam, niestety nie posiadamy książki {nazwa} w naszej bibliotece")
    else:
        print(f"Witam, posiadamy książke {nazwa} w naszej bibliotece, szczegóły poniżej")
        print(f"Twoja książka znajduje sie na indeksie {indeks}")
        print(book)

# Metoda nieużywana
# def zmien_nazwe_ksiazki(nazwa,nowa_nazwa):
#     book = _znajdz_ksiazke(nazwa)
#     if book is None:
#         print("Nie ma takiej książki")
#     elif biblioteka["czy_dostępna"]:
#         biblioteka[nazwa] = nowa_nazwa
#         print(f"Ksiażka {nazwa} zmieniła nazwe na {nowa_nazwa}")
#     else:
#         print("Nie można zmienić nazwy książki ze względu na jej brak dostępności")

def zmien_parametr_ksiazki(nazwa,parametr,nowa_wartosc_parametru):
    book = _znajdz_ksiazke(nazwa)
    if book is None:
        print("Nie ma takiej książki")
    elif book[1]["czy_dostępna"]:
        book = book[1]
        if parametr in book.keys():
            book[parametr] = nowa_wartosc_parametru
            print(f"Parametr {parametr} został zmieniony na {nowa_wartosc_parametru}")
        else:
            print("Podany parametr nie jest poprawny")
    else:
        print("Nie można zmienić parametru książki ze względu na jej brak dostępności")

def wyswietl_wszystkie_ksiazki():
    if len(biblioteka) == 0:
        print("Brak książek")
    else:
        for book in biblioteka:
            print(_formatuj_ksizake(book))

def _formatuj_ksizake(book):
    return f"nazwa = {book['nazwa']}\nautor = {book['autor']}\nrok wydania = {book['rok wydania']}\n"

def dodaj_przykladowa_ksiazke():
    test_ksiazka = {
"nazwa": "piotruś pan", 
"ilość stron" : 300, 
"ocena": 10,
"czy_dostępna": True,
"ilość wypożyczeń" : 0,
"autor" : "James Barrie",
"rok wydania" : "1914",
"stan" : "dobry"

                        }
    biblioteka.append(test_ksiazka)






def uruchom_interfejs():
    print("Witaj w mojej bibliotece!")
    while True:
        odp=input("""
Wybierz jedną z poniższych opcji:
>Pokaż wszystko-pokaże wszystkie książki w bibliotece
>Pokaż książke-pokazuje informacje o książce
>Wypożycz-Daje możliwość wypożyczenia danej książki z biblioteki        
>Zwóć-Zwraca daną książke do biblioteki
>Dodaj książke-dodaje nową książke do biblioteki
>Usuń książke-usuwa wybraną książkę z biblioteki
>Edytuj książke-Umożliwia edytowanie parametrów książki

>Wyjdz-Wyjscie z biblioteki
użytkownik: """).lower()
        
        if odp == "pokaż wszystko":
            wyswietl_wszystkie_ksiazki()
        elif odp == "pokaż książke":
            odp = input("Podaj nazwę książki: ")
            book = _znajdz_ksiazke(odp)
            if book is None:
                print("Taka książka nie istnieje")
            else:
                print(book)
        elif odp == "dodaj książke":
            nazwa = input("Podaj nazwę książki: ")
            ilosc_stron = input("Podaj ilość stron: ")
            ocena = input("Podaj ocenę(1-10): ") 
            autor = input("Podaj autora książki: ")
            rok_wydania = input("Podaj rok wydania książki: ")
            stan = input("Podaj stan książki: ")
            dodaj_ksiazke(nazwa,ilosc_stron,ocena,autor,rok_wydania,stan)
            print(f"Książka została utworzona.")
        elif odp == "usuń książke":
            nazwa = input("Podaj nazwę książke ktąrą chcesz usunąć:")
            usun_ksiazke(nazwa)
        elif odp == "wypożycz":
            nazwa = input("Podaj nazwę książki którą chcesz wypożyczy:")
            wypożycz_ksiazke(nazwa)
        elif odp == "zwróć":
            nazwa = input("Podaj nazwę książki którą chcesz zwrócić:")
            zwroc_ksiazke(nazwa)
        elif odp == "edytuj książke":
            nazwa = input("Podaj nazwę książki którą chcesz edytować:")
            book = _znajdz_ksiazke(nazwa)
            if book is None:
                print("Taka książka nie istnieje")
                continue
            parametr = input("""Jaki parametr chcesz zmienić:
>Nazwa
>Ilość stron
>Ocena         
>Autor
>Rok wydania                            
>Stan                             
""").lower()
            
            if parametr not in ["nazwa","ilość stron","ocena","autor","rok wydania","stan"]:
                print("Podano niewłaściwy parametr")
                continue
            nowa_wartosc = input(f"Podaj nową wartość dla {parametr}: ")
        
            
            

            zmien_parametr_ksiazki(nazwa,parametr,nowa_wartosc)
            



        elif odp =="wyjdz":
            break
        else:
            print("Nie ma tekiego polecenia")
    print("Do zobaczenia ponownie!")
    

























    

