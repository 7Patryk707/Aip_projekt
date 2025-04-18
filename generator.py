import nbformat as nbf
import random

def utworz_zadanie(wybor, nr_kol):
    with open(f'pytania.txt') as f:
        wiersze = f.readlines()
    
    zadania_temp = []
    zadania = []
    licznik = 1

    for i, pyt in enumerate(wiersze):
        if pyt.strip() == wybor:
            zadania_temp.append({"pytanie": f"### Zadanie {licznik}\n{wiersze[i+1].strip()}","kod": ""})
            licznik += 1

    il_zadan = int(input('Ile zadań: '))

    for i in range(il_zadan):
        zadania.append(random.choice(zadania_temp))

    cells = []

    for zadanie in zadania:
        cells.append(nbf.v4.new_markdown_cell(zadanie["pytanie"]))
        cells.append(nbf.v4.new_code_cell(zadanie["kod"]))
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = cells

    with open(f"kolokwium_{nr_kol}.ipynb", "w") as f:
        nbf.write(nb, f)

def utworz_kilka_zadan(nr_kol, tematy_kol):
    inp = input('Podaj numery tematow (oddzielone spacja): ').split()
    tematy = []

    for i in inp:
        tematy.append(tematy_kol[int(i)])

    with open(f'pytania.txt') as f:
        wiersze = f.readlines()
    
    zadania_temp = []
    zadania = []
    licznik = 1

    for i, pyt in enumerate(wiersze):
        if pyt.strip() in tematy:
            zadania_temp.append({"pytanie": f"### Zadanie {licznik}\n{wiersze[i+1].strip()}","kod": ""})
            licznik += 1

    il_zadan = int(input('Ile zadań: '))

    for i in range(il_zadan):
        zadania.append(random.choice(zadania_temp))

    cells = []

    for zadanie in zadania:
        cells.append(nbf.v4.new_markdown_cell(zadanie["pytanie"]))
        cells.append(nbf.v4.new_code_cell(zadanie["kod"]))
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = cells

    with open(f"kolokwium_{nr_kol}.ipynb", "w") as f:
        nbf.write(nb, f)


def tematy():
    inp = input("Wpisz tematy(oddziel ','): ")
    
    print(inp)
    print(inp[0])
    print(inp[2])
    
    if '1' in inp:
        print('znajduje się')
    if '2' in inp:
        print('znajduje się')
    if '3' in inp:
        print('nie znajduje się')

utworz_kilka_zadan(2, {1: 'Dekoratory', 2: 'Funkcje', 3: 'Pliki'})