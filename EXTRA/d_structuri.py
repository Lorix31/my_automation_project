'''DICTIONAR/ dictionar / dict
# se trec intre {}
# o structura de date in care tinem perechi de valori - cheie:valoare
# (cheia este cuvantul pe care il cautam in dicitonar/valoarea este explicatia. ex:masina = metoda de transport
# este ca o lista dar in loc de index, folosim niste porecle
# valoarea poate sa fie int, string, boolean, lista '''

mediaMate = {
    'Andy': 7,
    'Alina': 10,
    'Larisa': 8,
    'Bianca': 8,
    'Roxana': 8
}
print('mediaMate este', mediaMate) #=>mediaMate este {'Andy': 7, 'Alina': 10, 'Larisa': 8, 'Bianca': 8, 'Roxana': 8}

noteMate = {
    'Andy': [7, 6, 8, 9], # putem avea ce tip de date vrem noi atat la cheie cat si la valoare, in f de nevoi(int, str, boolean, liste)
    'Alina': [10, 10, 10, 9],
    'Larisa': [9, 7, 9],
    'Bianca': 8,
    'Roxana': 8
}
print('noteMate sunt', noteMate)
#=>noteMate sunt {'Andy': [7, 6, 8, 9], 'Alina': [10, 10, 10, 9], 'Larisa': [9, 7, 9], 'Bianca': 8, 'Roxana': 8}

premiantiiClasei = {1: 'Alina', 2: ['Larisa', 'Bianca', 'Roxana'], 3: 'Andy'}
print('premiantii clasei sunt', premiantiiClasei) #=>premiantii clasei sunt {1: 'Alina', 2: ['Larisa', 'Bianca', 'Roxana'], 3: 'Andy'}

# problema: cum vedem doar premul 1? (2 metode)
print('premiul 1 este', premiantiiClasei[1]) #=>premiul 1 este Alina, 1 este cheia din premiantiiClasei
print('premiul 2 este - metoda2', premiantiiClasei.get(2)) # get(2) este o metoda, de aceea se pune intre ()
# =>premiul 2 este - metoda2 ['Larisa', 'Bianca', 'Roxana']

# problema: cum modificam valorile unor chei? marire de nota pt Larisa, din 8 in 9
mediaMate['Larisa'] = 9
print('printam doar media Larisei', mediaMate['Larisa']) # suprascrie nota Larisei =>printam doar media Larise 9


# problema: sa adaugam o noua pereche cheie:valoare. vine un elev nou in clasa
mediaMate['Lore'] = 9
print('printam iar media la mate dupa ce adaugam o noua persoana (cheie)', mediaMate)

# intr-un dictionar nu este importanta ordinea

# problema: pleaca un elev din clasa, deci va trebuie sa eliminam cheia corespunzatoare, 2 variante
mediaMate.pop('Andy')
print('media fara Andy', mediaMate) #=> media fara Andy {'Alina': 10, 'Larisa': 9, 'Bianca': 8, 'Roxana': 8, 'Lore': 9}
del mediaMate['Lore']
print('media fara Andy si Lore', mediaMate) #=>media fara Andy si Lore {'Alina': 10, 'Larisa': 9, 'Bianca': 8, 'Roxana': 8}




''' SET este o structura de date in care elementele au voie sa apara O SINGURA DATA, se trec tot intre {}
# intr-un set nu conteaza ordinea, toate au aceeasi importanta => elementele se vor afisa aleatoriu'''

fructe = {"apple", "banana", "cherry", "apple"}
print('printam fructe', fructe) # observam ca apple apare o singura data, desi este definit x2 din greseala

# adaugam elemete
fructe.add('apple') # daca exista deja, nu se maia dauga
fructe.add('watermelon')
print('fructe dupa ce adaugam pepene', fructe) #=>fructe dupa ce adaugam pepene {'apple', 'watermelon', 'banana', 'cherry'}

fructe2 = {"apple", "orange"}
print('uniunea dintre seturi', fructe.union(fructe2)) #=>uniunea dintre seturi {'orange', 'watermelon', 'banana', 'apple', 'cherry'}
print('intersectia dintre seturi', fructe.intersection(fructe2)) #=>intersectia dintre seturi {'apple'}
print('diferenta dintre seturi', fructe2.difference(fructe)) #diferenta din perspectiva fructe2 #=> diferenta dintre seturi {'orange'}
print('diferenta dintre seturi', fructe.difference(fructe2)) #=>diferenta dintre seturi {'watermelon', 'cherry', 'banana'}
#ne arata ce element avem diferit in fructe 2 fata de fructe...iar apoi ce elemnte avem diferinte in fructe fata de fructe2

#CTR+click ne duce unde este definita variabila


''' TUPLE = structura de date ordonata in care elementele nu pot fi schimbate/adaugate/sterse ulterior, este ca o lista dar IMUTABILA
- poate avea de mai multe ori acelasi element
- este ordonata, deci are index 
- se trece intre () 
- poate sa contina int, str '''

reteta_bunicii = (
    '1 L de apa plata',
    'zeama de lamaie dintr-o lamaie stoarsa',
    'o lingurita de miere',
    'o frunza de menta',
    'o frunza de menta'
)
print('reteta bunicii limonada', reteta_bunicii)
#=>reteta buncii limonada ('1 L de apa plata', 'zeama de lamaie dintr-o lamaie stoarsa', 'o lingurita de miere',
# 'o frunza de menta', 'o frunza de menta')

print('ce pun prima data?', reteta_bunicii[0]) # un element se poate accesa prin idex, ca intr-o lista
# verificam ca este o o structura ordonata si avem index=> ce pun prima data? 1 L de apa plata


# # nu putem modifica reteta
#reteta_bunicii[0] = '2 L de apa plata'
print('verificam daca am reusit sau nu sa schimbam elementul 0', reteta_bunicii)
#=> NE DA EROARE - TypeError: 'tuple' object does not support item assignment


# putem cauta un index
print('ce index are menta?', reteta_bunicii.index('o frunza de menta')) #>ce index are menta? 3

# sa numaram de cate ori apare un element
print('cate frunze de menta punem?', reteta_bunicii.count('o frunza de menta')) #=>cate frunze de menta punem? 2



if 'o lingurita de miere' in reteta_bunicii:
    print('Limonada este dulce')
else:
    print('Limonada este acrisoara')
#=>Limonada este dulce


#Recapitulare
#1. declara si afiseaza 3 tari cu capitalele lor => ca este un dictionar
capitale_europene = {
    'Cehia' : 'Praga',
    'Romania': 'Bucuresti',
    'Italia': 'Roma'
}
print(capitale_europene) #=> {'Cehia': 'Praga', 'Romania': 'Bucuresti', 'Italia': 'Roma'}

# sa afisam capitala Rome
print('capitala Italiei este', capitale_europene['Italia']) # in [] este Italia care este CHEIE. in ex de mai sus aveam
# cifra pt ca asa era declarata cheia
print('capitala Italiei este', capitale_europene.get('Italia')) # capitala Italiei este Roma

#adaugam un element nou
capitale_europene['Franta'] = 'Paris'
print(capitale_europene) #=>{'Cehia': 'Praga', 'Romania': 'Bucuresti', 'Italia': 'Roma', 'Franta': 'Paris'}

#stergem un element din dicitonar:
capitale_europene.pop('Romania')
print('printam fara Romania', capitale_europene)

#2. configuratorul culorilor de pe un site. nu vrem sa avem 2 ori aceiasi culoare deci facem un set
culori_masini = {'rosu', 'alb', 'albastru', 'rosu'}
print(culori_masini) #=>{'rosu', 'alb', 'albastru'}
# adaugam galben in culori
culori_masini.add('galben')
print(culori_masini) #=>{'albastru', 'galben', 'rosu', 'alb'}
culori_masini.remove('rosu')
print(culori_masini) #=>{'albastru', 'alb', 'galben'}

culori2 = {'galben', 'alb'}
print(culori_masini.issubset(culori2)) #=> false
print(culori2.issubset(culori_masini)) #=> True
# un subset cuprinde TOATE elementele dintr-un set

#afiseaza coordonatele unei locatii
coordonate = (123, 876)
#3. aratam 3 puncte de pe harta cu latitudine si longitudine. =>Tuples
harta = (
    (123, 346),
    (765,785),
    (coordonate),
    {'Cluj':(145,320)}
)
print(harta) #=>((123, 346), (765, 785), (123, 876), {'Cluj': (145, 320)})
#intr-o tupla se poate adauga orice, o lista, un dictionar, o alta tupla

print(harta[3]) #=>{'Cluj': (145, 320)} afiseaza elementul cu index 3
print(harta[3]['Cluj']) #=>(145, 320) afiseaza elementul cu index 3 care este un dictionar dar de aici ne citeste doar valoarea din cheia Cluj
print(harta[3]['Cluj'][1]) #=>(320)afiseaza elementul cu index 3 care este un dictionar dar de aici ne citeste doar valoarea cu index 1 din cheia Cluj
#3 ne da dictionarul
#in cadrul dictionarului putem naviga pe chei, Cluj
#cheia Cluj de ne da ca si valoarea un tuplu, (145,320)
#in tuplu putem sa navigam cu index, 1 ne va da 320
print(harta[2][0]) #=> pe index 2 ne afiseaza din tuplu coordonate adica (123, 876) iar pe index 0 123. rezultatul va fi 123
