# Języki skryptowe - Python
# Lista 4 - styczeń

---

Punktacja:

* 80-100: bdb
* 70-79: db+
* 60-69: db
* 50-59: dst+
* 40-49: dst

---

Każdy program powinien:

* zawierać co najmniej jedną klasę

    * każda klasa powinna być zdefiniowana w osobnym pliku i importowana do głównego programu
    * każda klasa powinna mieć zdefiniowane co najmniej dwie metody specjalne (np. `__init__` i `__str__`)

* wykorzystywać wyjątki (tam gdzie trzeba, albo chociaż raz na siłę, żeby poćwiczyć)

* posiadać dokumentację w docstring

* być napisany czytelnie (zrozumiałe nazwy zmiennych, komentarze itp.)

---

## Zadanie 1 (100 pkt) - Kantor

Napisz program do przeliczania walut. Kursy walut wczytywane z pliku `xml` (można pobrać np. z [nbp.pl](http://www.nbp.pl/home.aspx?f=/kursy/kursya.html)).

Główna klasa powinna być inicjalizowana ścieżką do pliku `xml`, np. `kursy = Kursy("/moja/ścieżka/do/pliku.xml")`.

Program powinien posiadać poniższe opcje:

* lista dostępnych kursów
* konwersja PLN <-> wybrana waluta
* konwersja wybrana waluta <-> wybrana waluta

---

## Zadanie 2 (100 pkt) - Monte Carlo

Napisz program do obliczania całki oznaczonej metodą Monte Carlo. Na wejściu program powinien przyjmować funkcję, przedział całkowania oraz ilość kroków. Końcowy wynik powinien być przedstawiony na wykresie (wykres funkcji, wizualizacja wylosowanych punktów / prostokątów, przybliżony wynik całkowania).

---

## Zadanie 3 (100 pkt) - GUI

Napisz dowolny program z graficznym interfejsem użytkownika (biblioteka dowolna). Program powinien posiadać kilka podstawowych elementów (jak przyciski, menu, pola tekstowe itp.).

*Uwaga: program dowolny, ale projekty trywialne będą nisko oceniane.*

---

## Zadanie 4 (100 pkt) - Gra

Korzystając z biblioteki Pygame stwórz prostą grę (pong, wąż, arkanoid... dowolna gra).

---

## Zadanie 5 (100 pkt) - własny projekt

Zaproponuj prowadzącemu swój własny projekt.
