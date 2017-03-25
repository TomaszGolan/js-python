# Języki skryptowe - Python
# Lista 8

---

Zad 1.

Napisz skrypt, który tworzy listę (wykorzystaj *list comprehension*) zawierającą *n* pierwszych wyrazów ciągu: *an = n/(n + 1)*, gdzie *n* jest parametrem podanym z linii komend.

Następnie w pętli zapisuje wszystkie wyrazy ciągu do pliku.

---

Zad 2.

Napisz drugą wersję skryptu z pierwszego zadania, który wykorzystuje *generator expression* zamiast *list comprehension*.

---

Zad 3.

Wykorzystując */usr/bin/time* (nie mylić z wbudowaną funkcją *time*) porównaj zużycie procesora oraz pamięci przez skrypty z pierwszych zadań dla różnych wartości *n*. Wyjaśnij otrzymane wyniki.

Zastąp zapisywanie do pliku pustą pętlą (`for _ in lista/generator: pass`) i sprawdź, jak to wpływa na pomiar czasu.

---

Zad 4.

Plik [studenci_python.txt](src/studenci_python.txt) zawiera listę studentów uczęszczających na wykład z Pythona.

Plik [studenci_cpp.txt](src/studenci_cpp.txt) zawiera listę studentów uczęszczających na wykład z C++.

Napisz skrypt, który wydrukuję listę studentów uczęszczających na oba wykłady.

*Wsk: set.intersection*

---

Zadanie dla chętnych

Napisz skrypt, który dla zadanego *n* generuje *n* pierwszych wyrazów ciągu "look-and-say".

*Wsk: [itertools.groupby](https://docs.python.org/3.6/library/itertools.html#itertools.groupby)*
