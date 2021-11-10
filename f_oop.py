'''
- Functions to find the maximum out of 3 input numbers - vezi fisierul e_functii functia max3
- Functions to find the maximum out of 3 input numbers with nested functions
- Definirea  a 4 functii care efectueaza operatii de baza
- O functie definita in interiorul unei clase se numeste metoda
- OOP = Object Oriented Programming / POO = Programare Orientata pe Obiecte - tip de programare care se face exclusiv pe obiecte(ex obiect calculator mai jos)
'''

'''
O CLASA este un fel de schelet. Cand ii spunem sistemului keywordul class, sistemul stie ca trebuie sa definim ceea ce 
se numeste scheletul aplicatie. Acest schelet este ca un fel de template. 
Ex daca vrem sa creem o clasa masina, aceasta va avea mai multi parametri (nr roti, sasiu, nr usi, motor etc) adica creem un 
tipar  pe baza careia o sa creem toate masinile.  Ca sa putem defini fiecare parametru, masina in parte, o sa creem un 
tipar pornind de la care o sa creem celelate obiecte sau obiect de tip masina.
- prin conventie numele fiecarei clase trebuie sa inceapa cu liteta MARE.
- O functie definita in interiorul unei clase se numeste metoda. 
'''

# cam alambicat, greu am inteles sau nu prea

from f_functii2 import mathOperations
class Calculator:
    def __init__(self, num1, num2, num3): # ii spunem sistemului ca vream sa creem un constructor
        self._num1 = num1
        self._num2 = num2
        self._num3 = num3 #_nu inseamna ca este privat ci doar o conventie pt definirea constructorilor

    def max2(self, num1, num2):
        #num1 este marcat cu mov deoarece in momentul in care sistemul primeste o functie in interiorul unei clasei el
        #  asteapta ca acea clasa sa aibe un indicator care sa spuna ca acea functie face parte din clasa respectiva.
        #  pt asta trebuie sa punem in fata keywordu-ul self, prin care ii spunem sistemului ca acea functie max2 este
        #  o functie care apartine clasei Carculator
        if num1 > num2:
            return num1
        else:
            return num2

    def max3(self, num1, num2, num3):
        return self.max2(num1, self.max2(num2, num3))
        #aici max2 este subliniat cu rosu, eroare. noi am definit functiam max2 ca fiind o functie apartinind clasei Calculator
        # si cand scriem aceste return max2 ii spunem sistemului ca vrem sa sa se foloseasca de o functie max2 independenta de
        # clasa si nu o gaseste. ca sa putem sa ne folosm de functie pe care am definit-o mai devreme trebuie si aici sa punem
        # self.max2 in fata lui max2

    def test_max3(self):
        #scriem doar self pt ca nu vrem sa avem parametri, ci doar sa anuntam sistemul ca este o metoda
        # care apartine c,lasei.
        return self.max3(45, 8, 69) #am apelat o functie care apartine clasei. test_max3 nu are nici un parametru dar am apelat
                            # o alta functie cu niste parametrii. test_max3 a fost o functie definita in interiorul clasei
                            # pt a putea sa testam functia max3

    def max3v2(self):  #self ii spunem sist ca aceasta este o functie care apartine clasei, este dependenta de acea clasa
        def max2v2(nr1, nr2):  #nested functions - functii imbricate. functii definite in interiorul altei functii.
            if nr1 > nr2:
                return nr1
            else:
                return nr2
        return self.max2(self._num1, max2v2(self._num2, self._num3)) # self.max2 pt ca vrem sa apelem metoda max2 definita in clasa.

    def math_operation(self, a, b, operation):
        return mathOperations(a, b, operation) # este cu rosu pt ca trebuie sa importam cu from f_functii2 import mathOperations

''' CONSTRUCTOR = un bloc de cod care ne ajuta sa creem un anumit obiect
- constructor implicit = este cel care este apelat automat de Python in momentul in care apelam un obiect
- constructor explicit 
'''

''' instructiuni care se pot executa cu constructor implicit '''
# calculator = Calculator() # am definit un obiect de tip calculator
# print(calculator) #=><__main__.Calculator object at 0x0000029AB8C39FD0> printeaza obiectul in sine si nu ceva legat de obiectul respectiv
# #dupa ce printam obiectul o sa vrem sa folosim o metoda din clasa Calculator. O metoda poate sa fie accesata prin intermediul obictului.
# print(calculator.test_max3()) #=> 69
# print(calculator.max3(20, 56, 28)) #=>56
# print(calculator.max2(256, 325)) #=>325
# print(calculator.math_operation(20,60,'+')) #=>80

''' instructiuni care se pot executa cu constructor explicit'''
calculator = Calculator(5, 9, 30) #=> 30, calculator aici nu este variabila ci obiect.iar Calculator este clasa.
print(calculator.max3v2())
