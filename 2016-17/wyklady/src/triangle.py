"""Moduł do obsługi trójkątów."""

import sys
import math


def help():
    """Drukuje instrukcję obsługi i zamyka program"""

    print("usage: python triangle.py bok1 bok2 bok3")
    sys.exit(1)


def generate(a, b, c):
    """Zwraca posortowane boki trójkąta jako floaty."""

    return sorted([float(a), float(b), float(c)])


def check(a, b, c):
    """Zamyka program, jeśli nierówność trójkąta nie jest spełniona."""

    if a + b <= c:
        print("Nierówność trojkąta nie jest spełniona.\n")
        help()


def obwod(a, b, c):
    """Zwraca obwód trójkąta"""

    return a + b + c


def pole(a, b, c):
    """Zwraca pole trójkąta"""

    p = obwod(a, b, c) / 2
    # wzór Herona
    return math.sqrt(p*(p - a)*(p - b)*(p - c))


def typ_boki(a, b, c):
    """Zwraca typ trójkąta (ze względu na boki)"""

    if a == b == c:
        return "równoboczny"
    elif a == b or b == c:
        return "równoramienny"
    else:
        return "różnoboczny"


def typ_katy(a, b, c):
    """Zwraca typ trójkąta (ze względu na kąty)"""

    x = a**2 + b**2 - c**2

    if x == 0:
        return "prostokątny"
    elif x > 0:
        return "ostrokątny"
    else:
        return "rozwartokątny"

if __name__ == "__main__":

    try:
        a, b, c = generate(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        help()

    check(a, b, c)

    print("Obwód trójkąta =", obwod(a, b, c))
    print("Pole trójkąta =", pole(a, b, c))
    print("Trójkąt jest", 	typ_boki(a, b, c))
    print("Trójkąt jest", typ_katy(a, b, c))
