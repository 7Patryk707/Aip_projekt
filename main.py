import generator

print(f'{"-------MENU------"}\n{"1 - Petla\n2 - Dekoratory\n3 - Miasta\n4 - Kilka tematów\n'exit' - Wyjście"}\n-----------------')

i = 1 

nr_kol = input('Podaj nr kol: ')

while True:
    wybor = input("Wybierz  ")
    
    # tworzenie pliku

    match wybor.capitalize():
        case "1":
            generator.utworz_zadanie(wybor,nr_kol)
        case "2":
            generator.utworz_zadanie(wybor,nr_kol)

        case "3":
            generator.utworz_zadanie(wybor,nr_kol)

        case "4":
            generator.utworz_kilka_zadan(nr_kol)
            

        case 'Exit':
            print(f'Utworzono plik kolokwium{nr_kol}.txt')
            break
    
        case default:
            print('Brak takiej opcji!')
            i-=1

    print(f"Ilość zadań: {i}")
    i+=1

