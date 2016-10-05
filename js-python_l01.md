# Języki skryptowe - Python
# Lista 1

---

Zad 1.

Użyj trybu interaktywnego jako kalkulatora, aby wyliczyć następujące wyrażenia:

* suma liczb: 2, 3, 5, -8
* średnia liczb: 2, 3, 5, -8
* $cos(\pi)$

*wskazówka:*

```py
import math
dir(math)
help(math.cos)
```

* $sin(x)$, gdzie $x = 2 / 3 * \pi$

* $sin(x)$, gdzie $x = 2 / 3 * \pi - \pi$

---

Zad 2.

W trybie interaktywnym wykonaj następującą serię poleceń:

```py
2 * 2
_ * 3
_ * 4
_ * 5
```

Jakie jest znaczenie zmiennej `_`? Czy ułatwiłoby to wyliczenie punktu 2 z zadania 1?

---

Zad 3.

Zbadaj działanie funkcji wbudowanej `round`, np.

```py
help(round)
round(2.5)
round(2.51)
round(-2.5)
round(-2.51)
```

---

Zad 4.

* W Pythonie 2 sprawdź wynik następujących działań:

```py
import sys # informacje systemowe

x = sys.maxint # użyj help(sys), aby sprawdzić definicję maxint
type(x)

x += 1
type(x)
```

* Powtórz to samo w Pythonie 3. Korzystając z dowolnych źródeł (innych niż prowadzący lub koleżanki / koledzy z grupy) wyjaśnij otrzymany rezultat.

*Wskazówka: jeśli dysponujesz tylko interpreterem Pythona 3, możesz na potrzeby tego zadania użyć konsoli online, np. https://repl.it/languages/python*

---

Zad 5.

* Korzystając z wbudowanej dokumentacji znajdź funkcję, która wyznacza licznik i mianownik ułamka zwykłego dowolnej liczby zmiennoprzecinkowej.

*Wskazówka: `help(float)`*

* Przetestuj jej działanie na kilku dowolnych przykładach.

* Przetestuj jej działanie na `math.pi`. Czy jesteś w stanie to wyjaśnić ($\pi$ jest niewymierna)? Jeśli nie, to zapoznaj się z np. https://pl.wikipedia.org/wiki/Liczba_zmiennoprzecinkowa i sprawdź `sys.float_info`

* Wykonaj następujące obliczenia:

```py
x = sys.float_info.max
x
2 * x
```

---

Zad 6.

Zdefiniuj dwie zmienne typu tekstowego i jedną całkowitą, np.

```py
a = "jeden"
b = "dwa"
c = 3
```

Wykonaj następujące polecenia:

```py
a * b
a + b
a * c
a + c
a + str(c)
```

---

zad 7.

Korzystając z dokumentacji klasy *string* (`help(str)`) zapoznaj się z definicjami funkcji: `strip()`, `isnumeric()` oraz `rjust()`. Zademonstruj ich działanie na dowolnych przykładach.

---

Zad 8.

Napisz skrypt, który wykona następujące czynności:

* zmiennej `a` przypisze wartość `5`
* zmiennej `b` przypisze wartość `3`
* zmiennej `P` przypisze wartość `a*b`
* wypisze na ekranie "Pole prostokąta o bokach `a` i `b` wynosi `P`." (gdzie w miejsce zmiennych zostaną wstawione odpowiednie wartości).

Uruchom program w konsoli. Następnie edytuj skrypt zmieniając długości boków i uruchom go raz jeszcze.
