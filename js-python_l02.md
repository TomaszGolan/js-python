# Języki skryptowe - Python
# Lista 2

---

Zad 1.

* Stwórz krotkę (*tuple*) zawierającą pięć cyfr: 0, 1, 2, 3, 4 oraz pięć literałów słownych: "pięć", "sześć", "siedem", "osiem", "dziewięć".

* Wydrukuj na ekranie trzy pierwsze elementy.

* Wydrukuj na ekranie 2 ostatnie elementy.

* Wydrukuj co drugi element (zaczynając od drugiego).

* Korzystając z funkcji *len* sprawdź ilość elementów w krotce oraz długość przedostatniego elementu.

* Niech `x` oznacza nazwę krotki. Wykonaj:

    * x[:5] + (5, 6) + x[-3:]
    * x[:5], (5, 6), x[-3:]
    * porównaj otrzymane wyniki

* Dodaj pusty literał słowny na koniec krotki. Czy możesz skorzystać z funkcji *append*?

---

Zad 2.

* Stwórz listę studentów: Kasia, Basia, Marek, Darek.

* Korzystając z funkcji *append* dodaj do listy Józka.

* Korzystając z funkcji *extend* dodaj do listy Anię i Basię.

* Posortuj alfabetycznie studentów.

* Wypisz na ekranie:

    * czwartego studenta na liście
    * dwóch pierwszych studentów na liście
    * dwóch ostatnich studentów na liście

* Korzystając z funkcji *remove* usuń wszystkie Basie.

* Korzystając z funkcji *len* sprawdź ilość studentów.

* Z ostatecznej listy studentów utwórz krotkę.

---

Zad 3.

* Korzystając z `range` utwórz listę zawierającą wszystkie wielokrotności liczby 3 mniejsze od 100.

* Korzystając z `del` usuń co trzeci element (zaczynając od piątego).

* Sprawdź definicję funkcji wbudowanej *sum* (`help(sum)`). Wykorzystaj ją oraz funkcję *len*, aby wyliczyć średnią arytmetyczną otrzymanej listy.

---

Zad 4.

* Stwórz krotkę: `('a', 'b', 'c', 'd')`.

* Zapoznaj się z dokumentacją funkcji `str.join`.

* Wykonaj następujące polecenia (gdzie `x` to zmienna wskazująca na krotkę):

```py
"".join(x)
" ".join(x)
", ".join(x)
```

* Wydrukuj na ekranie 100 zer oddzielonych tabulacjami (spróbuj wykonać to komendą jednolinijkową).

---

Zad 5.

* Stwórz obiekt typu *str*, który przechowuje tekst ślubowania studenta:

```py
slubowanie = """
wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
- zdobywać wiedzę i umiejętności,
- postępować zgodnie z prawem, tradycją i dobrymi obyczajami akademickimi,
- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
"""
```

* W interpreterze sprawdź wynik:


```
>>> print(slubowanie)
>>> slubowanie
>>> slubowanie[0]
```

* Popraw zmienną `slubowanie`, aby tekst zaczynał się wielką literą.

* Korzystając z funkcji *count* sprawdź, ile razy występuje spójnik "i".

* Korzystając z funkcji *count* sprawdź, ile razy występuje litera "i".

* Korzystając z *in* sprawdź, czy słowo "Uniwersytet" występuje w tekście.

* Korzystając z funkcji *str.split*:

    * stwórz listę wyrazów występujących w tekście (30 słów => 30 elementów)
    * stwórz listę, której każdy element odpowiada jednej linijce tekstu (4 linie => 4 elementy)

---

Zad 6.

* Korzystając z funkcji *sys.getsizeof* sprawdź, ile pamięci zajmuje:
    * 0
    * 2**100
    * 2**1000

* Sprawdź, ile pamięci zajmują: *True* i *False*. Czy jest to wynik, którego się spodziewałeś?

* Zapoznaj się z dokumentacją funkcji *isinstance*.

* Wykonaj następujące polecenia:

```py
isinstance(0, int)
isinstance(0, float)
isinstance(0.0, float)
isinstance(True, bool)
isinstance(True, int)

```

* Wyjaśnij rozmiar *True* i *False*.

---

Zad 7.

* Zapoznaj się z dokumentacją funkcji *id*.

* Wykonaj następujące polecenia:

```py
x = 2
y = x
print(x, y, id(x), id(y))
y = 3
print(x, y, id(x), id(y))
```

* Wykonaj następujące polecenia:

```py
x = [1,2]
y = x
print(x, y, id(x), id(y))
y[1] = 3
print(x, y, id(x), id(y))
```

* Wyjaśnij, dlaczego modyfikacja listy *y* zmienia wartość listy *x*, ale nie dzieje się tak w przypadku *int*.


---

zad 8.

* Niech `x = (a, b, c) = (1, 2, 3)`. Sprawdź wartości zmiennych *x*, *a*, *b* i *c*.

* Niech `x = a, b, c = 1, 2, 3`. Sprawdź wartości zmiennych *x*, *a*, *b* i *c*.

* Niech `a = 1` oraz `b = "jeden"`. Podmień wartości zmiennych *a* i *b*.
