# Języki skryptowe - Python
# Lista 10

---

Lista do samodzielnego wykonania w trakcie zajęć.

Pod koniec zajęć każdy wysyła swoje rozwiązania na maila.

Każde zadanie w osobnym pliku: nazwisko_imie_zad_[numer].py.

Proszę zlitować się nad prowadzącymi i zadbać o to, żeby kod był czytelny
i odpowiednio komentowany. Dłuższe programy proszę rozbijać na mniejsze funkcje.
Każda funkcja powinna być opisana *docstringiem*.

---

Zad 1.

Niech `poczatek` i `koniec` będą całkowitymi zmiennymi globalnymi. Napisz pętlę `for`, która drukuje na ekranie liczby całkowite ze zbioru `[poczatek, koniec]`.

---

Zad 2.

Niech `poczatek` i `koniec` będą całkowitymi zmiennymi globalnymi. Napisz pętlę `while`, która drukuje na ekranie liczby całkowite ze zbioru `[poczatek, koniec]`.

---

Zad 3.

Napisz funkcję, która liczy objętość prostopadłościanu. Funkcja powinna przyjmować trzy argumenty, które są długościami krawędzi. Wywołana z jednym argumentem powinna się domyślić, że chodzi o sześcian, czyli:

```
funkcja(a)       # zwraca objętość sześcianu
funkcja(a, b, c) # zwraca objętość prostopadłościanu
```

---

Zad 4.

Napisz skrypt, który pobiera od użytkownika dowolny tekst, a następnie drukuje na ekranie liczbę występujących w nim samogłosek.

---

Zad 5.

Napisz skrypt, który wymaga dwóch argumentów z linii komend:

```
python append.py file text
```

Program powinien:

* dodać *text* na koniec pliku *file* (od nowej linii)
* stworzyć *file*, jeśli nie istnieje
* zwracać odpowiedni komunikat i przerywać pracę programu, gdy podana została zła liczba argumentów
