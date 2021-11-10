''' Functii = o bucata de cod care poate fi refolosita ori de cate ori avem nevoie
(- reguli create de noi
- cod ce il putem utiliza ulterior  prin apelarea lor dupa nume
- este un programel definit intr-un loc si folosit in alta parte)

Sunt mai multe tipuri de functii.
Parametru = o variabila ce intra in functie cu valori diferite la fiecare apelare.
Return = rezultatul functiei

Atat parametrii cat si return-ul sunt optionale.
Parametrii pot fi oricati in functie de nevoi dar rezultatul(return) va fi unul singur

Ex: paralela cu masina de tocat carne. deasupra putem introduce carne de porc, vita, oaie(parametrii), rezultatul(return)
va fi un amestec de carne

Apelare functiei - se executa logica din interior(ca si cand invartim maneta masinii de tocat)
La final, carnea tocata este rezultatul UNIC,expus prin return
putem sa punem carnea tocata intr-un bol(variabila)
'''

def sum(a,b): # definim  numele functiei si parametrii de care are nevoie /
                # a, b sunt variabile fara valoare declarate dar neinitializate.
                # a,b se numesc argumente si la apelare cand ii dam valori sunt parametri
    s = a + b   # rezolvam logica problemei folosind variabilele fara valori
    return s    # rezultatul

# apelare functie
bol = sum(3,4)
print(bol) #=> 7
bol2 = sum(32554841,54787)
print(bol2) #=>print(sum(1,1)) #=> 2
# nu este oblogatoriu sa o prindem intr-o variabila. putem sa scriem si
print(sum(2,2)) #=> 4


#varianta scurta a ex de deasupra
def sum2(a,b):
    return a+b
# Apelare functie
print(sum2(2,2)) # => 4

# EXEMPLE:
# 1. Functie simpla fara parametrii si fara return
def happyBday():
    print('La multi ani!!! ') #print nu este un return, nu avem ce salva in variabila => nu apare nimic nimic

#Apelare functie
happyBday() #=>La multi ani!!! ne afiseaza pt ca noi avem in functie sa printeze acrst mesaj

# 2. Functie cu parametri, fara return
def happyBdayX(nume, varsta):
    print(f'La multi ani, {nume}!')
    print(f'Felicitari pentru veritabila vasrta de {varsta} de ani!')

#Apelare functie
happyBdayX('Marian', 78)
# => La multi ani, Marian!
# Felicitari pentru veritabila vasrta de 78 de ani!
happyBdayX('Maria', 85)
happyBdayX('Ana', 20)

#3. Funcctie fara parametri, dar cu return
def show_pi():
    return 3.14

def zile_saptamana():
    return ['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'] #putem returna orice tip de date
                                                                                 # cunoscut (in cazul nostru lista)

#Apelare functie.
# pt ca in general se def toate functiile, si uneori pot fi multe, si la urma se apeleaza functiile, cu CTR+CLICK
# pe apelarea functie ne duce la definirea functiei
show_pi() # nu ne afiseaza nimic ca nu avem print
print(show_pi()) #=>3.14
print(zile_saptamana()) #=>['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica']

#4. Functie cu parametri si cu return (cea mai folosita)
def ariaDreptunghiului(lungime, latime):
    aria = lungime * latime
    return aria

#apelare functie
print(ariaDreptunghiului(10,5)) #=>50
print(ariaDreptunghiului(20,10)) #=>200
print(len('abc')) #=> abc este parametrul functiei len si len este parametrul functiei print.


#EXERCITII:
# 1. Afiseaza numarul de litere din numele tau complet (nume, nume mjlociu, prenume)
def nr_litere_nume(nume, nume_mijlociu, prenume):
    numar = len(nume) + len(nume_mijlociu) + len(prenume) #numele variabilelor nu se scriu niciodata intre '' ci doar  valorie
    return numar

#apelare functie
print(nr_litere_nume('Roman', '/', 'Loredana')) #=>14
print(nr_litere_nume('Sinpetrean', 'Daniel', 'Andrei')) #=>22


#2. Afisati media a 3 numere
def media_numerelor(a,b,c):
    media = (a + b + c) / 3
    return media

print(media_numerelor(10,20,60)) #=>30
print(media_numerelor(2,4,6)) #=>4
print(media_numerelor(1231,2562,6895)) #=> 3562.6666666666665

#3. Afisati daca un triunghi este isoscel, echilateral sau oarecare
def tip_triunghi(latura1, latura2, latura3):
    if latura1 == latura2 == latura3:
        return 'Triunghiul este echilateral'
    elif latura1 == latura2 or latura1 == latura3 or latura2 == latura3:
        return 'Triunghiul este isoscel'
    else:
        return 'Triunghiul este oarecare'

print(tip_triunghi(15,15,15)) # => Triunghiul este echilateral
print(tip_triunghi(10,10,20)) # => Triunghiul este isoscel
print(tip_triunghi(10,30,10)) # => Triunghiul este isoscel
print(tip_triunghi(10,40,40)) # => Triunghiul este isoscel
print(tip_triunghi(8,12,31)) # => Triunghiul este oarecare


