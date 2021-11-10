#TEMA1
'''
clasa Masina
ATRIBUTE definite inainte de constructor
- culori optionale - lista (ce vreti voi, macar 3)
- culoare masina - gri (toate masinile sunt gri cand ies din fabrica)
- viteza - 0 (stau pe loc initial)
- usa_deschisa - False (incep cu usile inchise)

CONSTRUCTOR
- marca masinii
- viteza maxima

METODE:
- afisare culori optionale()

- vopsire masina()
    daca culoarea nu e in lista, afisam eroare
    daca culoarea e in lista, modificam self.color

- accelerare()
    parametru de viteza, daca viteza > viteza maxima, viteza actuala va fi viteza maxima
    setam self.viteza, printam vrum vrum

- stop()
    printam stop
    setam viteza la 0

- deschide_usa()
    daca masina e in miscare sau daca usa e deja deschisa afisam ca nu se poate, altfel afisam CLICK, usa deschisa si
    setam usa_deschisa la true

- inchide_usa()
    daca usa e deschisa afisam CLICK, usa inchisa
    altfel afisam usa e deja inchisa

-   descriere()
    masina are marca x
    masina are viteza actuala x
    masina are culaorea x
    usile sunt deschise/inchise (aici un if else)

OBIECTE MASINA:
3 masini
- una ramane gri, accelereaza la 50, cu max speed 220, descriem
- una o vopsim rosie, deschidem usa, inchidem usa, inchidem iar usa, acceleram la 300, max speed 230, descriem
- una vopsim in culoare invalida, acceleram, deschidem usa (nu), franam, deschidem usa(da), descriem
'''


#REZOLVARE:
class Masina:
    culori_optionale = ['rosu', 'verde', 'negru', 'maro', 'albastru']
    culoare_fabrica = 'gri'
    usi_deschise = False # usa e inchisa
    viteza = 0

    def __init__(self, marca, viteza_maxima):
        self.marca = marca
        self.viteza_maxima = viteza_maxima

    def afisare_culori_optionale(self):
        print(self.culori_optionale)


    def vopsire_masina(self, culoare_aleasa):
        if culoare_aleasa in self.culori_optionale:
            self.culoare_vopsita = culoare_aleasa
            print(f'Am vopsit masina in {self.culoare_vopsita} ')
        else:
            print(f'Nu avem disponibila culoarea {culoare_aleasa}')


    def accelerare(self, viteza_dorita):
        if viteza_dorita > self.viteza_maxima:
            self.viteza = self.viteza_maxima
        else:
            self.viteza = viteza_dorita
        print('Vrum Vrum')


    def stop(self):
        self.viteza = 0
        print(f'STOP, viteza este {self.viteza}')

    def deschide_usa(self):
        if self.usi_deschise == False and self.viteza == 0 : #sau !=True era acelasi lucru
            print('CLICK, deschide usa')
        else:
            print('Usa este deja deschisa sau masina este in miscare')

    def inchide_usa(self):
        if self.usi_deschise != False: #usa este deschisa
            print('CLICK, inchide usa')
        else:
            print('Usa este deja inchisa')

    def descriere(self):
        print(f'Masina are marca {self.marca}')
        print(f'Masina are viteza actuala {self.viteza}')
        print(f'Masina are culoarea {self.culoare_vopsita}')
        if self.usi_deschise == False:
            print(' Usile sunt inchise')
        else:
            print(' Usile sunt inchise')

#creare obiecte si utilizare atribute care au aceiasi  valoare pt toate obiectele
print('********Printare atribute obiect masina BMW********')
bmw = Masina('BMW', 220)
print('Culoarea din fabrica pt BMW este: ', bmw.culoare_fabrica) #=> Culoarea din fabrica pt bmw este:  gri
print('Culorile optionale disponibile pt BMW sunt: ', bmw.culori_optionale) #=>Culorile optionale disponibile pt bmw sunt:  ['rosu', 'verde', 'negru', 'maro', 'albatru']
print(bmw.usi_deschise) #=> False
print('Viteza curenta pentru BMW este ' , bmw.viteza) #=>Viteza curenta pentru BMW este  0
print('Marca masinii este: ', bmw.marca) #=>Marca masinii este:  BMW
print('Masina poate sa atinga o viteza maxima de: ', bmw.viteza_maxima, 'km/h') #=>Masina poate sa atinga o viteza maxima de:  220 km/h


print('*************VERIFICARE METODE*******************')
bmw.afisare_culori_optionale() #=>['rosu', 'verde', 'negru', 'maro', 'albatru']
bmw.vopsire_masina('verde') #=>Am vopsit masina in verde
bmw.accelerare(250) #=>Vrum Vrum
bmw.stop() #=>STOP, viteza este 0
bmw.deschide_usa() #=>CLICK, deschide usa
bmw.inchide_usa() #=>Usa este deja inchisa
bmw.descriere() #=>Masina are marca BMW / Masina are viteza actuala 0 /Masina are culoarea verde
bmw.accelerare(250) #=>Vrum Vrum
bmw.descriere() #=>Masina are marca BMW / Masina are viteza actuala 220 /Masina are culoarea verde

print('___________________________________________')
print('*******Printare atribute obiect masina AUDI********')
audi = Masina('AUDI', 230)
print('Culoarea din fabrica pt AUDI este: ', audi.culoare_fabrica) #=> Culoarea din fabrica pt audi este:  gri
print('Culorile optionale disponibile pt AUDI sunt: ', audi.culori_optionale) #=> Culorile optionale disponibile pt audi sunt:  ['rosu', 'verde', 'negru', 'maro', 'albatru']
print(audi.usi_deschise) #=> False
print('Viteza curenta pentru AUDI este ' , audi.viteza) #=>Viteza curenta pentru AUDI este  0
print('Marca masinii este: ', audi.marca) #=>Marca masinii este:  AUDI
print('Masina poate sa atinga o viteza maxima de: ', audi.viteza_maxima, 'km/h') #=>Masina poate sa atinga o viteza maxima de:  230 km/h


print('*************VERIFICARE METODE*******************')
audi.afisare_culori_optionale() #=>['rosu', 'verde', 'negru', 'maro', 'albatru']
audi.vopsire_masina('roz') #=>Nu avem disponibila culoarea roz
audi.vopsire_masina('maro')
audi.accelerare(80) #= Vrum Vrum
audi.stop() #=>STOP, viteza este 0
audi.deschide_usa() #=>CLICK, deschide usa
audi.inchide_usa() #=>Usa este deja inchisa
audi.accelerare(110) #= Vrum Vrum
audi.descriere() #=>Masina are marca AUDI /Masina are viteza actuala 110/Masina are culoarea maro



print('___________________________________________')
print('********Printare atribute obiect masina VW********')
vw = Masina('VW', 150)
print('Culoarea din fabrica pt VW este: ', vw.culoare_fabrica) #=>Culoarea din fabrica pt vw este:  gri
print('Culorile optionale disponibile pt VW sunt: ', vw.culori_optionale) #=>Culorile optionale disponibile pt vw sunt:  ['rosu', 'verde', 'negru', 'maro', 'albatru']
print(vw.usi_deschise) #=> False
print('Viteza curenta pentru VW este ' , vw.viteza) #=>Viteza curenta pentru VW este  0
print('Marca masinii este: ', vw.marca) #=>Marca masinii este:  VW
print('Masina poate sa atinga o viteza maxima de: ', vw.viteza_maxima, 'km/h') #=>Masina poate sa atinga o viteza maxima de:  150 km/h

print('*************VERIFICARE METODE*******************')
vw.afisare_culori_optionale() #=>['rosu', 'verde', 'negru', 'maro', 'albatru']
vw.vopsire_masina('albastru') #=>Nu avem disponibila culoarea mov
vw.accelerare(100) #=Vrum Vrum>
vw.stop() #=>STOP, viteza este 0
vw.deschide_usa() #=>CLICK, deschide usa
vw.inchide_usa() #=>Usa este deja inchisa
vw.deschide_usa() #=>CLICK, deschide usa
vw.accelerare(130) #=>Vrum Vrum
vw.descriere() #=>Masina are marca VW / Masina are viteza actuala 130 / Masina are culoarea albastru



#
# # TEMA 2
# '''
# Ne imaginam un lant hotelier cu multe hoteluri cu etaje diferite, cu multe lifturi inauntru
# clasa Lift
# - etaj curent (va fi la 0 pentru toate lifturile)
#
# CONSTRUCTOR
# - nume hotel
# - numarul de etaje
#
# METODE
# - afiseaza_optiuni()
#     print('Liftul are {x} etaje')
#
# - urca() - la ce etaj? - dorinta
#     vom urca doar daca etajul curent este mai mic decat etajul dorit
#     print(ai urcat la etajul x)
#     SAU
#     print(Eroare)
#
# - coboara() - la ce etaj? - dorinta
#     vom cobora doar daca etajul curent este mai mare decat etajul dorit
#     print(ai coborat la etajul x)
#     SAU
#     print(Eroare)
#
# -descrie()
#     Liftul este in hotelul
#     Liftul este la etajul x
# '''
#
# #REZOLVARE:
# class Lift:
#     etaj_curent = 0
#
#     def __init__(self, nume_hotel, nr_stele):
#         self.nume_hotel = nume_hotel
#         self.nr_stele = nr_stele
#
#
#     def afiseaza_optiuni(self, nr_etaje):
#         self.etaj = nr_etaje
#         print(f'Liftul  are {self.etaj} etaje')
#
#     def urcat(self, etajul_dorit):
#
#         if etajul_dorit > self.etaj_curent and etajul_dorit <= self.etaj:
#             self.etaj_curent = etajul_dorit
#             print(f'Ai urcat la etajul {self.etaj_curent}')
#
#         else:
#             print(f'Nu poti urca la {self.etaj_curent} deoarece hotelul are doar {self.etaj}')
#
#
#
#     def coboara(self, etajul_dorit):
#         if etajul_dorit < self.etaj_curent and etajul_dorit>=0:
#             self.etaj_curent = etajul_dorit
#             print(f'Ai coborat la etajul {etajul_dorit}')
#         else:
#             print('eroare')
#
#     def descriere(self):
#         print(f'Descriere: Liftul este in hotelul {self.nume_hotel} si este un hotel de {self.nr_stele} stele. Acum liftul este la etajul {self.etaj_curent}')
#
# #creare obiecte si utilizare atribute
# lift_marriott = Lift('Marriott', '4*')
# print('********Printare atribute obiect lift Marriott********')
#
# print('Liftul de la Marriott este la etajul', lift_marriott.etaj_curent)
# print('Suntem la hotelul ', lift_marriott.nume_hotel, 'si este un hotel de ', lift_marriott.nr_stele)
#
# print('*************VERIFICARE METODE*******************')
# lift_marriott.afiseaza_optiuni(10)
# lift_marriott.urcat(0) #=>Ai urcat la etajul 0
# lift_marriott.urcat(8) #=> Ai urcat la etajul 8
# #lift_marriott.urcat(15) #=>Nu poti urca la 15 deoarece hotelul are doar 10
#
# lift_marriott.descriere()
#
#
# print('___________________________________________')
# print('********Printare atribute obiect lift Holiday Inn********')
# lift_holiday_inn = Lift('Holiday Inn', '3*')
# print('Liftul de la Holiday Inn este la etajul', lift_holiday_inn.etaj_curent)
# print('Suntem la hotelul ', lift_holiday_inn.nume_hotel, 'si este un hotel de ', lift_holiday_inn.nr_stele)
#
# print('*************VERIFICARE METODE*******************')
# lift_holiday_inn.afiseaza_optiuni(8)
# lift_holiday_inn.urcat(0) #=>Ai urcat la etajul 0
# lift_holiday_inn.urcat(5) #=>Ai urcat la etajul 5
# #lift_holiday_inn.urcat(15) #=>Nu poti urca la 15 deoarece hotelul are doar 8
# lift_holiday_inn.descriere()
#
#
#
# print('___________________________________________')
# print('********Printare atribute obiect Best Western********')
# lift_best_western = Lift('Best Western', '5*')
# print('Liftul de la Best Western este la etajul', lift_best_western.etaj_curent)
# print('Suntem la hotelul ', lift_best_western.nume_hotel, 'si este un hotel de ', lift_best_western.nr_stele)
#
# print('*************VERIFICARE METODE*******************')
# lift_best_western.afiseaza_optiuni(12) #=>Liftul  are 12 etaje
# lift_best_western.urcat(0) #=>Ai urcat la etajul 0
# lift_best_western.urcat(3) #=>Ai urcat la etajul 3
# lift_best_western.urcat(16) #=>Nu poti urca la 16 deoarece hotelul are doar 12
# lift_best_western.descriere() # DAR daca decomentez etajul 16 imi zice ca sunt la etajul 16....