def utworz_zadanie(wybor, nr_kol):
    print(wybor, nr_kol)
    # with open(f'kolos{nr_kol}.txt') as f:
    #     f.readlines()
    while True:
        inp = input('Wybor: ')
        match inp:
            case 'a':
                print('a')
                break
            case 'b':
                print('b')

def utworz_kilka_zadan(nr_kol):
    inp = input('Podaj nr tematow: ')
    print(inp)

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
