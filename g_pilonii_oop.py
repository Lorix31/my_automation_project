'''
# MOSTENIREA-> Proprietate prin care o clasa poate sa reutilizeze material din alta clasa

#Encapsulare -> modalitate prin care putem sa atribuim un anumit nivel de acces unor variabile sau metode
(metoda de a restrictiona accesul la informatiile din anumite variabile sau metode)
# Niveluri de acces:
# - public -> Sunt vizibile de oriunde din program
# - private (__)-> Se pot folosi doar in interiorul clasei curente
# - protected  (_)-> Se pot folosi doar in aceeasi clasa sau si in clasa copil

#ABSTRACTIZAREA-> modalitate prin care putem sa creem anumite template-uri pentru alte clase.
# Adica daca vrem sa definim o clasa test case cu metoda setup sau execute,
# atunci toate clasele care vor extinde modelul asta vor fi obligate sa aiba mapate metodele respective
# Un alt avantaj e faptul ca avem suficient de bine documentata folosirea altor clase


# POLIMORFISM -> Se refera la o abilitate prin care un obiect poate avea mai multe forme.
# Ex: avem o metoda calculateArea, prin care se poate calcula diferit aria pentru un triunghi, patrat etc.
# Am folosit polimorfismul deja in functia print (unde putem sa punem atat numere cat si stringuri, boolean sau alt tip de data)

'''

# POLIMORFISM

print('Mesaj')  # => Mesaj
print(7)  # => 7
print(7, 3, 5)  # => 7 3 5
print(7, 3, 5, sep=':', end='*')  # =>7:3:5*
print(7, 3, 5, sep=':', end='*')  # =>7:3:5*7:3:5* (printeaza randul 28 impreuna cu 29 in aceiasi linie
print('.............')
a = ['masina', 10, 'avion', True, 15]
b = 'complex'
print(len(a))  # => sunt 5 elemente in lista
print(len(b))  # => 7 - sunt 7 litere in cuv complex


# Construirea  functiilor custom cu caracter polimorfic
# Exemplu: Adunam 3 numere date de la tastatura
def addition(num1, num2, num3):
    return (num1 + num2 + num3)


a = int(input('Introduceti nr 1: '))
b = int(input('Introduceti nr 2: '))
c = int(input('Introduceti nr 3: '))

print(addition(a, b, c))  # => 60


# Exemplu:
class Romania:  # clasele se definesc cu litera mare
    def capital(self):  # Scriem self pt ca nu definim cate argumete are.
        print('Capitala Romaniei este Bucuresti ')

    def language(self):
        print('Limba nationala este romana ')


class Germania:
    def capital(self):
        print('Capitala Germaniei este Berlin ')

    def language(self):
        print('Limba nationala este germana ')


# Ctr ALT L = formatare cod
obj_rom = Romania()  # Aici am instantiat un obiect din clasa Romania
obj_ger = Germania()  # Aici am instantiat un obiect din clasa Germania

for capitala in (obj_rom, obj_ger):  # capitala este un contor cu care parcurgem anumite elemente. NU AM INTELES.....CE E CU CONTORUL...
    capitala.language() # CE ESTE capitala.language...????
            # am luat contorul capitala pe care il folosim sa parcurgem obiectele obj_rom si obj_ger # si folosind contorul capitala am accesat metoda din fiecare clasa

''' =>
Limba nationala este romana
Capitala Romaniei este Bucuresti
Limba nationala este germana
Capitala Germaniei este Berlin
'''

#MOSTENIRE
'''numele claselor vor incepe intotdeauna cu litera mare si va urma tipologia camelcase(numeClasa) in timp ce variabilele si
functiile se vor scrie intotdeauna cu litara mica si vor urma tipologia snake case (nume_variabila ) .'''
''' o functie de sine statatoare se numeste functtie iar o functie definita in interiorul unei clase se numeste metoda. '''

class Car:
    def start(self):
        print('Masina trebuie sa porneasca atunci cand motorul este pornit')
    def stop(self):
        print('Masina trebuie sa se opreasca acum')

class OldCar(Car):  #Mostenirea sau legatura intre clasa parinte si clasa copil se face pe baza plasarii intre () a numelui clasei parinte
    def start(self):
        print('Masina trebuie sa porneasca atunci cand cheia este rasucita spre dreapta')

    def stop(self):
        print('Masina trebuie sa se opreasca atunci cand cheia este rasucita spre stanga')

class NewCar(Car):
    def start(self):
        print('Masina trebuie sa porneasca atunci cand apesi butonul start')
    def stop(self):
        print('Masina trebuie sa se opreasca atunci cand apesi butonul stop')

#metoda de a instantia obiectul
obj_car = Car()#dupa clasa trebuie sa punem () ALTFEL LE CITESTE CA SI VARAIBILE
obj_old_car = OldCar()
obj_new_car = NewCar()

obj_car.start() # se apeleaza metoda start din clasa Car =>Masina trebuie sa porneasca atunci cand motorul este pornit
obj_old_car.start() #=>Masina trebuie sa porneasca atunci cand cheia este rasucita spre dreapta
obj_new_car.start() # =>Masina trebuie sa porneasca atunci cand apesi butonul start
#daca comentam de ex def start def stop de la clasa nedw Car =>Masina trebuie sa porneasca atunci cand motorul este pornit(ne ia textul de la parinte)




# # Exercitiu
# # definiti polimorfismul si mostenirea fara sa copiati!! :)
'''
Polimorfismul este o proprietate sau un atribut al programarii orientate pe obiecte (OOP) prin care noi putem sa obtinem
divere rezultate de la o functie pe baza diverselor input-uri. este o propietate care se poate adopta in functie de nevoi.
Mostenirea este o proprietate a OOP prin care putem sa accesam functionalitatea definita intr-o clasa parinte
'''




#ABSTRACTIZARE
from abc import ABC, abstractmethod # ABC = abstract base class
# Decorator este o modalitate de a altera comportamentul unei functii

class TestModel(ABC): # ABC = abstract base class inseamna ca in momentul in care definim functia cu argumentul ABC noi mostenim
                    #clasa care se numeste ABC....este subliniat pt ca trebuie importat
    @abstractmethod # este un decorator. apare mai intai cu rosu, apasam pe beculet si import abtract method from ABC
    def setup(self):
        pass # facem o functie pe care nu stim exact inca cum o sa o implementam
    @abstractmethod
    def execute(self):
        raise NotImplemented  #raise este keyword folosit cand vrem sa anuntam utilizatorul viitor/sistemul ca block code-ul pt aceasta
                              # metoda nu a fost implementat
    @abstractmethod
    def tear_down(self): #self este o metoda care apartine clasei
        raise NotImplemented


#definim o functie care implementeaza clasa abstracta
class TC1(TestModel):
    def setup(self):
        print('Am setat parametrii test case-ului')
    def execute(self):
        print('Acum executam test case-ul')
    def tear_down(self):
        print('Test case-ul s-a executat')

# Instantiere obiect
obj_tc = TC1()
''' Functiile unei clase se pot apela doar cu ajutorul obiectului'''
#apelare metoda
obj_tc.setup()
obj_tc.execute()
obj_tc.tear_down()
# =>
# Am setat parametrii test case-ului
# Acum executam test case-ul
# Test case-ul s-a executat
# ne ia mesajul de la class TC1 daca definim aceleasi fucntii si in clasa copil si in clasa parinte prioritate vor avea
# cele din clasa copil, de aceea ne apar aceste mesaje.

'''La abstractizare suntem obligati sa definim toate metodele din clasa abstracta'''
'''class TestModel(ABC): este un fel de sablon.'''
'''ultimele 20 min sunt despre excercitiu care nu ne-a mers mai sus....
 explicatia:
 m-am prins care e problema cu exercitiul

cand gandesti la rece merge treaba :)))

problema era ca noi incercam sa executam in acelasi timp si pentru text si pentru numere

print(addition(a, b, c, 'int'))
print(addition(a, b, c))

Noi avem doua instructiuni: ambele iau ca parametri aceleasi valori

si absolut intotdeauna una va crapa si cealalta va merge

are sens si pentru voi?
'''




