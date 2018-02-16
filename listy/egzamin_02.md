% Języki skryptowe - Python
% Egzamin poprawkowy, XX.02.2018

Punktacja

```
for i in range(10, 5, -1): print("{} - {} -> {}".format(i - 1, i, i / 2))
```

---

## Zadanie 1 (1 pkt)

Napisz funkcję, która przyjmuje dwa argumenty: lista kluczy i lista wartości. Na podstawie podanych list tworzy i zwraca słownik. 

## Zadanie 2 (2 pkt)

(1 pkt) Napisz program, który drukuje wszystkie liczby podzielne przez 3 z przedziału podanego przez użytkownika.

(1 pkt) Zabezpiecz program przed nierozważnym użytkownikiem - program powinien pytać do skutku, aż użytkownik poda poprawne dane.

## Zadanie 3 (2 pkt)

Napisz program, który przyjmuje dwa argumenty z linii komend: ścieżkę do pliku oraz wyrażenie a następnie zlicza ile razy wyrażenie występuje w pliku.

## Zadanie 4 (2 pkt)

Niech

```
def ciag(n):
    """Zwraca n-ty wyraz ciągu"""
    return n * (n + 1)
```

(1 pkt) Napisz funkcję, która przyjmuje jeden argument (N) i zwraca N pierwszych wyrazów ciągu.

(1 pkt) Napisz funkcję, która przyjmuje jeden argument (max_value) i drukuje na ekranie wszystkie wyrazy ciągu mniejsze od max_value.

## Zadanie 5 (3 pkt)

Napisz klasę Egzamin, która posiada:

* słownik, którego kluczami są studenci a wartościami oceny
* *konstruktor*, w którym inicjowany jest pusty słownik
* metodę, która dodaje studenta z oceną do słownika
* metodę, która usuwa studenta ze słownika
* metodę, która drukuje studentów i ich oceny (posortowane wg ocen)
