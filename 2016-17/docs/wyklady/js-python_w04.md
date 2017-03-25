
# Jęzki skryptowe - Python
## Wykład 4

---

* typy mapujące: *dict*
* funkcje
* dokumentacja
* wyrażenie lambda

## Złożone typy danych

---

* typy sekwencyjne ("mutowalne"): *list*
* typy sekwencyjne ("niemutowalne"): *tuple*, *range*, *str*

---

* typy mapujące ("mutowalne"): *dict*

## Słownik (*dict*)

---

* mapuje obiekty hashowalne (*hashable*) w dowolne obiekty, czyli: *klucz: wartość*
    * *klucz* - stały hash
    * *wartość* - dowolny obiekt
* np. krotka może być kluczem, ale lista już nie
* słowniki tworzymy umieszczając oddzielone przecinkiem pary *key: value* w nawiasach klamrowych, np.


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

print(slownik)
```

    {'Kasia': 7236, 'Basia': 5286, 'Darek': 7738, 'Marek': 9807}


## Słownik przez konstruktor

---


```python
# {key1: value1, key2: value2...}
a = {"jeden": 1, "dwa": 2, "trzy": 3}
# dict(key1=value1, key2=value2...)
b = dict(jeden=1, dwa=2, trzy=3) 
# dict([(key1, value1), (key2, value2)...])
c = dict(zip(["jeden", "dwa", "trzy"], [1, 2, 3]))
# dict(słownik)
d = dict(a)

a == b == c == d
```




    True



## Słownik - dostęp do wartości

---


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

slownik["Kasia"] # dostęp -> dict[key]
```




    7236




```python
slownik[0] # słownik nie jest uporządkowany
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-4-8f2cb9210d58> in <module>()
    ----> 1 slownik[0] # słownik nie jest uporządkowany
    

    KeyError: 0


## Słowniki - dostęp do wartości

---


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

print(slownik["Kasia"]) # Kasia jest w słowniku -> OK
print(slownik["Ania"])  # Ani nie ma -> KeyError
```

    7236



    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-5-7f55cd27f397> in <module>()
          3 
          4 print(slownik["Kasia"]) # Kasia jest w słowniku -> OK
    ----> 5 print(slownik["Ania"])  # Ani nie ma -> KeyError
    

    KeyError: 'Ania'


## Słowniki - dostęp do wartości

---


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

print(slownik.get("Kasia")) # Kasia jest w słowniku -> OK
print(slownik.get("Ania"))  # Ani nie ma -> default = None
print(slownik.get("Ania", 1234)) # Ani nie ma -> default = 1234
```

    7236
    None
    1234



```python
# czemu domyślnie None?
if slownik.get("Ania"):
    print(slownik["Ania"])
else:
    print("Brak studenta.")
```

    Brak studenta.



```python
# lub prościej
print(slownik.get("Ania") or "Brak studenta.")
```

    Brak studenta.


## Słownik - klucze i wartości

---


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}
```


```python
slownik.keys() # lista kluczy
```




    dict_keys(['Kasia', 'Basia', 'Darek', 'Marek'])




```python
slownik.values() # lista wartości
```




    dict_values([7236, 5286, 7738, 9807])




```python
slownik.items() # lista par
```




    dict_items([('Kasia', 7236), ('Basia', 5286), ('Darek', 7738), ('Marek', 9807)])



## Słownik - Python 2 vs 3

---

- w Pythonie 2 *dict.keys()*, *dict.values()* i *dict.items()* zwracają listy (czyli dopuszczalne jest np. *dict.keys()[0]*)
- w Pythonie 3:


```python
import collections # for Iterable

# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

# slownik.keys()[0] # TypeError: 'dict_keys' object does not support indexing

isinstance(slownik.keys(), list)
```




    False




```python
isinstance(slownik, collections.Iterable) # pętla po keys() -> OK
```




    True



## Słownik - modyfikacja kluczy

---


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

slownik["Kasia"] = 1234 # dict[key] = value

print(slownik)
```

    {'Kasia': 1234, 'Basia': 5286, 'Darek': 7738, 'Marek': 9807}



```python
slownik["Kasia"] += 1 # analogicznie do listy: list[index]

print(slownik)
```

    {'Kasia': 1235, 'Basia': 5286, 'Darek': 7738, 'Marek': 9807}


## Słownik - usuwanie kluczy

---


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

del slownik["Marek"] # del dict[key] -> usuń klucz

print(slownik)
```

    {'Kasia': 7236, 'Basia': 5286, 'Darek': 7738}



```python
slownik.clear() # wyczyść słownik
 
print(slownik)
```

    {}


## Słownik  - dodawanie kluczy

---


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

slownik["Ania"] = 3384 # jeśli jest to zmień, jeśli nie ma to dodaj

print(slownik)
```

    {'Kasia': 7236, 'Ania': 3384, 'Basia': 5286, 'Darek': 7738, 'Marek': 9807}



```python
nowi_studenci = {"Romek": 3343, "Basia": 8573}

slownik.update(nowi_studenci) # "dodaj/scal" słowniki
 
print(slownik) # zwróć uwagę na Basię
```

    {'Basia': 8573, 'Romek': 3343, 'Darek': 7738, 'Kasia': 7236, 'Ania': 3384, 'Marek': 9807}



```python
slownik.update(Józek=2276)

print(slownik)
```

    {'Basia': 8573, 'Romek': 3343, 'Darek': 7738, 'Józek': 2276, 'Kasia': 7236, 'Ania': 3384, 'Marek': 9807}


## Pętla po słowniku

---


```python
# student: numer indeksu
slownik = {"Kasia": 7236, "Basia": 5286, "Marek": 9807, "Darek": 7738}

for student in slownik.keys(): # pętla po kluczach
    print(student, end=' ')
```

    Kasia Basia Darek Marek 


```python
for index in slownik.values(): # pętla po wartościach
    print(index, end=' ')
```

    7236 5286 7738 9807 


```python
for student, index in slownik.items(): # pętla po (klucz, wartość)
    print(student, index)
```

    Kasia 7236
    Basia 5286
    Darek 7738
    Marek 9807


## Przykład - tworzenie słownika

---


```python
studenci = {} # stwórz pusty słownik

while True:
    # pobierz imię studenta
    student = input("Imię: ")
    # przerwij jeśli puste
    if not student: break # niezalecane, ale możliwe
    # pobierz numer indeksu
    index = input("Nr indeksu: ")
    # aktualizuj słownik
    studenci.update({student: index})
    
print(studenci)
```

    Imię: Kasia
    Nr indeksu: 1234
    Imię: Jasiu
    Nr indeksu: 0987
    Imię: 
    {'Kasia': '1234', 'Jasiu': '0987'}


## Słownik w słowniku

---


```python
Kasia = {"Wiek": 20, "Wzrost": 190, "Waga": 70}
Marek = {"Wiek": 22, "Wzrost": 180, "Waga": 80}

# klucz musi być hashowalny
# wartością może być dowolny obieky, np. słownik
studenci = {"Kasia": Kasia, "Marek": Marek}

# wydrukuj w pętli wszystkich studentów i ich atrybuty
for imie, wlasnosci in studenci.items():
    print("{student} ma {wiek} lat, "
          "{wzrost} cm wzrostu "
          "i waży {waga} kg.".format(
            student=imie,
            wiek=studenci[imie]["Wiek"],
            wzrost=studenci[imie]["Wzrost"],
            waga=studenci[imie]["Waga"])
          )
```

    Kasia ma 20 lat, 190 cm wzrostu i waży 70 kg.
    Marek ma 22 lat, 180 cm wzrostu i waży 80 kg.


## Funkcje

---

* funkcje (w programowaniu) to "wywoływalne bloki instrukcji"
* mogą (ale nie muszą) przyjmować argumenty
* mogą (ale nie muszą) zwracać obiekt
* raz napisana funkcja może być wykorzystywana wiele razy
* zwiększają czytelność kodu
* łatwiejsze debugowanie

## Definiowanie funkcji

---

```py
def nazwa_funkcji(argumenty):
    instrukcje
    ...
    return obiekt
```

1. słowo kluczowe *def*
2. nazwa funkcji
3. lista argumentów (opcjonalnie)
4. dwukropek
5. (wcięte) instrukcje
6. słowo kluczowe *return* (opcjonalnie)

## Funkcja "Hello World"

---


```python
def hello(): # brak argumentów
    print("Hello World!")
    # nic nie zwraca
    
hello() # wywołanie funkcji
```

    Hello World!


## Argumenty funkcji

---


```python
# funkcja dzialanie przyjmuje trzy argumenty a, b i c
# następnie zwraca wyrażenie a + b - c
def dzialanie(a, b, c):
    return a + b - c
```


```python
dzialanie(1, 2, 3) # zwróci 1 + 2 - 3
```




    0




```python
x = 1
y = 2

dzialanie(x, y, 2*x + 3*y) # zwróci 1 + 2 - 2*1 - 3*2 
```




    -5



## Argumenty funkcji

---


```python
def pobierz(komunikat): # funkcja przyjmuje jeden argument
    user_input = input(komunikat.ljust(20))
    return user_input   # zwraca dane użytkownika

imie = pobierz("Jak masz na imię?") # komunikat = "Jak masz na imię?"
wiek = pobierz("Ile masz lat?")     # komunikat = "Ile masz lat?"

print(imie, wiek)
```

    Jak masz na imię?   Józek
    Ile masz lat?       20
    Józek 20


## Argumenty ze słowem kluczowym

---


```python
# funkcja dzialanie przyjmuje trzy argumenty a, b i c
# następnie zwraca wyrażenie a + b - c
def dzialanie(a, b, c):
    return a + b - c
```


```python
dzialanie(1, 2, 3) # 3 argumenty pozycyjne
```




    0




```python
dzialanie(a=1, b=2, c=3) # 3 argumenty kluczowe
```




    0




```python
dzialanie(b=2, c=3, a=1) # kolejność nieważna dla argumentów kluczowych
```




    0



## Mieszanie argumentów

---


```python
# funkcja dzialanie przyjmuje trzy argumenty a, b i c
# następnie zwraca wyrażenie a + b - c
def dzialanie(a, b, c):
    return a + b - c
```


```python
dzialanie(1, c = 3, b = 2) # jeden pozycyjny, dwa kluczowe
```




    0




```python
dzialanie(a = 1, b = 2, 3) # najpierw pozycyjne, potem kluczowe!
```


      File "<ipython-input-38-60286ad5b769>", line 1
        dzialanie(a = 1, b = 2, 3) # najpierw pozycyjne, potem kluczowe!
                               ^
    SyntaxError: positional argument follows keyword argument



## Domyślne wartości argumentów

---


```python
def pobierz(komunikat):           # funkcja przyjmuje jeden argument
    user_input = input(komunikat) # pobiera dane od użytkownika
    return user_input             # i je zwraca
```


```python
x = pobierz() # funkcja oczekuje argumentu "komunikat"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-40-6184fdb92a47> in <module>()
    ----> 1 x = pobierz() # funkcja oczekuje argumentu "komunikat"
    

    TypeError: pobierz() missing 1 required positional argument: 'komunikat'


## Domyślne wartości argumentów

---


```python
def pobierz(komunikat='> '):      # domyślna wartość = "> "
    user_input = input(komunikat) # pobiera dane od użytkownika
    return user_input             # i je zwraca
```


```python
x = pobierz() # brak argumentu -> domyślna wartość
```

    > 1



```python
x = pobierz("Napisz coś: ") # nadpisanie wartości domyślne
```

    Napisz coś: 1


## Domyślne wartości argumentów

---


```python
# dwa ostatnie argumenty mają wartości domyślne
def dzialanie(a, b=2, c=3):
    return a + b - c
```


```python
dzialanie(1, 2, 3) == dzialanie(1)
```




    True




```python
# argumenty bez wartości domyślnych
# nie mogą występować po tych
# które wartości domyśne posiadają
def dzialanie(a=1, b, c):
    return a + b - c
```


      File "<ipython-input-46-21b67a48022e>", line 4
        def dzialanie(a=1, b, c):
                     ^
    SyntaxError: non-default argument follows default argument



## Argumenty "niemutowalne"

---


```python
def zwieksz(x):
    print("wewnątrz funkcji (przed) id(x) =", id(x))
    x += 1
    print("wewnątrz funkcji (po) id(x)=", id(x))

x = 0 # zmienna x wskazuje na dany obszar pamięci

print("Przed zwiększeniem x =", x)

print("id(x) = ", id(x))

zwieksz(x)

print("id(x) = ", id(x))

print("Po zwiększeniu x =", x)
```

    Przed zwiększeniem x = 0
    id(x) =  140266666990080
    wewnątrz funkcji (przed) id(x) = 140266666990080
    wewnątrz funkcji (po) id(x)= 140266666990112
    id(x) =  140266666990080
    Po zwiększeniu x = 0


## Argumenty "mutowalne"

---


```python
def zwieksz(x):
    print("wewnątrz funkcji (przed) id(x) =", id(x))
    x[0] += 1
    print("wewnątrz funkcji (po) id(x) () =", id(x))

x = [0] # zmienna x wskazuje na dany obszar pamięci

print("Przed zwiększeniem x =", x)

print("id(x) = ", id(x))

zwieksz(x)

print("id(x) = ", id(x))

print("Po zwiększeniu x =", x)
```

    Przed zwiększeniem x = [0]
    id(x) =  140266455152520
    wewnątrz funkcji (przed) id(x) = 140266455152520
    wewnątrz funkcji (po) id(x) () = 140266455152520
    id(x) =  140266455152520
    Po zwiększeniu x = [1]


## "Mutowalna" wartość domyślna

---


```python
# wartość domyślna jest inicjowana tylko raz
def update(N, L = []):
    L.append(N)
    return L

print(update(1)) # L wskazuje na obszar w pamięci
print(update(2)) # i tak już zostaje
print(update(3)) # dla każdego kolejnego wywołania
```

    [1]
    [1, 2]
    [1, 2, 3]


## Obejście problemu

---


```python
def update(N, L = None):
    if not L:
        L = []
    L.append(N)
    return L

print(update(1)) # z każdym wywołaniem funkcji
print(update(2)) # tworzona jest nowa lista
print(update(3))
```

    [1]
    [2]
    [3]


## Dowolna liczba argumentów (pozycyjnych)

---


```python
# funkcja przyjmuje dwa "normalne" argumenty
# z pozostałych powstanie krotka
def funkcja(arg1, arg2, *args):
    print(arg1, arg2, args)

funkcja('a', 'b', 'c', 'd', 'e', 'f')
```

    a b ('c', 'd', 'e', 'f')


## *args i key

---


```python
# po *args mogą występować tylko argumenty kluczowe
# mogą (ale nie muszą) mieć wartości domyślne
def funkcja(arg1, *args, kwarg1, kwarg2="key"):
    print("arg1 =", arg1)
    print("*args =", args)
    print("kwarg1 =", kwarg1)
    print("kwarg2 =", kwarg2)
    
funkcja('a', 'b', 'c', 'd', kwarg1="argument kluczowy")
```

    arg1 = a
    *args = ('b', 'c', 'd')
    kwarg1 = argument kluczowy
    kwarg2 = key



```python
funkcja('a', 'b', 'c', 'd')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-53-aa278ac540f2> in <module>()
    ----> 1 funkcja('a', 'b', 'c', 'd')
    

    TypeError: funkcja() missing 1 required keyword-only argument: 'kwarg1'


## Przykład

---


```python
# średnia z dowolnej liczby argumentów
def srednia(*args):
    if not args: # brak argumentów -> 0
        return 0
    return sum(args) / len(args)
```


```python
srednia()
```




    0




```python
srednia(1, 2, 3, 4)
```




    2.5




```python
srednia(*range(100))
```




    49.5



## Dowolna liczba argumentów (kluczowych)

---


```python
# *args -> krotka argumentów pozycyjnych
# **kwargs -> słownik argumentów kluczowych
def funkcja(**kwargs):
    for key, value in kwargs.items():
        print(key, value, type(value))
```


```python
funkcja(imie="Jan", nazwisko="Kowalski", wiek=25)
```

    imie Jan <class 'str'>
    wiek 25 <class 'int'>
    nazwisko Kowalski <class 'str'>



```python
funkcja("Jan", "Kowalski", 25)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-60-1c93f25ce1db> in <module>()
    ----> 1 funkcja("Jan", "Kowalski", 25)
    

    TypeError: funkcja() takes 0 positional arguments but 3 were given


## Forsowanie argumentów kluczowych

---


```python
# zwróć sumę a i b
# jeśli flaga==True zwróć 0
def moja_suma(a, b, flaga=False):
    if flaga:
        return 0
    else:
        return a + b
```


```python
moja_suma(1, 2) # dla dwóch argumentów działa OK
```




    3




```python
moja_suma(1, 2, 3) # flaga == 3
```




    0



## Forsowanie argumentów kluczowych

---


```python
# zwróć sumę a i b
# jeśli flaga==True zwróć 0
def moja_suma(a, b, *args, flaga=False):    
    if flaga:
        return 0
    else:
        return a + b
```


```python
moja_suma(1, 2)
```




    3




```python
moja_suma(1, 2, 3) # args=(3)
```




    3




```python
moja_suma(1, 2, flaga=True)
```




    0



## Forsowanie argumentów kluczowych

---


```python
# zwróć sumę a i b
# jeśli flaga==True zwróć 0
def moja_suma(a, b, *, flaga=False):    
    if flaga:
        return 0
    else:
        return a + b
```


```python
moja_suma(1, 2)
```




    3




```python
moja_suma(1, 2, 3) # nadmiarowy argument wywołuje błąd
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-70-f09f12e8bd26> in <module>()
    ----> 1 moja_suma(1, 2, 3) # nadmiarowy argument wywołuje błąd
    

    TypeError: moja_suma() takes 2 positional arguments but 3 were given


## Przykład

---


```python
def create_car(marka, model, **options):
    print(marka, model)
    for opcja, wartosc in options.items():
        print("  {}: {}".format(opcja, wartosc))
```


```python
create_car("Fiat", "126p", kolor="czarny", rocznik=1980)
create_car("Ford", "Mustang", kolor="różowy", moc="200KM", skrzynia="manualna")
```

    Fiat 126p
      kolor: czarny
      rocznik: 1980
    Ford Mustang
      moc: 200KM
      kolor: różowy
      skrzynia: manualna


## Argumenty ze słownika

---


```python
def create_car(marka, model, **options):
    print(marka, model)
    for opcja, wartosc in options.items():
        print("  {}: {}".format(opcja, wartosc))
        
ford_mustang = {"kolor": "różowy", "moc": "200KM", "skrzynia": "manualna"}

# **dict jako argument -> rozpakuj slownik
create_car("Ford", "Mustang", **ford_mustang)
```

    Ford Mustang
      moc: 200KM
      kolor: różowy
      skrzynia: manualna


## Funkcja jako rezultat funkcji

---


```python
def kwadrat(x):
    print("kwadrat({})".format(x))
    return x*x

def kwadrat_sumy(a, b):
    print("kwadrat_sumy({}, {})".format(a, b))
    return kwadrat(a + b) # return może zwrócić inną funkcję

wynik = kwadrat_sumy(2, 3)

print("wynik =", wynik)
```

    kwadrat_sumy(2, 3)
    kwadrat(5)
    wynik = 25


## Wynik funkcji jako argument funkcji

---


```python
def kwadrat(x):
    print("kwadrat({})".format(x))
    return x*x

def suma(a, b):
    print("suma({}, {})".format(a, b))
    return a + b

def kwadrat_sumy(a, b):
    print("kwadrat_sumy({}, {})".format(a, b))
    return kwadrat(suma(a, b)) # wynik funkcji jest argumentem

wynik = kwadrat_sumy(2, 3)

print("wynik =", wynik)
```

    kwadrat_sumy(2, 3)
    suma(2, 3)
    kwadrat(5)
    wynik = 25


## Funkcja jako argument funkcji

---


```python
def kwadrat(x):
    print("kwadrat({})".format(x))
    return x*x

def suma(a, b):
    print("suma({}, {})".format(a, b))
    return a + b

def kwadrat_sumy(a, b, f1, f2):
    print("kwadrat_sumy({}, {}, {}, {})".format(a, b, f1, f2))
    return f2(f1(a, b))

wynik = kwadrat_sumy(2, 3, suma, kwadrat) # funkcja jest argumentem

print("wynik =", wynik)
```

    kwadrat_sumy(2, 3, <function suma at 0x7f9254388d08>, <function kwadrat at 0x7f925438ed90>)
    suma(2, 3)
    kwadrat(5)
    wynik = 25


## Zmienne globalne

---


```python
zmienna_globalna = "Hello World!"

print("Zmienna globalna przed =", zmienna_globalna)

def zmien():
    # print("Wewnątrz funkcji przed =", zmienna_globalna) # not assigned yet
    zmienna_globalna = "Bye World!" # zmienna_globalna jest zmienną lokalną
    print("Wewnątrz funkcji po =", zmienna_globalna)
    
zmien()    

print("Zmienna globalna po =", zmienna_globalna)
```

    Zmienna globalna przed = Hello World!
    Wewnątrz funkcji po = Bye World!
    Zmienna globalna po = Hello World!


## Zmienne globalne

---


```python
zmienna_globalna = "Hello World!"

print("Zmienna globalna przed =", zmienna_globalna)

def zmien():
    global zmienna_globalna # sygnalizuje, że operujemy na zmiennej globalnej
    print("Wewnątrz funkcji przed =", zmienna_globalna)
    zmienna_globalna = "Bye World!"
    print("Wewnątrz funkcji po =", zmienna_globalna)
    
zmien()    

print("Zmienna globalna po =", zmienna_globalna)
```

    Zmienna globalna przed = Hello World!
    Wewnątrz funkcji przed = Hello World!
    Wewnątrz funkcji po = Bye World!
    Zmienna globalna po = Bye World!


## Rekurencja

---


```python
i = 0

def funkcja():
    global i # używaj zmiennej globalnej i
    i += 1
    print(i, end=' ')
    if i < 10:
        return funkcja() # wywołuje sama siebie
```


```python
funkcja()
```

    1 2 3 4 5 6 7 8 9 10 

## Rekurencja - silnia

---


```python
def silnia(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
```


```python
print("Klasycznie silnia(5) =", silnia(5))
```

    Klasycznie silnia(5) = 120



```python
def silnia(n):
    if n < 2:
        return 1 # 0! = 1, 1! = 1
    return n*silnia(n - 1)
```


```python
print("Rekurencyjnie silnia(5) =", silnia(5))
```

    Rekurencyjnie silnia(5) = 120


## Dokumentacja

---


```python
help(help)
```

    Help on _Helper in module _sitebuiltins object:
    
    class _Helper(builtins.object)
     |  Define the builtin 'help'.
     |  
     |  This is a wrapper around pydoc.help that provides a helpful message
     |  when 'help' is typed at the Python interactive prompt.
     |  
     |  Calling help() at the Python prompt starts an interactive help session.
     |  Calling help(thing) prints help for the python object 'thing'.
     |  
     |  Methods defined here:
     |  
     |  __call__(self, *args, **kwds)
     |      Call self as a function.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    


## Dokumentowanie własnych funkcji

---


```python
def funkcja():
    pass
```


```python
help(funkcja)
```

    Help on function funkcja in module __main__:
    
    funkcja()
    



```python
def funkcja():
    """To jest moja funkcja, która nic nie robi"""
    pass
```


```python
help(funkcja)
```

    Help on function funkcja in module __main__:
    
    funkcja()
        To jest moja funkcja, która nic nie robi
    


## Dokumentacja (PEP 257)

---

* dokumentacja (czyli tzw. *docstring*) wg standardów PEP 257:
    * jednolinjkowy opis
    ```py
    """Mój opis"""
    ```
    * wielolinijkowy opis
    ```py
    """Mój opis
    
    więcej opisu
    """
    ```

## Opis

---

* opis powinien krótki i jasny (i mieć sens), np:

```py

# taki opis nie ma sensu
def moja_funkcja(a, b):
    """moja_funkcja(a, b) -> a + b"""
    return a + b

# taki jest lepszy
def moja_funkcja(a, b):
    """Zwraca sumę podanych liczb"""
    return a + b
```

## Dokumentowanie zmiennych

---


```python
def reszta(a = 0, b = 0):
    """Zwraca resztę z dzielenia
    
    Keyword arguments:
    a -- licznik
    b -- mianownik
    """
    if not b:
        return 0
    return a%b
```


```python
help(reszta)
```

    Help on function reszta in module __main__:
    
    reszta(a=0, b=0)
        Zwraca resztę z dzielenia
        
        Keyword arguments:
        a -- licznik
        b -- mianownik
    


## Wyrażenie *lambda*

---


```python
def suma(a, b): # "klasyczna" funkcja
    return a + b
```


```python
lsuma = lambda a, b: a + b # "anonimowa" funkcja
```


```python
suma(1, 2) # wywołujemy funkcję suma
```




    3




```python
lsuma(1, 2) # wywołujemy wyrażenia lambda
```




    3



## Wyrażenie *lambda*

---


```python
def wrapper(funkcja):
    print("Wywołuję funkcję:", funkcja)
    funkcja()

def f():
    print("Hello World!")
    
wrapper(f)
```

    Wywołuję funkcję: <function f at 0x7f92543518c8>
    Hello World!



```python
wrapper(lambda: print("Hello World!"))
```

    Wywołuję funkcję: <function <lambda> at 0x7f92543517b8>
    Hello World!


## Wyrażenie *lambda*

---


```python
def increase(n):
    print("Teraz tworzę lambdę")
    return lambda x: x + n

inc2 = increase(2) # powiększ o 2
inc4 = increase(4) # inc4 = lambda x: x + 4
```

    Teraz tworzę lambdę
    Teraz tworzę lambdę



```python
inc2(10)
```




    12




```python
inc4(10)
```




    14



## Funkcja *main*

---

* najczęście program podzielony jest na pojedyczne funkcje
* zwiększa to czytelność kodu i ułatwia jego debugowanie
* funkcja main "steruje" programem - uruchamiana jest przy wywołaniu skryptu

## Funkcja *main*

---


```python
# skrypt.py

def start():
    print("Zaczynam program")
    
def operations():
    print("Wykonuje obliczenia")
    
def end():
    print("Kończę program")
    
# taki skrypt nic nie zrobi
# bo żadna funkcja nie jest wywołana
```

## Funkcja *main*

---


```python
# skrypt.py

def start():
    print("Zaczynam program")
    
def operations():
    print("Wykonuje obliczenia")
    
def end():
    print("Kończę program")

if __name__ == "__main__":
    start()
    operations()
    end()
```

    Zaczynam program
    Wykonuje obliczenia
    Kończę program

