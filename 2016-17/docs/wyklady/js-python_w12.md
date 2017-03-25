
# Języki skryptowe - Python
## Wykład 12

---

* graficzny interfejs użytkownika

## GUI

---

* *Graphical User Interface*
* Najpopularniejsze biblioteki:
    * **Tkinter**
    * PyQT
    * PyGTK
    * wxPython
* Pełna lista: [link](https://wiki.python.org/moin/GuiProgramming)

## PIerwsze okienko

---


```python
import tkinter as tk

# główne okno programu
# z tytułem, krawędziami itp
# kontener na resztę
root = tk.Tk()

# pętla programu - wyłapuje sygnały
# przerwana przez zamknięcie okna
# lub wywołanie quit()
root.mainloop()  
```

## Tytuł i wymiary

---


```python
root = tk.Tk()

# tytuł okna
root.title("Hello World!")

# szerokość x wysokość + położenie x + położenie y
root.geometry("400x300+200+200")

root.mainloop()
```

## Klasa *App*

---


```python
class App(tk.Tk):
    # App dziedziczy z tkinter.Tk
    def __init__(self, title="Aplikacja"):
        super().__init__() # konstruktor Tk
        self.title(title)  # ustaw tytuł
        
    def run(self):
        # app.run() będzie się lepiej prezentować
        self.mainloop()
```

## Pierwsza "aplikacja"

---


```python
app = App("Pierwsza aplikacja")

# app dziedziczy z Tk
# więc ma dostęp do tych samych funkcji

#app.geometry("400x300+200+200")

app.run()
```

## Centrowanie aplikacji

---


```python
class App(tk.Tk):
    def __init__(self, title="Aplikacja"):
        super().__init__() # konstruktor Tk
        #super().option_add("*font", "Helvetica 24")
        self.title(title)  # ustaw tytuł
        self.center()      # wyśrodkuj
        
    def run(self): self.mainloop()
        
    def center(self):
        self.update()
        # szerokość / wysokość okna
        wx = self.winfo_width()
        wy = self.winfo_height()
        # szerokość wysokość ekranu
        sx = self.winfo_screenwidth()
        sy = self.winfo_screenheight()
        # środek ekranu przesunięty o 
        x = (sx - wx) // 2 # połowę szerokośi
        y = (sy - wy) // 2 # połowę wysokości
    
        self.geometry("{}x{}+{}+{}".format(wx, wy, x, y))
```

## Test

---


```python
app = App("Wyśrodkowana aplikacja")

app.run()
```

## Pierwszy *Frame*

---


```python
# Frame to po prostu prostokątny obszar

root = tk.Tk()
root.geometry("400x300+200+200")

# Frame(parent)
ramka = tk.Frame(root) # umieść ramkę w root
# więcej o pack za chwilę
ramka.pack(fill=tk.BOTH, expand=True)

root.mainloop()
```

## Pierwszy kolorowy Frame

---


```python
root = tk.Tk()
root.geometry("400x300+200+200")

# Frame(parent, background=color)
ramka = tk.Frame(root, background="red")
ramka.pack(fill=tk.BOTH, expand=True)

root.mainloop()
```

## Aplikacja z ramką

---


```python
app = App("Jedna ramka")

# App dziedziczy z tk.Tk
# więc też może być argumentem Frame(...)
ramka = tk.Frame(app, background="red")
ramka.pack(fill=tk.BOTH, expand=True)

app.run()
```

## Klasa ramka

---


```python
# pozwoli zaoszczędzić miejsca na kolejnych slajdach

class Ramka(tk.Frame):
    # nasza ramka dziedziczy z tkinter.Frame
    def __init__(self, parent, color="white"):
        # wywołaj konstruktor Frame
        tk.Frame.__init__(self, parent, background=color)
        # o pack więcej za chwilę
        self.pack(fill=tk.BOTH, expand=True)
```

## Przykład

---


```python
app = App("Jedna ramka")

# Ramka inicjuje Frame
# i się pakuje w App
ramka = Ramka(app)

app.run()
```

## Dwie ramki

---


```python
app = App("Jedna ramka")


r1 = Ramka(app) # "white"
r2 = Ramka(app, "red")

app.run()
```

## Pakowanie

---

* do rozmieszczania widgetów służy funkcja *widget.pack(opcje)*
* dostępne opcje:
    * **expand** - *True* / *False*; domyślnie jak rodzic
    * **fill** - *None* (domyślnie) / *BOTH* / *X* / *Y*
    * **side** - z której strony rodzica zacząć układać: *TOP* (domyślnie) / *BOTTOM* / *LEFT* / *RIGHT*

## Pakowanie ramek

---


```python
class Ramka(tk.Frame):
    # dodajemy argument kluczowy side
    def __init__(self, parent, color="white", side=tk.TOP):
        tk.Frame.__init__(self, parent, background=color)   
        self.pack(fill=tk.BOTH, expand=True, side=side)
```

## Pakowanie ramek I

---


```python
app = App("Dwie ramki")

r1 = Ramka(app, "white", tk.LEFT)
r2 = Ramka(app, "red", tk.RIGHT)

app.run()
```

## Pakowanie ramek II

---


```python
app = App("Trzy ramki")

r1 = Ramka(app, "white", tk.LEFT)
r2 = Ramka(app, "red", tk.RIGHT)
r3 = Ramka(app, "green", tk.TOP)

app.run()
```

## Pakowanie ramek III

---


```python
app = App("Trzy ramki")

r1 = Ramka(app, "green", tk.TOP) # górna ramka
r2 = Ramka(app) # dolna ramka

# do dolnej ramki wrzucamy lewą i prawą
r21 = Ramka(r2, "white", tk.LEFT)
r22 = Ramka(r2, "red", tk.RIGHT)

app.run()
```

## Pierwszy przycisk

---


```python
app = App("Aplikacja z przyciskiem")

ramka = Ramka(app)

# Button(parent, text, command)
# app.center bez ()
przycisk = tk.Button(ramka, text="Center", command=app.center)
przycisk.place(x=0, y=0) # pozycja przycisku

app.run()
```

## Więcej o *command*

---


```python
def funkcja():
    return "Hello"

# przypisuje odpowiednią funkcję
# która będzie wywołana po naciśnięciu
przycisk1 = tk.Button(command=funkcja)

przycisk1.cget("command")
```


```python
# przypisuje wynik zwracany przez funkcję
przycisk2 = tk.Button(command=funkcja())

przycisk2.cget("command")
```

## *command* i argumenty funkcji?

---

* a co jeśli chcemy, aby przycisk wywoływał funkcję z jakimś argumentem?
* np. mamy dwa przyciski i chcemy, aby jeden zmieniał tło na kolor biały a drugi na czerwony
* chcemy użyć tej samej funkcji, ale z innym argumentem
* wtedy niezbędne jest wykorzystanie wyrażeń lambda

## Wyrażenia *lambda*

---


```python
def suma(a, b): # "klasyczna" funkcja
    return a + b
```


```python
lsuma = lambda a, b: a + b # "anonimowa" funkcja
```


```python
suma(1, 2) # wywołujemy funkcję suma
```


```python
lsuma(1, 2) # wywołujemy wyrażenia lambda
```

## Wyrażenie *lambda*

---


```python
def suma(a, b):
    return a + b

suma2 = lambda b: suma(2, b) # dodaj 2
suma4 = lambda b: suma(4, b) # dodaj 4
```


```python
suma2(1)
```


```python
suma4(1)
```

## Wyrażenie *lambda*

---


```python
def change_color(color="white"):
    print("Zmieniam kolor na:", color)
    
ustaw_zielony = lambda: change_color("zielony")
ustaw_niebieski = lambda: change_color("niebieski")
```


```python
ustaw_zielony() # change_color("zielony")
```


```python
ustaw_niebieski() # change_color("niebieski")
```

## Kolor ramki

---


```python
class Ramka(tk.Frame):

    def __init__(self, parent, color="white", side=tk.TOP):
        tk.Frame.__init__(self, parent, background=color)   
        self.pack(fill=tk.BOTH, expand=True, side=side)
        
    def change_color(self, color="white"):
        # Frame.config umożliwia zmianę parametrów
        self.config(bg=color) # bg = background
```


```python
app = App("Jedna ramka")

ramka = Ramka(app) # domyślnie biała
ramka.change_color("red") # zmień kolor

app.run()
```

## Przycisk do koloru

---


```python
app = App("Przycisk do tła")

ramka = Ramka(app)

# Button(parent, text, command)
przycisk = tk.Button(ramka, text="Red",
                     command=lambda: ramka.change_color("red"))
przycisk.place(x=0, y=0) # pozycja przycisku

app.run()
```

## Kilka przycisków

---


```python
app = App("Przyciski v1")

ramka = Ramka(app)

but_red = tk.Button(ramka, text="Red",
                    command=lambda: ramka.change_color("red"))
but_red.place(x=0, y=0) # wpisujemy ręcznie

but_blue = tk.Button(ramka, text="Blue",
                     command=lambda: ramka.change_color("blue"))
but_blue.place(x=0, y=50) # absolutne pozycje

but_def = tk.Button(ramka, text="Default",
                    command=lambda: ramka.change_color())
but_def.place(x=0, y=100) # przycisków

app.run()
```

## Kilka przycisków krócej

---


```python
app = App("Przyciski v2")

ramka = Ramka(app)

# wykorzystamy wyrażenia lambda do generowania przycisków
button = lambda color: tk.Button(ramka, text=color,
                                 command=lambda: ramka.change_color(color))

button("red").place(x=0, y=0)     # wpisujemy ręcznie
button("blue").place(x=0, y=50)   # absolutne pozycje
button("white").place(x=0, y=100) # przyciskow

app.run()
```

## Układanie przycisków

---


```python
app = App("Przyciski v3")

ramka = Ramka(app)

button("red").pack(side=tk.LEFT)   # pakujemy od lewej
button("blue").pack(side=tk.LEFT)
button("white").pack(side=tk.LEFT)

app.run()
```

## Rozciąganie przycisków

---


```python
app = App("Przyciski v4")

ramka = Ramka(app)

# czerwony rozciągamy w poziomie
button("red").pack(side=tk.LEFT, fill=tk.X, expand=True)
# niebieski ma stały rozmiar
button("blue").pack(side=tk.LEFT)
# biały rozciądamy w pionie
button("white").pack(side=tk.LEFT, fill=tk.Y, expand=True)

app.run()
```

## Siatka

---


```python
app = App("Przyciski v5")

ramka = Ramka(app)


# 1 rząd 1 kolumna
button("red").grid(row=0, column=0)
# 1 rząd 2 kolumna
button("blue").grid(row=0, column=1)
# 2 rząd 1 kolumna
button("white").grid(row=1, column=0)
# 2 rząd 2 kolumna
button("black").grid(row=1, column=1)

app.run()
```

## Rozciąganie w siatce

---


```python
from tkinter import N, S, E, W

app = App("Przyciski v6")

ramka = Ramka(app)

# 1 rząd 1 kolumna
button("red").grid(row=0, column=0, sticky=N+S+E+W)
# 1 rząd 2 kolumna
button("blue").grid(row=0, column=1, sticky=N+S+E+W)
# 2 rząd 1 kolumna
button("white").grid(row=1, column=0, sticky=N+S+E+W)
# 2 rząd 2 kolumna
button("black").grid(row=1, column=1, sticky=N+S+E+W)

app.run()
```

## Pole tekstowe

---


```python
app = App("Pole tekstowe")

tekst = tk.Entry(app) # pole tekstowe
tekst.pack() # domyślne pakowanie

app.run()
```

## Pole tekstowe - wstaw

---


```python
app = App("Pole tekstowe - insert")

tekst = tk.Entry(app)
tekst.pack(fill=tk.X, expand=True) # rozciągnij w poziomie

# wstaw początkowy tekst
tekst.insert(0, "Tutaj wpisz cokolwiek...")

app.run()
```

## Usuwanie tekstu

---


```python
app = App("Pole tekstowe - delete")

tekst = tk.Entry(app)
tekst.pack(fill=tk.X, expand=True)

tekst.insert(0, "Tutaj wpisz cokolwiek...")

# Entry.delete usuwa tekst
przycisk = tk.Button(app, text="clear",
                     command=lambda: tekst.delete(0, tk.END))
przycisk.pack()

app.run()
```

## Pobieranie tekstu

---


```python
app = App("Pole tekstowe - get")

tekst = tk.Entry(app)
tekst.pack(fill=tk.X, expand=True)

tekst.insert(0, "Tutaj wpisz cokolwiek...")

# Entry.get pobiera tekst
przycisk = tk.Button(app, text="pobierz", command=lambda: print(tekst.get()))
przycisk.pack()

app.run()
```

## Student GUI

---


```python
class Student:

    def __init__(self, imie, nazwisko, indeks):
        self._imie = imie
        self._nazwisko = nazwisko
        self._indeks = indeks

        self.save() # automatyczny zapis przy tworzeniu studenta

    def save(self):
        with open(".".join([self._imie, self._nazwisko]), 'w') as f:
            f.write(self._indeks)
```

## Główne okno programu

---


```python
import tkinter as tk

root = tk.Tk()
#root.option_add("*font", "Helvetica 24")
root.title("Student")
root.geometry("800x600+400+300")

# ramka z tłem, do której będziemy wrzucać pola tekstowe
ramka = tk.Frame(root, bg="white")
ramka.pack(fill=tk.BOTH, expand=True)
```

## Entries

---


```python
# imię
tk.Label(ramka, text="Imię: ").grid(row=0, column=0, sticky="nsew")
imie = tk.Entry(ramka)
imie.grid(row=0, column=1, sticky="nsew")

# nazwisko
tk.Label(ramka, text="Nazwisko: ").grid(row=1, column=0, sticky="nsew")
nazwisko = tk.Entry(ramka)
nazwisko.grid(row=1, column=1, sticky="nsew")

# numer indeksu
tk.Label(ramka, text="Indeks: ").grid(row=2, column=0, sticky="nsew")
indeks = tk.Entry(ramka)
indeks.grid(row=2, column=1, sticky="nsew")
```

## Przycisk *save*

---


```python
# wyrażenie lamba generujące studenta
# na bazie wpisów w entries
make_student = lambda: Student(imie.get(), nazwisko.get(), indeks.get())

przycisk = tk.Button(root, text="save", command=make_student)
przycisk.pack()
```

## Test

---


```python
root.mainloop()
```


```python
%%bash
cat Jan.Kowalski
```
