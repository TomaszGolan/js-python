% Języki skryptowe - Python
% Egzamin, 01.02.2018

Punktacja

```
for i in range(10, 5, -1): print("{} - {} -> {}".format(i - 1, i, i / 2))
```

---

## Zadanie 1 (1 pkt)

Niech

```
small_letters = string.ascii_lowercase
capital_letters = string.ascii_uppercase
```

Napisz pętlę (bez użycia `range`), która wydrukuje na ekranie:

```
1. a -> A
2. b -> B
.
.
.
26. z -> Z
```

## Zadanie 2 (2 pkt)

(1 pkt) Napisz funkcję, która przyjmuje trzy argumenty: słownik, klucz, wartość. Jeśli klucz nie istnieje w słowniku, funkcja powinna go dodać i zwrócić prawdę. W przeciwnym wypadku funkcja powinna zwrócić fałsz.

(1 pkt) Niech

```
slownik = {}
klucze = ("foo", "bar", "baz", "qux", "bar", "baz", "quux")
wartosci = tuple(range(len(klucze)))
```

W pętli dodaj klucze i odpowiadające im wartości do słownika wykorzystując funkcję z pierwszej części zadania. W zależności od wyniku powinien być drukowany komunikat z informacją, czy dany klucz został dodany czy nie.   

## Zadanie 3 (2 pkt)

(1 pkt) Napisz program, który zapisuje wszystkie argumenty podane z linii komend do pliku (każdy argument od nowej linii). Np. wywołanie:

```
python program.py ala ma kota 1 2 3
```

powinno stworzyć plik `argumenty.txt` o zawartości:

```
ala
ma
kota
1
2
3
```

(1 pkt) Napisz program, który wczytuje plik `argumenty.txt` i drukuje na ekranie tylko te, które są liczbami całkowitymi podzielnymi przez 3.

## Zadanie 4 (2 pkt)

Napisz program, który liczy sumę wszystkich liczb z listy (łącznie z tymi, które zajmują się w listach wewnątrz listy). Przykłady:

```
[1, 2, 3] -> 6
[1, [2, 3], 4, 'a'] -> 10
[1, [2], [3, [4, 5, [6]]]] -> 21
```

## Zadanie 5 (3 pkt)

Napisz klasę do konwersji liczb na system rzymski. Klasa powinna zawierać:

* *konstruktor* inicjowany liczbą całkowitą z domyślna wartością 0
* metodę, która konwertuje liczbę całkowitą na system rzymski
* wywołanie funkcji `print` na obiekcie powinno drukować na ekranie informacje o liczbie, np.

```
Liczba 10 w systemie rzymskim to X.
```

* metodę, która umożliwia zmianę liczby





