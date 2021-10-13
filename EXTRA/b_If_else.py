'''
If else este o structura care evalueaza niste conditii de sus in jos iar in momentul in care o gaseste pe prima adevarata
executa codul corespunzator acesteia.
'''

# Ex. sa calculam impozitul la o masina.
cm_cubi = 2400
impozit = 0
if cm_cubi < 0:
    print('date invalide') #daca conditia este adevarata se excuta zona aceasta de cod care este indentata(alineata)
elif cm_cubi <=50:
    print('motocicleta')
    impozit = 50
elif cm_cubi <= 2000:
    print('masina mica')
    impozit = 160
else:  # in toate celelalte cazuri va executa codul acesta
    print('masina mare')
    impozit = 700
print(f'impozitul este {impozit}') #am declarat variabila cm_cubi = 2400 si atunci rezultatul va fi => masina mare, impozitul este 700



#alt ex
cm_cubi = 49
impozit = 0
if cm_cubi < 0:
    print('date invalide') #daca conditia este adevarata se excuta zona aceasta de cod care este indentata(alineata)
elif cm_cubi <=50:
    print('motocicleta')
    impozit = 50
elif cm_cubi <= 2000:
    print('masina mica')
    impozit = 160
else:  # in toate celelalte cazuri va executa codul acesta
    print('masina mare')
    impozit = 700
print(f'impozitul este {impozit}') #am declarat variabila cm_cubi = 49 si atunci rezultatul va fi => motocicleta, impozitul este 50

#exercitii -  daca afara ploua sa afiseze 'umbrela', daca nu e true, 'ochelari de soare
afara_ploua=True
if afara_ploua==True: #  == operator de comparare, intoarce true daca stanga = cu dreapta. merge si daca nu punem==True
    print('umbrela')
else:
    print('ochelari de soare') #=>umbrela

# # != verifica daca stanga este diferita de dreapta. este inversul lui ==
#
# #exercitiu
# afara_ploua=True
# if afara_ploua!=True: #  != operator de comparare, verifica daca stanga este diferita de dreapta. este inversul lui ==
#     print('ochelari de soare') #afara plua e true !=>true este diferit de true - nu
# else:
#     print('umbrela') #=> umbrela

# assert verifica daca conditia este True
# afara_ploua=True
# assert afara_ploua #=>Process finished with exit code 0 adica codul a fost validat
#
# afara_ploua=False
# assert afara_ploua #=> primim eroare AssertionError

# cm_cubi = 1
# assert cm_cubi => trece testul

# Verificati daca x este intre -5 si 13
x=15
if x>=-5 and x<=13:
    print('corect')
else:
    print('incorect') #=> -6=incorect, 10=corect, 15=incorect

# La sedinta cu parintii trebuie sa vina ori cu mama ori cu tata ori cu bunica si cu bunicul
mama = False #adica nu a venit la sedinta
tata = False
bunica = True
bunicu = False

if mama or tata or (bunica and bunicu):
    print('corect')
else:
    print('incorect') #=>incorect

#sau
mama = False #adica nu a venit la sedinta
tata = True
bunica = False
bunicu = False

if mama or tata or (bunica and bunicu):
    print('corect')
else:
    print('incorect') #=>corect

#sau
mama = False #adica nu a venit la sedinta
tata = True
bunica = True
bunicu = False

if mama or tata or (bunica and bunicu):
    print('corect')
else:
    print('incorect') #=>corect (bunica nu mai este luata in calcul) este indeplinita minim una din conditii

# Verificati daca y are minim 4 cifre. Indiciu: sa luam niste valori corecte si valori incorecte.
# corect y = 1000
# gresit y = 999
y = 10000
if y>=1000 or y<=1000: #trebuie sa gandim si varianta de -10000 care are 4 cifre
    print('y are min 4 cifre')
    raspuns = True
else:
    print('y nu are 4 cifre')
    raspuns = False
assert raspuns == True #=> daca definim y=pt-10 000 nu ne pica tetsul Process finished with exit code 0

#sau
y = 888
if y>=1000 or y<=1000: #trebuie sagandim si varianta de -10000care are 4 cifre
    print('y are min 4 cifre')
    raspuns = True
else:
    print('y nu are 4 cifre')
    raspuns = False
assert raspuns == False #=> daca definim y=888 => pica testul AssertionError


ex de if else cu string
if-ul merge doar pe prima ramura true.
inainte sa verificam ziua, vrem sa procesam datele ca sa mearga si pt litere mari si pt spatii


day = day.replace(' ''')
day = input('alege o zi din saptamana ')
if day == 'sambata' or day == 'duminica':
    print('weekend!')
    print('Happy!')
    if day == 'duminica':
        print('biserica')
elif day in ['luni', 'marti', 'miercuri', 'joi', 'vineri']: #daca ziua este in lista
    print('weekday')
    print('not so happy')
else:
    print('zi invalida')

# cu CTRL + CLICK pe numele functieie (adica istitle), ajungem la definitia functiei
titlu = 'Luceafarul'
print(titlu.istitle()) # este titlu? DA sau NU