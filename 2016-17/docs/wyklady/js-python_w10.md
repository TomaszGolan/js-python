
# Języki skryptowe - Python
## Wykład 10

---

* klasy i obiekty, czyli pierwsze kroki w programowaniu obiektowym

## Programowanie strukturalne

---

* sekwencje (ciąg instrukcji)
* wybór (*if*)
* iteracja (pętle *for* i *while*)
* funkcje

## Słownik

---

* OOP - *Object-Oriented Programming*
* klasa - definicja obiektu
* instanacja (klasy) - obiekt utworzony na podstawie klasy

## Klasy

---

<div class="tree">
    <ul>
        <li><p>Klasa</p>
        <ul>
            <li><p>Atrybuty</p>
            <ul>
                <li><p>Dane</p>
                <li><p>Metody</p>
            </ul> 
        </ul>
    </ul>
</div>

## Przykład - klasa *complex*

---

<div class="tree">
    <ul>
        <li><p>complex</p>
        <ul>
            <li><p>Dane:</p>
            <ul>
                <li><p>real</p>
                <li><p>imag</p>
            </ul>
            <li><p>Metody:</p>
            <ul>
                <li><p>conjugate</p>
            </ul>
        </ul> 
    </ul>
</div>

## Klasa *complex*

---


```python
c = 10 + 5j # utwórz obiekt klasy int
```


```python
c.real # dane: real
```




    10.0




```python
c.imag # dane: imag
```




    5.0




```python
c.conjugate() # metody: conjugate
```




    (10-5j)



## Programowanie obiektowe

---

* tworzenie obiektów
    * mogą przechowywać dane
    * mogą wykonywać opearacje
    * przykład: klasa samochód
        * dane: moc, masa, moment obrotowy ...
        * metody: jedź, skręć, ...
* komunikacja między obiektami
    * przykład: klasa łyżka i klasa zupa
        * łyżka.pobierz(zupa)

## Klasa w Pythonie

---

```py
class Nazwa:
    instrukcje
    ...
```

* zbudujemy krok po kroku klasę trójkąt:
    * dane: boki a, b, c
    * metody: pole, obwód, typ...

## "Pusta" klasa

---


```python
class Triangle:
    pass
```


```python
# na razie klasa Triangle
# nie zawiera ani danych ani metod
# ale już możemy stworzyć obiekt typu Triangle

t = Triangle()
```


```python
type(t)
```




    __main__.Triangle



## Uwaga

---

* w Pythonie można dodawać atrybuty do istniejących obiektów (choć nie jest to zalecane!)


```python
t.a = 3.0 # atrybut a obiektu t
t.b = 4.0 # atrybut b obiektu t
t.c = 5.0 # atrybut c obiektu t

print(t.a, t.b, t.c) # drukuj atrybuty a, b, c
```

    3.0 4.0 5.0



```python
def drukuj(triangle): # każdy obiekt może być argumentem funkcji
    print(triangle.a, triangle.b, triangle.c)
    
drukuj(t)
```

    3.0 4.0 5.0


## Inicjalizacja

---

* `__init__` - prawie jak konstruktor, ale wywoływana **po** utworzeniu instancji
* *self* - odpowiednik *this* z c++


```python
class Triangle:
    """Dokumentacja jak w przypadku funkcji"""
    
    def __init__(self, a, b, c):
        """Prawie jak konstruktor"""
        self.a = a # zmiennej obiekt.a
        self.b = b # przypisz wartość a
        self.c = c # itd
```


```python
# wywołuje funkcję __init__(3, 4, 5)
t = Triangle(3, 4, 5)
```


```python
print(t.a, t.b, t.c)
```

    3 4 5


## *self*

---

* pierwszy argument każdej metody = *self*
* przyjęto konwencję *self*, ale może to być dowolna nazwa


```python
class Triangle:
    """Dokumentacja jak w przypadku funkcji"""
    
    def __init__(this, a, b, c):
        """Prawie jak konstruktor"""
        this.a = a
        this.b = b
        this.c = c
```


```python
# wywołuje funkcję __init__(3, 4, 5)
t = Triangle(3, 4, 5)
```


```python
print(t.a, t.b, t.c)
```

    3 4 5


## Dokumentacja

---


```python
help(t)
```

    Help on Triangle in module __main__ object:
    
    class Triangle(builtins.object)
     |  Dokumentacja jak w przypadku funkcji
     |  
     |  Methods defined here:
     |  
     |  __init__(this, a, b, c)
     |      Prawie jak konstruktor
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    


## Metody specjalne

---

* `__init__` jest jedną z metod specjalnych klasy
* [tutaj](https://docs.python.org/3/reference/datamodel.html#special-method-names) znajduje się pełna lista dostępnych metod specjalnych
* w trakcie wykładu pojawią się kolejne (wszystkie `__nazwa__`)

## *str* i *repr*

---

* `__repr__` - "oficjalna" reprezentacja obiektu, powinna być jednoznaczna; wywołana przez `repr(obiekt)` lub w interpreterze po wpisaniu nazwy zmiennej
* `__str__` - "nieformalna" reprezentacja obiektu, powinna być czytelna; wywołana przez `str(obiekt)` lub `print`

## *Triangle* : *str* i *repr*

---


```python
class Triangle:
    # pomijamy dokumentację: oszczędność slajdu
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self): # zwraca string
        return "Trójkąt o bokach: {}, {}, {}"\
                .format(self.a, self.b, self.c)
    
    def __repr__(self): # zwraca string
        return "Triangle({}, {}, {})"\
                .format(self.a, self.b, self.c)
```

## *Triangle* : *str* i *repr*

---


```python
t = Triangle(3, 4, 5)

print(t) # wywołuje __str__
```

    Trójkąt o bokach: 3, 4, 5



```python
t # wywołuje __repr__
```




    Triangle(3, 4, 5)



## Własne metody - obwód

---


```python
class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def obwod(self):
        # do zmiennych obiektu odwołujemy się
        # przez self.zmienna
        return self.a + self.b + self.c
```


```python
t = Triangle(3, 4, 5)
```


```python
t.obwod()
```




    12



## Własne metody - pole

---


```python
from math import sqrt

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def obwod(self):
        return self.a + self.b + self.c
    
    def pole(self):
        # do metod odwołujemy się
        # przez self.metoda
        p = self.obwod()/2
        return sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
```

## Test

---


```python
t = Triangle(3, 4, 5)

print("Obwód =", t.obwod())
print("Pole =", t.pole())
```

    Obwód = 12
    Pole = 6.0


## Klasa wektor

---

* współrzędne *x*, *y*, *z*
* długość wektora
* dodawanie wektorów
* mnożenie wektora przez liczbę
* iloczyn skalarny
* ...

## Wektor: długość

---


```python
from math import sqrt

class Wektor:
    """Trójwymiarowy wektor"""
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def norm(self):
        """Długość wektora"""
        return sqrt(self.x**2 + self.y**2 + self.z**2)
```

## Długość: test

---


```python
w = Wektor(1) # utwórz wektor (1, 0, 0)

w.norm()
```




    1.0




```python
w.x = 2 # zmień składową x

w.norm()
```




    2.0



## Zmienne prywatne

---


```python
class Wektor:
    """Trójwymiarowy wektor"""
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = x # zmienne "prywatne"
        self._y = y # sygnalizuje się _
        self._z = z
        
    def __str__(self):
        return "[{}, {}, {}]".format(self._x, self._y, self._z)
```

## Wektor prywatny

---


```python
from wektor import Wektor

w = Wektor(1) # utwórz wektor (1, 0, 0)

print(w)
```

    [1, 0.0, 0.0]



```python
# dostęp do _zmienna nie jest ograniczony
# jest to tylko wskazówka, żeby nie ruszać
w._x = 2.0

print(w)
```

    [2.0, 0.0, 0.0]


## Zmienne bardziej prywatne

---


```python
class Wektor:
    """Trójwymiarowy wektor"""
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.__x = x # zmienne zaczynające się __
        self.__y = y # zamieniane są na
        self.__z = z # _nazwa_klasy__zmienna
        
    def __str__(self):
        return "[{}, {}, {}]".format(self.__x, self.__y, self.__z)
```

## Wektor bardziej prywatny

---


```python
w = Wektor(1) # [1, 0, 0]

print(w)
```

    [1, 0.0, 0.0]



```python
w.__x = 2 # nie zmienia skladowej __x

print(w)
```

    [1, 0.0, 0.0]



```python
w._Wektor__x = 2 # zmienia składową __x

print(w)
```

    [2, 0.0, 0.0]


## Dodawanie wektorów

---


```python
class Wektor:
    """Trójwymiarowy wektor"""
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)
        
    def __add__(self, w): # operator dodawania
        return Wektor(self.x + w.x, self.y + w.y, self.z + w.z)
```

## Dodawanie: test

---


```python
x = Wektor(1, 2, 3)
y = Wektor(2, 4, 6)

print(x + y) # wywołuje x.__add__(y)
```

    [3, 6, 9]


## Wektor: iloczyn skalarny

---


```python
class Wektor:
    """Trójwymiarowy wektor"""
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)
        
    def __mul__(self, w): # operator mnożenia
        return self.x*w.x + self.y*w.y + self.z*w.z
```

## Iloczyn skalarny: test

---


```python
x = Wektor(1, 2, 3)
y = Wektor(2, 4, 6)

print(x*y) # wywołuje x.__mul__(y)
```

    28


## Mnożenie przez liczbę

---


```python
class Wektor:
    """Trójwymiarowy wektor"""
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)
        
    def __mul__(self, w): # operator mnożenia
        if type(w) == type(self): # dla wektora - iloczyn skalarny
            return self.x*w.x + self.y*w.y + self.z*w.z
        else: # dla liczby - mnożenie składowych
            return Wektor(w*self.x, w*self.y, w*self.z)
```

## Mnożenie: test

---


```python
x = Wektor(1, 2, 3)
y = Wektor(2, 4, 6)

print(x*y) # wywołuje x.__mul__(y)
```

    28



```python
print(x*10) # mnoży wektor z przez 10
```

    [10, 20, 30]



```python
print(10*x) # nie działa...
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-43-c2e4c5ebcda6> in <module>()
    ----> 1 print(10*x) # nie działa...
    

    TypeError: unsupported operand type(s) for *: 'int' and 'Wektor'


## Mnożenie z prawej

---


```python
class Wektor:
    """Trójwymiarowy wektor"""
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)
        
    def __mul__(self, w): # operator mnożenia
        if type(w) == type(self): # dla wektora - iloczyn skalarny
            return self.x*w.x + self.y*w.y + self.z*w.z
        else: # dla liczby - mnożenie składowych
            return Wektor(w*self.x, w*self.y, w*self.z)
        
    def __rmul__(self, w): # mnożenie z prawej
        return self.__mul__(w)
```

## Mnożenie z prawej: test

---


```python
x = Wektor(1, 2, 3)

print(x*10)
```

    [10, 20, 30]



```python
print(10*x)
```

    [10, 20, 30]


## Klasa student

---

* imię, nazwisko, nr indeksu
* zliczanie studentów

## Atrybuty klasy

---

* zmienne wprowadzane poza `__init__` są traktowane jako atrybuty klasy, a nie obiektu


```python
class Student:
    counter = 0 # licznik studentów
    
    def __init__(self, imie, nazwisko, indeks):
        self.__class__.counter += 1
        self.imie = imie
        self.naziwsko = nazwisko
        self.indeks = indeks
```

## Studenci

---


```python
student1 = Student("Jan", "Kowalski", 1234)
student2 = Student("Anna", "Nowak", 1234)

# każdy student ma swoje imię
print(student1.imie, student2.imie)
```

    Jan Anna



```python
# ale licznik jest wspólny
# dla wszystkich obiektów klasy Student
print(student1.counter, student2.counter)
```

    2 2


## Ciąg arytmetyczny

---

* zadany przez pierwszy wyraz ciągu i różnicę
* przechowuje *n* pierwszych wyrazów ciągu
* *len(ciąg)* zwraca *n*
* *sum(ciąg)* zwraca sumę *n* wyrazów

## Ciąg arytmetyczny: *init*

---


```python
%%writefile arciag.py

class ArCiag:
    """Ciąg arytmetyczny"""
    
    def __init__(self, a1, r, n=1):
        """Inicjuje ciąg arytmetyczny
        
        a1 -- pierwszy wyraz ciągu
        r -- różnica
        n -- początkowa liczba wyrazów
        """
        
        self.__a1 = a1
        self.__r = r
        self.__wyrazy = [a1]
        
        if n > 1:
            self.generate(n - 1)
```

    Overwriting arciag.py


## Ciąg arytmetyczny: *str*

---


```python
%%writefile -a arciag.py

    def __str__(self):
        s = "Ciąg arytmetyczny ({a1}, {r}):".format(a1=self.__a1, r=self.__r)
        
        for wyraz in self: # skąd wie, jak po sobie iterować?
            s += " " + str(wyraz)
            
        return s
```

    Appending to arciag.py


## Ciąg arytmetyczny: *iter*

---


```python
%%writefile -a arciag.py

    def __iter__(self): # iterator ciągu
        """Umożliwia iterację po ciągu"""
        
        for a in self.__wyrazy:
            yield a
```

    Appending to arciag.py


## Ciąg arytmetyczny: *len*

---


```python
%%writefile -a arciag.py

    def __len__(self): # wywoływana przez len()
        """Zwraca ilość wyrazów ciągu"""
        
        return len(self.__wyrazy)
```

    Appending to arciag.py


## Ciąg arytmetyczny: *generate*

---


```python
%%writefile -a arciag.py

    def generate(self, n):
        """Generuje kolejne wyrazy ciągu"""
        
        for _ in range(n):
            self.__wyrazy.append(self.__wyrazy[-1] + self.__r)
```

    Appending to arciag.py


## Ciąg arytmetyczny: *save*

---


```python
%%writefile -a arciag.py

    def save(self, filename):
        """Zapisuje ciąg do pliku"""
        
        with open(filename, 'w') as f:
            f.write(self.__str__())
```

    Appending to arciag.py


## Ciąg arytmeytczny: dokumentacja

---


```python
from arciag import ArCiag

help(ArCiag)
```

    Help on class ArCiag in module arciag:
    
    class ArCiag(builtins.object)
     |  Ciąg arytmetyczny
     |  
     |  Methods defined here:
     |  
     |  __init__(self, a1, r, n=1)
     |      Inicjuje ciąg arytmetyczny
     |      
     |      a1 -- pierwszy wyraz ciągu
     |      r -- różnica
     |      n -- początkowa liczba wyrazów
     |  
     |  __iter__(self)
     |      Umożliwia iterację po ciągu
     |  
     |  __len__(self)
     |      Zwraca ilość wyrazów ciągu
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  generate(self, n)
     |      Generuje kolejne wyrazy ciągu
     |  
     |  save(self, filename)
     |      Zapisuje ciąg do pliku
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    


## Ciąg arytmetyczny: test

---


```python
from arciag import ArCiag

x = ArCiag(1, 2)     # domyślnie jeden wyraz
y = ArCiag(2, 3, 10) # zacznij od 10 wyrazów

print(x)
print(y)
```

    Ciąg arytmetyczny (1, 2): 1
    Ciąg arytmetyczny (2, 3): 2 5 8 11 14 17 20 23 26 29


## Ciąg arytmetyczny: *len* i *sum*

---


```python
from arciag import ArCiag

x = ArCiag(1, 2) # domyślnie 1 wyraz

x.generate(10) # generuj kolejne 10

print(x)
```

    Ciąg arytmetyczny (1, 2): 1 3 5 7 9 11 13 15 17 19 21



```python
len(x) # ilość wyrazów (dzięki __len__)
```




    11




```python
sum(x) # suma wyrazów (dzięki __iter__)
```




    121



## Ciąg arytmetyczny: zapis


```python
from arciag import ArCiag

x = ArCiag(1, 2, 10) # generuj 10 wyrazów

x.save('moj_ciag.txt') # i zapisz do pliku
```


```python
%%bash

cat moj_ciag.txt
```

    Ciąg arytmetyczny (1, 2): 1 3 5 7 9 11 13 15 17 19

## Ciąg geometryczny

---

* gdybyśmy chcieli stworzyć analogiczną klasę dla ciągu geometrycznego, to różnica pojawiłaby się tylko w funkcji `generate`
* istnieje mechanizm, który umożliwia klasom posiadanie wspólnych metod
* omówiony zostanie na kolejnym wykładzie


```python
s = """
<style>

* {margin: 0; padding: 0;}

.tree ul {
	padding-top: 20px; position: relative;
}

.tree li {
	float: left; text-align: center;
	list-style-type: none;
	position: relative;
	padding: 20px 5px 0 5px;
}

.tree li::before, .tree li::after{
	content: '';
	position: absolute; top: 0; right: 50%;
	border-top: 1px solid #ccc;
	width: 50%; height: 20px;
}

.tree li::after{
	right: auto; left: 50%;
	border-left: 1px solid #ccc;
}

.tree li:only-child::after, .tree li:only-child::before {
	display: none;
}

.tree li:only-child{ padding-top: 0;}

.tree li:first-child::before, .tree li:last-child::after{
	border: 0 none;
}

.tree li:last-child::before{
	border-right: 1px solid #ccc;
	border-radius: 0 5px 0 0;
	-webkit-border-radius: 0 5px 0 0;
	-moz-border-radius: 0 5px 0 0;
}

.tree li:first-child::after{
	border-radius: 5px 0 0 0;
	-webkit-border-radius: 5px 0 0 0;
	-moz-border-radius: 5px 0 0 0;
}

.tree ul ul::before{
	content: '';
	position: absolute; top: 0; left: 50%;
	border-left: 1px solid #ccc;
	width: 0; height: 20px;
}

.tree li p {
	border: 1px solid #ccc;
	padding: 15px 15px;
	text-decoration: none;
	color: #666;
	font-family: arial, verdana, tahoma;
	font-size: 40px;
	display: inline-block;
	
	border-radius: 5px;
	-webkit-border-radius: 5px;
	-moz-border-radius: 5px;
}

</style>
"""

from IPython.display import display, HTML

display(HTML(s))
```



<style>

* {margin: 0; padding: 0;}

.tree ul {
	padding-top: 20px; position: relative;
}

.tree li {
	float: left; text-align: center;
	list-style-type: none;
	position: relative;
	padding: 20px 5px 0 5px;
}

.tree li::before, .tree li::after{
	content: '';
	position: absolute; top: 0; right: 50%;
	border-top: 1px solid #ccc;
	width: 50%; height: 20px;
}

.tree li::after{
	right: auto; left: 50%;
	border-left: 1px solid #ccc;
}

.tree li:only-child::after, .tree li:only-child::before {
	display: none;
}

.tree li:only-child{ padding-top: 0;}

.tree li:first-child::before, .tree li:last-child::after{
	border: 0 none;
}

.tree li:last-child::before{
	border-right: 1px solid #ccc;
	border-radius: 0 5px 0 0;
	-webkit-border-radius: 0 5px 0 0;
	-moz-border-radius: 0 5px 0 0;
}

.tree li:first-child::after{
	border-radius: 5px 0 0 0;
	-webkit-border-radius: 5px 0 0 0;
	-moz-border-radius: 5px 0 0 0;
}

.tree ul ul::before{
	content: '';
	position: absolute; top: 0; left: 50%;
	border-left: 1px solid #ccc;
	width: 0; height: 20px;
}

.tree li p {
	border: 1px solid #ccc;
	padding: 15px 15px;
	text-decoration: none;
	color: #666;
	font-family: arial, verdana, tahoma;
	font-size: 40px;
	display: inline-block;
	
	border-radius: 5px;
	-webkit-border-radius: 5px;
	-moz-border-radius: 5px;
}

</style>


