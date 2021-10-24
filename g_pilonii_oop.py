'''
# mostenire -> Proprietate prin care o clasa poate sa reutilizeze material din alta clasa

#Encapsulare -> modalitate prin care putem sa atribuim un anumit nivel de acces unor variabile sau metode
# niveluri de acces:
# - public -> Sunt vizibile de oriunde din program
# - private (__)-> Se pot folosi doar in interiorul clasei curente
# - protected  (_)-> Se pot folosi doar in aceeasi clasa sau si in clasa copil

#Abstractizare -> modalitate prin care putem sa creem anumite template-uri pentru alte clase.
# Adica daca vrem sa definim o clasa test case cu metoda setup sau execute,
# atunci toate clasele care vor extinde modelul asta vor fi obligate sa aiba mapate metodele respective
# Un alt avantaj e faptul ca avem suficient de bine documentata folosirea altor clase


# Polimorfism -> Se refera la o abilitate prin care un obiect poate avea mai multe forme.
# Ex: avem o metoda calculateArea, prin care se poate calcula diferit aria pentru un triunghi, patrat etc.
# Am folosit polimorfismul deja in functia print (unde putem sa punem atat numere cat si stringuri, boolean sau alt tip de data)

'''

#POLIMORFISM

print('mesaj')
print(7)
print(7, 3, 5)
print(7, 3, 5, sep=':', end='*')
print(7, 3, 5, sep=':', end='*')
print('.................')
a = ['masina', 10, 'avion', True, 15]
b = 'complex'
print(len(a))
print(len(b))


# adunam 3 numere date de la tastatura
# def addition(num1, num2, num3=0, data_type = 'int'):
#     if data_type == 'str':
#         return str(num1) + str(num2) + str(num3)
#     else:
#         return (num1+num2+num3)

# def addition(a,b, c=0, dataType='str'):
#     if dataType=='str':
#         return str(a) + str(b) + str(c)
#     return a+b+c
#
# a = (input('Introduceti primul numar: '))
# b = (input('Introduceti cel de al 2lea nr: '))
# c = (input('introduceti cel de al 3lea nr: '))
#
# print(addition(2,3,6))
# print(addition('a', 'b'))


class Romania:
    def capital(self):
        print('Capitala Romaniei este Bucuresti ')

    def language(self):
        print('Limba nationala este romana ')


class Germania:
    def capital(self):
        print('Capitala Germaniei este Berlin ')

    def language(self):
        print('Limba nationala este germana ')

#Ctr ALT L = formatare cod
obj_rom = Romania()    #Aici am instantiat un obicet din clasa Romania
obj_ger = Germania()   #Aici am instantiat un obicet din clasa Germania

for capitala in (obj_rom, obj_ger):
    capitala.language()
    capitala.capital()



#MOSTENIRE
'''numele claselor vor incepe intotdeauna cu litera mare si va urma tipologia camelcase in timp ce variabilele si 
functiile se vor scrie intotdeauna cu litara mica si vor urma tipologia snake case.'''
''' Functiile definite in interiorul unei clase se numesc metode. '''

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

obj_car = Car()
obj_old_car = OldCar()
obj_new_car = NewCar()

obj_car.start() # se apeleaza metoda start din clasa Car =>Masina trebuie sa porneasca atunci cand motorul este pornit
obj_old_car.start() #=>Masina trebuie sa porneasca atunci cand cheia este rasucita spre dreapta
obj_new_car.start() # =>Masina trebuie sa porneasca atunci cand apesi butonul start

# Exercitiu
# definiti polimorfismul si mostenirea fara sa copiati!! :)

#ABSTRACTIZARE
from abc import ABC, abstractmethod  # ABC = abstract base class
# Decorator este o modalitate de a altera comportamentul unei functii

class TestModel(ABC):
    @abstractmethod
    def setup(self):
        pass # facem o functie pe care nu stim exact inca cum o sa o implementam
    @abstractmethod
    def execute(self):
        raise NotImplemented  #raise este keyword folosit cand vrem sa anuntam utilizatorul viitor/sistemul ca block code-ul pt aceasta ,etoda nu a fost implementat
    @abstractmethod
    def tear_down(self):
        raise NotImplemented

class TC1(TestModel):
    def setup(self):
        print('Am setat parametrii test case-ului')
    def execute(self):
        print('Acum executam test case-ul')
    def tear_down(self):
        print('Test case-ul s-a executat')

obj_tc = TC1()
''' Functiile unei clase se pot apela doar cu ajutorul obiectului'''
obj_tc.setup()
obj_tc.execute()
obj_tc.tear_down()
