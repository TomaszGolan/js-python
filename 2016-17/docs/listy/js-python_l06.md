# Języki skryptowe - Python
# Lista 6

---

Lista do samodzielnego wykonania w trakcie zajęć.

Pod koniec zajęć każdy wysyła swoje rozwiązania na maila.

Każde zadanie w osobnym pliku: nazwisko_imie_zad_[numer].py.

Proszę zlitować się nad prowadzącymi i zadbać o to, żeby kod był czytelny
i odpowiednio komentowany. Dłuższe programy proszę rozbijać na mniejsze funkcje.
Każda funkcja powinna być opisana *docstringiem*.

---

Zad 1.

Napisz skrypt, który wygeneruje listę zawierającą 100 pierwszych wyrazów
ciągu geometrycznego (dla zadanych *a1* i *q* - pierwszy wyraz ciągu i iloraz).

Następnie wydrukuje na ekranie ten ciąg oraz jego podciąg zawierający tylko
parzyste wyrazy.

---

Zad 2.

Napisz funkcję, która sprawdza, czy podana liczba jest liczbą pierwszą. Funkcja
powinna zwracać *True* lub *False*.

Napisz skrypt, który sprawdzi, czy podana przez użytkownika liczba jest liczbą pierwszą.

*Uwaga: program powinien pytać do skutku, aż użytkownik poda liczbę naturalną. Wsk.* `str.isdigit()`

---

Zad 3.

Napisz skrypt, który wymaga trzech argumentów z linii komend (wsk. `sys.argv`), czyli

```
python moj_skrypt.py arg1 arg2 arg3
```

które są długościami boków trójkąta (można założyć, że podane argumenty są liczbami). Na tej podstawie skrypt powinien wydrukować na ekranie następujące informacje:

* obwód trójkąta
* pole trójkąta
* informację czy trójkąt jest równoboczny, równoramienny czy różnoboczny
* informację czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny

W przypadku złej liczby argumentów program powinien wyświetlić odpowiedni komunikat i zakończyć działanie.

---

Zad 4. (dla ambitnych)

Korzystając z metody równego podziału (bisekcji) znajdź przybliżone miejsce zerowe
funkcji: `f(x) = x**3 + 2*x*2 - 4*x - 10` w przedziale [1:3].
