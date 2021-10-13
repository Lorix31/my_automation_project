'''o masina merge pe strada si computerul de bord ne anunta daca suntem pe loc, in localitate, drum judetean sau autostrada
definim o variabila viteza actuala unde tinem viteza si verificam daca e pe loc (0), sau daca e in localitate
(unde poti merge cu max 50), sau pe drum judetean unde poti merge cu pana in 90, sau pe autostrada unde poti merge cu peste 90
si printam de fiecare data situatia masinii, unde se afla iar daca viteza e cu -, printam valoare invalida
'''

viteza_actuala = 120
if viteza_actuala<0:
    print('invalid')
elif viteza_actuala==0:
    print('masina sta pe loc')
elif viteza_actuala >= 1 and viteza_actuala <= 50:
    print('masina se deplaseaza in localitate')
elif viteza_actuala>=51 and viteza_actuala<=90:
    print('masina se deplaseaza pe un drum judetean')
else:
    print('masina se deplaseaza pe autostrada')
#rezultate => -1=invalid,0=masina sta pe loc, 1,49,50 = masina se deplaseaza in localitate, 51, 90 =judetean, 91, 120 = autostrada

''' Exercitiu dat de mine
- daca se anuleaza charterul, turistul primeste banii inapoi de la agentie
- daca turistul se imbolnaveste si are asigurare storno, turistul primeste banii incapoi de la asigurator
- daca turistul se imbolnaveste si nu are asigurare storno, penalizare conform contract
- daca se razgandeste, pierde banii'''
charter_anulat = True
asigurare_storno= True
imbolnavire_fara_asigurare = False
if charter_anulat:
    print('turistul primeste banii inapoi de la agentie')
else:
    print('penalizare ')

if asigurare_storno:
    print('turistul primeste banii incapoi de la asigurator')
else:
    print('penalizare ')

if imbolnavire_fara_asigurare:
    print('penalizare conform contract')
else:
    print('calatoreste')