# rezolvat cu gabi insa nu cred ca am inteles....


'''
Exercitiul 1: Definiti o clasa Vehicul care sa ia urmatoarele atribute: viteza_maxima si kilometraj.
Cele doua atribute vor fi date de catre utilizator de la tastatura'''


class Vehicul:
    def __init__(self, viteza_maxima, kilometraj):  # definirea construcorului  = __init__ constructor de clasa explicit
        self._viteza_maxima = viteza_maxima  # variabila declarata in constructor, incare stocam viteza maxima
        self._kilometraj = kilometraj

    def calculeaza_timp(self, _viteza_maxima, distanta):  # definirea unei metode in interiroul clasei care calculeazaq timpul necesar pt a parcurge o distanta
        return int(distanta) / int(_viteza_maxima)


# Crearea obiectului
autobuz = Vehicul(100, 2000)
print(f'Autobuzul poate ajunge la destinatie in {autobuz.calculeaza_timp(100, 100)} ore')




# # asocierea clasei cu un obiect?
# viteza_maxima = Vehicul()
# kilometraj = Vehicul()
#
# # accesarea variabilelor uniui obiect?
# viteza_maxima.viteza = 'ceva dat de la tastatura cu input???'
# kilometraj.km = 'input o valoare'

'''Exercitiul 2: Creati un obiect numit autobuz pornind de la clasa Vehicul.
Obiectul respectiv va trebui sa poata sa apeleze o metoda care sa calculeze timpul pe care il face intre doua locatii
diferite, pornind de la distanta intre cele doua locatii si folosindu-ne de viteza data ca parametru in constructor.
Distanta intre cele doua locatii va fi data ca si parametru in metoda care calculeaza timpul, iar viteza vehiculului
va fi data ca si parametru in constructor
'''


# Rezolvare







#TEMA pt mine sa vad daca am inteles....
'''- Creaza o noua clasa care sa descrie excursia unei persoane. clasa respectiva ar trebui sa descrie un obiect pe baza 
atributelor urmatoare: cate pers calatoresc, sezonul, destinatia, nr zile sejur.
-In interiorul clasei se va defini o metoda care sa printeze pe ecran sezonul in care calatoreste clientul, destinatia si nr zile (def)
-Optional se va defini o alta functie care sa calculeze un discount de 10% in cazul in care clientul calatoreste iarna (if)
-Aditional se va crea un obiect care va instantia clasa respectiva'''


class Excursie:
    def __init__(self, nr_calatori, sezon, destinatie, nr_zile_sejur, tarif):  # definirea constructorului  = __init__ constructor de clasa explicit
        self.nr_calatori = nr_calatori
        self.sezon = sezon
        self.destinatie = destinatie
        self.nr_zile_sejur = nr_zile_sejur
        self.tarif = tarif

    def detalii_excursie(self):
        print(f'Cei {self.nr_calatori} turisti calatoresc in sezonul de {self.sezon}, in destinatia {self.destinatie} pt un nr de {self.nr_zile_sejur} nopti. Tariful pt excursie este {self.tarif}')

    def discount_sezon(self):
        if self.sezon == 'iarna':
            self.tarif = self.tarif - (self.tarif*0.10)
            print(f'Tariful cu discount al excursiei este {self.tarif}')
        else:
            print('Nu se aplica discounturi suplimentare')

#obiect 1
familia1 = Excursie(4,'vara','Grecia',7, 1500)

# verificare atribute
print(familia1.nr_calatori) #=>4
print(familia1.sezon) #=>vara
print(familia1.destinatie) #=>Grecia
print(familia1.nr_zile_sejur) #=>7
print(familia1.tarif) #=>1500

#verificare metode
familia1.detalii_excursie() #=>Cei 4 turisti calatoresc in sezonul de vara, in destinatia Grecia pt un nr de 7 nopti.Tariful pt excursie este 1500
familia1.discount_sezon() #=>Nu se aplica discounturi suplimentare


#obiect2
familia2 = Excursie(2,'iarna','Turcia',7, 1690)

# verificare atribute
print(familia2.nr_calatori) #=>2
print(familia2.sezon) #=>iarna
print(familia2.destinatie) #=> Turcia
print(familia2.nr_zile_sejur) #=>7
print(familia2.tarif) #=>1690

#verificare metode
familia2.detalii_excursie() #=>Cei 2 turisti calatoresc in sezonul de iarna, in destinatia Turcia pt un nr de 7 nopti.Tariful pt excursie este 1690
familia2.discount_sezon() #=>Tariful cu discount al excursiei este 1521.0

