'''
For si while sunt cicluri repetitive (loops). Raspunde la nevoie de a face un lucru de mai multe ori.
if-else este o intersectie, niste conditii.
'''

# Exercitiu: printam 101 dalmatieni
# rezolvare cu WHILE
print('dalmatian 1')
print('dalmatian 2')
print('dalmatian 101') # ar fi prea mult de scris



i = 1
while i <= 101: # conditia este supapa de intrare, daca este adevarat se executa codul din while
    print('dalmatianul cu nr ' + str(i)) #=?dalmatianul 1 printeaza la infinit
    i = i + 1 # sau i+=1, incrementam in fiecare ciclu, il crestem cu 1 pe i =>#printeaza dalmatienii de la 1 la 101
else:
    print('nu mai sunt alti dalmatiei ')



#while-else exista dar se foloseste mai rar, else are rolul sa ne arate ceva daca conditia este falsa
while 1==2:
    print('nu intram pe ramura asta niciodata')
else:
    print('cand conditia este falsa , se executa else')

bool_var = True
while bool_var:
    print('nu intram pe ramura asta niciodata')
    bool_var = False
else:
    print('else se executa de fiecare data la final, cand conditia nu se mai indeplineste')


# Exercitiu - Supermario are 3 vieti. De fiecare data cand moare, scadem o viata, la final afisam game over

print('start game')
superMario = 3
while superMario >=1:
    print('Continua jocul si pierde o viata ')
    superMario = superMario - 1
else:
    print('Game Over')



#Rezolvare cu FOR pt exercitiu cu dalmatieni
for j in range(0, 102): #pt j de la 0 la 102 (fara ultimul index 102)
    print(f'Dalmatianul cu nr {j}') #printeaza dalmatienii de la 1 la 101



# Exercitiu: numaram de la 0 la 7
for index in range(8):
    print(index) # daca nu punem de unde sa inceapa, incepe de la 0 => printeaza 0,1,...7



#Rezolvare cu FOR pt exercitiu cu dalmatieni - numaram din 2 in 2  (pasul)
for n in range(0, 102, 2): #pt j de la 0 la 102 (fara ultimul index 102)
    print(f'Dalmatianul cu nr {n}') #=>0,2,4,6...100




# FOR EACH = pentru fiecare element dintr-o LISTA
telefoane = ['iphone 7', 'samsung galaxi 10', 'HTC']
print(telefoane) # =>['iphone 7', 'samsung galaxi 10', 'HTC']
for telefon in telefoane: #telefon este o variabila denumita de noi de obicei la singular
    print(telefon)
    # => iphone 7
    # samsung galaxi 10
    # HTC
    print('reducere mare la ' + telefon)
#=>
# iphone 7
# reducere mare la iphone 7
# samsung galaxi 10
# reducere mare la samsung galaxi 10
# HTC
# reducere mare la HTC


# FOR EACH = pentru fiecare element dintr-un string
nume = 'Andy'
for litera in nume:
    litera = litera.upper()
    print(litera)
    # A
    # N
    # D
    # Y

# FOR CU ELSE
for x in 'banana':
    print(x)
else:
    print('am terminat banana') # ca si la while, se executa o data la final.


''' BREAK & CONTINUE
- break =  forteaza iesirea din ciclu
- sare peste executia respectiva  dar continua restul iteratiei'''

#ex: printam 101 Dalmatiei si il cautam pe Pogo (D7) (cautam acul in carul cu fan :)  )
for dalmatian in range(1,102):
    print(f'Dalmatian:  {dalmatian}')
    if dalmatian == 7:
        print('L-am gasit pe Pogo, dalmatianul 7')
        break  # opreste executia de tot
# = >Dalmatian:  1
# Dalmatian:  2
# Dalmatian:  3
# Dalmatian:  4
# Dalmatian:  5
# Dalmatian:  6
# Dalmatian:  7
# L-am gasit pe Pogo, dalmatianul 7
# s-a oprit la 7

#TEMA SA IL GASIM PE POGO DAR CU WHILE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

# Ex cu continue- vreau sa NU afisez parintii (D7 si D17)
for dalmatian in range(1,102):
    if dalmatian == 7 or dalmatian == 17:
        continue # opreste DOAR acest print(f'Dalmatian:  {dalmatian}')asta iteratie. nu mai merge pe linia de dedesupt print ci ne trimite la inceputul for-ului
    print(f'Dalmatian:  {dalmatian}') #= printeaza de la d1 la d101 dar fara 7 si fara 17

#TEMA SA IL GASIM PE POGO DAR CU WHILE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



#exercitiu
''' Luam produse de la tastatura si le adaugam in stoc(o lista) pana scriem stop (un while/for).'''
stoc = [] #declaram o lista goala de produse
produs = ''
while produs != 'Stop': # != semn pt diferit / atata timp cat produsul este !=de stop vom continua sa luam produse de la tastatura
    produs = input('Introdu produsul in stoc: ') # luam produse de la tastatura si le pastram invariabila produs
    # if produs != 'Stop':  #daca produsul nu este stop
    #     stoc.append(produs) # adaugam produsul in lista stoc
print(stoc)


# scoatem cu remove valoarea stop din lista
# parsam/parcurgem lista fara ultimul element(folosindu-ne de un for cu range  sau folosind slicing)
# scoatem ultimul element dintr-o lista folosind o metoda index-ul
# scoatem ultimul element dintr-o lista folosind o metoda pop care scoatem ultimul element
# nu adaugam stop-ul in stoc din start (cu if)

''' Exercitiu: ghicitoare de numere / avem un nr secret / cerem un nr de la tastatura intre 1 si 30 / daca este ,mai mic
sau mai mare dam indiciu / daca e acelasi felicitari '''

secret = 17
ghicit = 0
print('Alege un nr intre 1 si 30')
while secret != ghicit: # jocul incepe cand jucatorul nu a ghicit nr secret
    ghicit = int(input ()) # luam nr de la tastatura si il castam/fortam sa fie int
    if ghicit < secret:
        print('alege un nr mai mare')
    elif ghicit > secret:
        print('alege un nr mai mic')
    else:
        print('FELICITARI')