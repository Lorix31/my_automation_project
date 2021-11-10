class Semafor:
    #atribute care au aceiasi valoare de inceput pentru toate obiectele
    culori_posibile = ['rosu','galben','verde'] #am ales  culorile posibile
    este_pornit = False # toate semafoarele vor incepe oprite
    sunet_verde = 'Bing Bing!'


    #CONSTRUCTOR - aici setam atribute diferite pt fiecare obiect (dorinte)
    def __init__(self, adresa_dorita, culoarea_de_start_dorita):
        self.adresa = adresa_dorita #trebuie sa salvam dorintele in atribute permanente(care incep cu self)
        self.culoare_curenta = culoarea_de_start_dorita


    # Metode care ofera ofera functionalitate obiectelor
    def pornim_semaforul(self):
        #functia seteaza atributul unde tinem statusul semaforului in True (functiile manipuleaza atributele)
        self.este_pornit = True
        print('Pornim semaforul')

    def oprim_semaforul(self):
        print('Oprim semaforul')
        self.este_pornit = False

    def modificare_sunet_verde(self, noul_sunet_dorit):
        #vrem sa suprascriem valoarea in care tinem sunetul verde
        self.sunet_verde = noul_sunet_dorit
        print(f' Noul sunet pentru verde este {self.sunet_verde}')

    def modificam_culoarea_curenta(self, noua_culoare_dorita):
        #verificam daca culoarea este permisa
        if noua_culoare_dorita in self.culori_posibile:
            #vreau sa setez noua culoare
            self.culoare_curenta = noua_culoare_dorita
            print(f'Noua culoare este {self.culoare_curenta} ')
        else:
            print('Culoare invalida')


#cream un obiect  de tip semafor
print('Rezultate semafor1: ')
semafor1 = Semafor('Primaverii', 'verde')

# #cand vrem sa accesam atribute sau metode a unui obiect incepem cu numele lui urmat de punct(.)
print(semafor1.este_pornit) # =>False
print(semafor1.culori_posibile) #=> ['rosu', 'galben', 'verde']('Primaverii', 'verde')
print(semafor1.adresa) #=>Primaverii
print(semafor1.culoare_curenta) #=>verde
print(semafor1.sunet_verde) # =>Bing Bing!


print('___________________________________________________')
#mai facem un obiect de tip semafor, dar este alta entitate
print('Rezultate semafor2: ')
semafor2 = Semafor('Izlazului', 'rosu')
print(semafor2.este_pornit) # =>False
print(semafor2.culori_posibile) #=> ['rosu', 'galben', 'verde']
print(semafor2.adresa) #=>Izlazului
print(semafor2.culoare_curenta) #=> rosu
print(semafor2.sunet_verde) # =>Bing Bing!


# ACCESAM METODELE
#pornim semaforul 1
semafor1.pornim_semaforul() #=>Pornim semaforul

#modificam sunetul pt semaforul 1
semafor1.modificare_sunet_verde('Ding Dong') #=>Noul sunet pentru verde este Ding Dong


print(semafor1.sunet_verde) #=>Ding Dong
print(semafor2.sunet_verde) #=>Bing Bing!

# pt semafor 1 o sa modificam culoarea in mov iar pt semafor 2 in galben
# verificam culoarea curenta
print(semafor1.culoare_curenta) #=>verde
semafor1.modificam_culoarea_curenta('mov') #=>Culoare invalida

semafor2.modificam_culoarea_curenta('galben') #=>Noua culoare este galben
print(semafor2.culoare_curenta) #=>galben
