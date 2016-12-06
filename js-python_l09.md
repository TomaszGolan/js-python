# Języki skryptowe - Python
# Lista 9

---

Zad 1.

Stwórz klasę `Samochod`, która:

* posiada dane:

    * maksymalna prędkość
    * spalanie
    * obecna prędkość (0 na starcie)
    * pokonany dystans (0 na starcie)
    * czas podróży (0 na starcie)
    
* posiada metody:

    * `przyspiesz`, która zwiększa prędkość o podaną wartość (aż do osiągnięcia prędkości maksymalnej)
    * `zwolnij`, która zmniejsza prędkość o podaną wartość (aż do 0)
    * `hamuj`, która zatrzymuje samochód
    * `turbo`, która przyspiesza samochód do maksymalnej prędkości
    * `jedz`, która zmienia pokonany dystans o podaną wartość oraz aktualizuje czas podróży
    * `podroz`, która podsumowuje podróż, drukując na ekranie: całkowity pokonany dystans, czas podróży, średnią prędkość, ilość spalonej benzyny
    
Stwórz obiekt klasy `Samochód` i przetestuj działanie, np.:


```
samochod = Samochod(200, 10) 

samochod.przyspiesz(100) # samochód jedzie 100km/h

samochod.jedz(100) # dystans = 100km, czas = 1h

samochod.turbo() # prędkość = 200km/h

samochod.jedz(100) # dystans = 100 + 100km, czas = 1 + 0.5h

samochod.podroz()

*Samochód przejechał ..., ze średnią prędkością ..., co zajęło ... i spaliło ... benzyny.*

---

Zad 2.

Zaskocz prowadzącego i stwórz swoją własną klasę, która robi coś ciekawego.

i / lub

Zmodyfikuj klasę z pierwszego zadania, aby zapamiętywane były informacje o kolejnych odcinkach (wywoływanych funkcją `jedz`). Dodaj funkcje, które umożliwią rysowanie wykresu zależności drogi od czasu oraz prędkości od czasu. *Wsk. matlibplot, wykorzystywany wielokrotnie na wykładach*
