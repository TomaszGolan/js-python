
# Języki skryptowe - Python
## Wykład 9

---

* typy sekwencyjne: *set* i *frozenset*
* generatory
* omówienie zadań z listy 6

## Typy sekwencyjne 

---

* do tej pory poznaliśmy cztery typy sekwencyjne:
    * *str* - typ tekstowy
    * *list* - *mutowalna* sekwencja
    * *tuple* - *niemutowalna* sekwencja
    * *range* - *niemutowalna* sekwencja liczb

## Sekwencja *set*

---

* *set* jest *mutowalną* sekwencją
* różnice względem *list*
    * nie może zawierać duplikatów
    * jest nieuporządkowana
    * może zawierać tylko *hashowalne* obiekty

## Definiowanie *set*

---


```python
zbior = {1, 4, 6, 2, 1} # nawiasy klamrowe

type(zbior)
```




    set




```python
print(zbior)
```

    {1, 2, 4, 6}



```python
zbior[0] # nie ma indeksowania zbiorów
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-119e4f5506a9> in <module>()
    ----> 1 zbior[0] # nie ma indeksowania zbiorów
    

    TypeError: 'set' object does not support indexing


## *set* z *list*

---


```python
lista = [1, 4, 6, 2, 1]

zbior = set(lista) # stwórz zbiór na bazie listy

print(zbior)
```

    {1, 2, 4, 6}


## Dodawanie elementów do zbioru

---


```python
zbior = {1, 2, 3}

print(zbior)
```

    {1, 2, 3}



```python
zbior.add(4) # dodaj 4

print(zbior)
```

    {1, 2, 3, 4}



```python
zbior.add(4) # jeszcze raz dodaj 4

print(zbior) # nie ma duplikatów
```

    {1, 2, 3, 4}


## Elementy *niehashowalne*

---


```python
zbior = {1, 2, 3}

lista = [4, 5] # lista jest niehashowalna

# zbiór nie może przechowywać 
# elementów niehashowalnych
zbior.add(lista)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-c1da28ad9f1d> in <module>()
          5 # zbiór nie może przechowywać
          6 # elementów niehashowalnych
    ----> 7 zbior.add(lista)
    

    TypeError: unhashable type: 'list'


## Sekwencje hashowalne

---


```python
zbior = {1, 2, 3}

krotka = (4, 5) # krotka jest hashowalna

# więc można dodać krotkę
# do zbioru
zbior.add(krotka)

print(zbior)
```

    {(4, 5), 1, 2, 3}


## Usuwanie elementów ze zbioru

---


```python
zbior = {1, 2, 3}

zbior.remove(1) # usuń 1

print(zbior)
```

    {2, 3}



```python
# zwróci błąd jeśli element nie istnieje
zbior.remove(1)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-11-15d16e079b36> in <module>()
          1 # zwróci błąd jeśli element nie istnieje
    ----> 2 zbior.remove(1)
    

    KeyError: 1


## Bezpieczne usuwanie?

---


```python
zbior = {1, 2, 3}

# aby uniknąć błędów i przerwania programu
# można sprawdzić, czy na pewno element
# znajduje się w zbiorze
if 1 in zbior:
    zbior.remove(1)
```


```python
# lub skorzystać z try...except
try:
    zbior.remove(1)
except:
    pass
```


```python
# lub skorzystać z discard
zbior.discard(1)
```

## Zastosowanie zbiorów

---


```python
# usuwanie duplikatów z listy

lista = [2, 1, 2, 3, 4, 3, 2, 1, 5, 5, 2]

lista = list(set(lista))

# uwaga - tracimy kolejność
print(lista)
```

    [1, 2, 3, 4, 5]


## Część wspólna zbiorów

---


```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

A.intersection(B) # część wspólna A i B
```




    {3, 4, 5}




```python
# lub krócej
A & B
```




    {3, 4, 5}



## Część wspólna list

---


```python
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]

# rzutuje A i B na zbiory
# wyznacza ich część wspólną
# rzutuje na listę
wspolna = list(set(A) & set(B))

print(wspolna)
```

    [3, 4, 5]


## *frozenset*

---

* jak *set* ale *niemutowalny*, czyli nie można modyfikować zawartości


```python
zamrozony_zbior = frozenset([1, 2, 3, 4, 5])

type(zamrozony_zbior)
```




    frozenset




```python
zamrozony_zbior.add(1) # nie można dodawać / usuwać
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-20-c3b7844219a4> in <module>()
    ----> 1 zamrozony_zbior.add(1) # nie można dodawać / usuwać
    

    AttributeError: 'frozenset' object has no attribute 'add'


## Przykład - Totolotek

---


```python
from random import randint

# z wykładu 7

def losowanie():
    """Losuje 6 liczb od 1 do 49."""
    # nie jesteśmy zabezpieczni przed powtórzeniami
    return sorted([randint(1, 49) for _ in range(6)])

def check(a, b):
    """Sprawdza ilość takich samych elementów."""
    return len([n for n in a if n in b])

def play():
    """Gra w lotka."""
    lotto = losowanie() # losowanie lotto
    kupon = losowanie() # kupon chybił-trafił
    return check(kupon, lotto)
```

## Totolotek z *set*

---


```python
from random import randint

def losowanie():
    """Losuje 6 liczb od 1 do 49."""
    los = set() # tutaj zapiszemy wyniki losowania

    while len(los) < 6: # dodawaj aż 6 unikatów
        los.add(randint(1, 49))
    
    return los

def check(a, b):
    """Sprawdza ilość takich samych elementów."""
    return len(a & b)
```

## Totolotek - test

---


```python
lotto = losowanie()
kupon = losowanie()

print(lotto, kupon, sep="\n")
```

    {35, 7, 12, 16, 48, 29}
    {32, 10, 13, 26, 29, 31}



```python
check(lotto, kupon)
```




    1



## Totolotek z *frozenset*

---


```python
from random import sample

# frozenset bo losowania nie będziemy modyfikować

def losowanie():
    """Losuje 6 liczb od 1 do 49."""
    los = sample(range(1, 50), 6) # sample gwarantuje brak powtórzeń
    return frozenset(los) # zwracamy jako zamrożony zbiór

def check(a, b):
    """Sprawdza ilość takich samych elementów."""
    return len(a & b)
```

## Totolotek - test

---


```python
lotto = losowanie()
kupon = losowanie()

print(lotto, kupon, sep="\n")
```

    frozenset({37, 46, 48, 19, 25, 31})
    frozenset({38, 40, 41, 18, 19, 30})



```python
check(lotto, kupon)
```




    1



## Generatory

---

* funkcja, która zachowuje się jak iterator (czyli można np. wykorzystać ją w pętli)
* zamiast tworzyć całą listę obiektów, które będą przechowywane w pamięci
* oszczędza czas i pamięć

## Dygresja: *range*

---


```python
%timeit -n1 range(1000000) # tworzy obiekt range
```

    1 loop, best of 3: 1.68 µs per loop



```python
# kolejne elementy range
# muszą zostać zapisane w pamięci
%timeit -n1 list(range(1000000))
```

    1 loop, best of 3: 53.3 ms per loop


## Ciąg geometryczny

---


```python
def geometryczny(a1, q, n):
    """Generuje n wyrazów ciągu geometrycznego."""
    
    ciag = [a1]
    
    for _ in range(n-1): # n-1 bo pierwszy już jest
        ciag.append(ciag[-1]*q) # następny = poprzedni * iloraz
        
    return ciag
```


```python
ciag = geometryczny(1, 3, 10)

print(ciag)
```

    [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]


## Ciąg geometryczny - generator

---


```python
def gen_geometryczny(a1, q, n):
    """Generuje n wyrazów ciągu geometrycznego."""
    
    for _ in range(n):
        yield a1 # zwróć obecną wartość a1
        a1 *= q  # i czekaj na kolejną iterację
```

## Generator a lista

---


```python
ciag1 = geometryczny(1, 3, 10)     # zwraca listę 
ciag2 = gen_geometryczny(1, 3, 10) # zwraca generator
```


```python
print(ciag1)
```

    [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]



```python
print(ciag2)
```

    <generator object gen_geometryczny at 0x7f9bac1ec678>


## Generator jak iterator

---


```python
next(ciag2) # pierwszy element
```




    1




```python
next(ciag2) # kolejny element itd
```




    3




```python
# a najczęściej w pętli
for i in gen_geometryczny(1, 3, 10):
    print(i, end=', ')
```

    1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 

## Czas

---


```python
%timeit -n3 geometryczny(1, 3, 10000)
```

    3 loops, best of 3: 12.8 ms per loop



```python
%timeit -n3 gen_geometryczny(1, 3, 10000)
```

    3 loops, best of 3: 978 ns per loop


## Czas dokładniej

---


```python
def test_lista():
    """Pętla po liście"""
    for element in geometryczny(1, 3, 10000):
        pass
    
def test_generator():
    """Pętla po generatorze"""
    for element in gen_geometryczny(1, 3, 10000):
        pass
```


```python
%timeit -n3 test_lista()
```

    3 loops, best of 3: 13.6 ms per loop



```python
%timeit -n3 test_generator()
```

    3 loops, best of 3: 12.1 ms per loop


## Lista czy generator

---

* generator będzie z reguły szybszy
* generator może być nieskończony
* jednak nie można wykonywać operacji na "elementach", np. sortowania
* lista może być efektywniejsza, jeśli planujemy więcej pętli

## "Wyczerpanie" generatora

---


```python
ciag = gen_geometryczny(1, 3, 20) # generuje 20 wyrazów
```


```python
for i in range(10): # wydrukuj 10 pierwszych
    print(next(ciag), end=' ')
```

    1 3 9 27 81 243 729 2187 6561 19683 


```python
for element in ciag: # nie zaczyna od pierwszego!
    print(element, end=' ')
```

    59049 177147 531441 1594323 4782969 14348907 43046721 129140163 387420489 1162261467 

## Wielekrotne użycie

---


```python
def lista_loop(n=10):
    """Wykonuje n pętli po liście"""
    
    ciag = geometryczny(1, 3, 10000)
    
    for _ in range(n):
        for element in ciag:
            pass
    
def gen_loop(n=10):
    """Wykonuje n pętli po generatorze"""
    
    for _ in range(n):
        for element in gen_geometryczny(1, 3, 10000):
            pass
```


```python
%timeit -n3 lista_loop()
```

    3 loops, best of 3: 14.2 ms per loop



```python
%timeit -n3 gen_loop()
```

    3 loops, best of 3: 77.4 ms per loop


## Powtórka: listy składane (*list comprehensions*)

---


```python
# chcemy stworzyć listę zawierającą
# kwadraty wszystkich cyfr

kwadraty = []

for x in range(10):
    kwadraty.append(x**2)
    
print(kwadraty)
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



```python
# a korzystając z listy skladanej

kwadraty = [x**2 for x in range(10)]

print(kwadraty)
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


## Append vs lista składana

---


```python
def create_list(n=100000):
    """Tworzy listę kwadratów pierwszych n liczb naturalnych"""
    
    kwadraty = []
    
    for x in range(n):
        kwadraty.append(x**2)
        
    return kwadraty

def list_comprehension(n=100000):
    """Tworzy listę kwadratów pierwszych n liczb naturalnych"""
    
    return [x**2 for x in range(n)]
```

## Czas

---


```python
%timeit -n3 x = create_list() # lista tworzona przez append
```

    3 loops, best of 3: 48.3 ms per loop



```python
%timeit -n3 y = list_comprehension() # lista składana
```

    3 loops, best of 3: 42.5 ms per loop



```python
create_list() == list_comprehension() # wynik ten sam
```




    True



## Przykład

---


```python
def force(m, a):
    """Zwraca wartość siły [N].
    
    Liczy siłę jaką należy zadziałać na ciało
    o masie m [kg], aby nadać mu przyspieszenie a [m/s^2].
    """
    return m*a

wagi = [10, 20, 30, 40, 50] # kg
przyspieszenia = [1, 2, 3, 4, 5] # m/s^2
```


```python
# stwórz tablicę z wartościami sił 

sily = [force(m, a) for m, a in zip(wagi, przyspieszenia)]

print(sily)
```

    [10, 40, 90, 160, 250]


## Generator "jak lista składana"

---


```python
# lista składana
list_comprehension = [x**2 for x in range(10)]

# generator expression
generator = (x**2 for x in range(10))
```


```python
for x in generator:
    print(x, end=' ')
```

    0 1 4 9 16 25 36 49 64 81 


```python
# lub prościej

for x in (x**2 for x in range(10)):
    print(x, end=' ')
```

    0 1 4 9 16 25 36 49 64 81 

## Uwagi na koniec

---

* unikaj tworzenia list przez *append*, jeśli można wykorzystać *list comprehension*
* unikaj tworzenia list jeśli jest to zbędne (użyj generatorów)
* unikaj *generator function* na rzecz *generator expression*

## Próbne kolokwium - zadanie 1

---

Napisz skrypt, który wygeneruje listę zawierającą 100 pierwszych wyrazów ciągu geometrycznego (dla zadanych a1 i q - pierwszy wyraz ciągu i iloraz).

Następnie wydrukuje na ekranie ten ciąg oraz jego podciąg zawierający tylko parzyste wyrazy.

## Zadanie 1 - wersja I

---


```python
# podnoszenie q do potęgi jest bardzo czasochłonne!

def geometryczny_v1(a1, q, n):
    """Zwraca n-ty wyraz ciągu geometrycznego (a1, q)"""
    
    return a1*q**(n-1) # nie wymaga wyjaśnienia (oby...)
```


```python
# składamy listę na bazie naszej funkcji

ciag = [geometryczny_v1(1, 3, n+1) for n in range(100)]
```


```python
# print(ciag) # drukuje cały ciąg
# print(ciag[1::2]) # drukuje tylko parzyste wyrazy
```

## Zadanie 1 - wersja II

---


```python
def geometryczny_v2(a1, q, n, ciag=[]):
    """Tworzy listę n pierwszych wyrazów ciągu (a1, q)"""
    
    for _ in range(n):
        ciag.append(a1) # dodaj obecny wyraz
        a1 *= q         # następny wyraz
        
    return ciag
```


```python
ciag = geometryczny_v2(1, 3, 100)
```


```python
# print(ciag) # drukuje cały ciąg
# print(ciag[1::2]) # drukuje tylko parzyste wyrazy
```

## Zadanie 1 - wersja III

---


```python
def geometryczny_v3(a1, q, n):
    """Generator ciągu geometrycznego (a1, q)"""
    
    for _ in range(n):
        yield a1 # zwróć obecny wyraz i czekaj
        a1 *= q  # następny wyraz
```


```python
ciag = geometryczny_v3(1, 3, 100) # generator!
```


```python
# drukuj cały ciąg

# for x in ciag:
#     print(x, end=' ')

# nie ma wycinków generatorów
# ale można skorzystać z itertools.islice
```

## Zadanie 1 - wersja IV

---


```python
def geometryczny_v4(a1, q, n, ciag=[]):
    """Ciąg geometryczny (a1, q) rekurencyjnie"""
    
    if not n:
        return ciag # zwróć ciąg gdy dotrzemy do n
    
    ciag.append(a1) # dodaj obecny element
    # wywołaj rekurencyjnie z kolejnym elementem
    return geometryczny_v4(a1*q, q, n-1, ciag)
```


```python
ciag = geometryczny_v4(1, 3, 100)
```


```python
# print(ciag) # drukuje cały ciąg
# print(ciag[1::2]) # drukuje tylko parzyste wyrazy
```

## Próbne kolokwium - zadanie 2

---

Napisz funkcję, która sprawdza, czy podana liczba jest liczbą pierwszą. Funkcja powinna zwracać True lub False.

Napisz skrypt, który sprawdzi, czy podana przez użytkownika liczba jest liczbą pierwszą.

## Zadanie 2 - wersja I

---


```python
def is_prime_v1(n):
    """Sprawdza czy n jest liczbą pierwszą."""
    
    if n < 2:
        return False # 0 i 1 nie są pierwsze
    
    if n < 4:
        return True # 2 i 3 są pierwsze
    
    if n % 2 == 0:
        return False # parzyste nie są pierwsze
    
    i = 3
    
    while i < n:
        if n % i == 0:
            return False # dzieli się przez i
        i += 1

    return True # nie dzieli się przez nic    
```


```python
is_prime_v1(11)
```




    True



## Dygresja o dzielnikach

---

* Niech $n = a * b$
* Jeśli $a = b$, to $a = b = \sqrt(n)$
* Jeśli $a \neq b$, to albo $a < \sqrt(n)$ albo $b < \sqrt(n)$
* Co oznacza, że jeśli nie znajdziemy dzielnika mniejszego od $\sqrt(n)$, to nie znajdziemy og też dalej


## Zadanie 2 - wersja II

---


```python
def is_prime_v2(n):
    """Sprawdza czy n jest liczbą pierwszą."""
    
    if n < 2:
        return False # 0 i 1 nie są pierwsze
    
    if n < 4:
        return True # 2 i 3 są pierwsze
    
    if n % 2 == 0:
        return False # parzyste nie są pierwsze
    
    i = 3
    
    while i*i < n: # szukamy do pierwiastka z n
        if n % i == 0:
            return False # dzieli się przez i
        i += 1

    return True # nie dzieli się przez nic  
```


```python
is_prime_v2(11)
```




    True



## Sito Eratostenesa

---

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif">

## Implementacja

---


```python
def sieve_v1(n):
    """Create Sieve of Eratosthenes"""
    is_prime = [False, False] + [True] * n # ustaw flagi na True
    
    i = 2
    
    while i * i < n: # do pierwiastka z n
        if is_prime[i]:
            for j in range(2*i, n, i): # zmień flagę
                is_prime[j] = False    # dla wszystkich wielokrotności
        i += 1

    return is_prime
```


```python
primes = sieve_v1(100)

for i in range(100):
    if primes[i]:
        print(i, end=' ')
```

    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 

## Próbne kolokwium - zadanie 3

---

Napisz skrypt, który wymaga trzech argumentów z linii komend (wsk. sys.argv), czyli: `python moj_skrypt.py arg1 arg2 arg3`

które są długościami boków trójkąta (można założyć, że podane argumenty są liczbami). Na tej podstawie skrypt powinien wydrukować na ekranie następujące informacje:

* obwód i pole trójkąta
* informację czy trójkąt jest równoboczny, równoramienny czy różnoboczny
* informację czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny

W przypadku złej liczby argumentów program powinien wyświetlić odpowiedni komunikat i zakończyć działanie.

## Zadanie 3

---

* Pełny skrypt można znalęźć tutaj: [zadanie 3](https://raw.githubusercontent.com/TomaszGolan/js-python/master/src/triangle.py)

## Zadanie 3 - część I

---


```python
%%writefile zad3.py

"""Moduł do obsługi trójkątów."""

import sys
import math


def help():
    """Drukuje instrukcję obsługi i zamyka program"""

    print("usage: python triangle.py bok1 bok2 bok3")
    sys.exit(1)


def generate(a, b, c):
    """Zwraca posortowane boki trójkąta jako floaty."""

    return sorted([float(a), float(b), float(c)])
```

    Overwriting zad3.py


## Zadanie 3 - część II

---


```python
%%writefile -a zad3.py

def check(a, b, c):
    """Zamyka program, jeśli nierówność trójkąta nie jest spełniona."""

    if a + b <= c:
        print("Nierówność trojkąta nie jest spełniona.\n")
        help()


def obwod(a, b, c):
    """Zwraca obwód trójkąta"""

    return a + b + c


def pole(a, b, c):
    """Zwraca pole trójkąta"""

    p = obwod(a, b, c) / 2
    # wzór Herona
    return math.sqrt(p*(p - a)*(p - b)*(p - c))
```

    Appending to zad3.py


## Zadanie 3 - część III

---


```python
%%writefile -a zad3.py

def typ_boki(a, b, c):
    """Zwraca typ trójkąta (ze względu na boki)"""

    if a == b == c:
        return "równoboczny"
    elif a == b or b == c:
        return "równoramienny"
    else:
        return "różnoboczny"


def typ_katy(a, b, c):
    """Zwraca typ trójkąta (ze względu na kąty)"""

    x = a**2 + b**2 - c**2

    if x == 0:
        return "prostokątny"
    elif x > 0:
        return "ostrokątny"
    else:
        return "rozwartokątny"
```

    Appending to zad3.py


## Zadanie 3 - część IV

---


```python
%%writefile -a zad3.py

if __name__ == "__main__":

    try:
        a, b, c = generate(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        help()

    check(a, b, c)

    print("Obwód trójkąta =", obwod(a, b, c))
    print("Pole trójkąta =", pole(a, b, c))
    print("Trójkąt jest", 	typ_boki(a, b, c))
    print("Trójkąt jest", typ_katy(a, b, c))
```

    Appending to zad3.py


## Zadanie 3 - test

---


```python
%%bash

python zad3.py
```

    usage: python triangle.py bok1 bok2 bok3



```python
%%bash

python zad3.py 3 4 5
```

    Obwód trójkąta = 12.0
    Pole trójkąta = 6.0
    Trójkąt jest różnoboczny
    Trójkąt jest prostokątny


## Próbne kolokwium - zadanie 4

---

Korzystając z metody równego podziału (bisekcji) znajdź przybliżone miejsce zerowe funkcji: `f(x) = x**3 + 2*x*2 - 4*x - 10` w przedziale [1:3].

## Metoda bisekcji

---

* $f(x)$ jest ciągła w przedziale $[a, b]$
* i przyjmuje różne znaki na końcach przedziału $f(a)f(b) < 0$
* idea:
    * sprawdzamy, czy środek $x$ jest miejscem zerowym -> koniec
    * dzielimy przedział na dwa: $[a, x]$ i $[x, b]$
    * wybieramy przedział, dla którego znaki są różne na brzegach
    * powtarzamy do skutku

## Zadanie 4 

---


```python
def bisekcja(f, a, b, epsilon=0.0001):
    """Szuka miejsca zerowego f w [a, b] z dokładnością epislon.
    
    Zakładamy b > a oraz f(a)*f(b) < 0
    """
    
    while b - a > epsilon: # dopóki mieścimy się w epsilon
        x = (b + a) / 2    # środek przedziału
                
        if f(x) == 0:       # miejsce zerowe znalezione
            return x
        elif f(x)*f(a) < 0: # nowy przedział [a, x1]
            b = x
        else:               # nowy przedział [x1, b]
            a = x 
    
    return (b + a) / 2 # zwracamy przybliżoną wartość    
```

## Zadanie 4 - test

---


```python
def funkcja(x):
    return x**3 + 2*x**2 - 4*x - 10

x0 = bisekcja(funkcja, 1, 3)

print("x0 =", x0)
print("f(x0) =", funkcja(x0))
```

    x0 = 2.117950439453125
    f(x0) = 0.00014644321370838043

