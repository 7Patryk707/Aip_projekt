import generator

nr_kol = input('Podaj numer kolokwium: ')

tematy_kol = {}

with open('pytania.txt') as f:
    wiersze = f.readlines()
    licznik_pom = 1
    for i, temat in enumerate(wiersze):
        if i % 2 == 0:
            if temat.strip() not in tematy_kol.values():
                tematy_kol[licznik_pom] = temat.strip()
                licznik_pom += 1

j = 1 
while True:
    print("-------MENU------")
    for i, temat in tematy_kol.items():
        print(f'{i} - {temat}')
    print('q - Kolokwium z kilku tematów\nexit - Wyjście\n-----------------')
    wybor = input("Wprowadź: ")

    match wybor.capitalize():
        case wybor if wybor.isdigit() and 1 <= int(wybor) <= len(tematy_kol):
            generator.utworz_zadanie(tematy_kol[int(wybor)], nr_kol)
            print(f'Utworzono plik kolokwium_{nr_kol}.ipynb')
            break

        case "Q":
            generator.utworz_kilka_zadan(nr_kol, tematy_kol)
            print(f'Utworzono plik kolokwium_{nr_kol}.ipynb')
            break

        case 'Exit':
            break
    
        case default:
            print('Brak takiej opcji!')