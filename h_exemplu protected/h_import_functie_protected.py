'''incercam sa importam fisierul h_sursa_functie_protected.py'''

from h_exemplu_protected_sursa import h_sursa_functie_protected
#definim un obiect din clasa SursaProtected
from h_exemplu_protected_sursa.h_sursa_functie_protected import SursaProtected

# instantiere obiect
test = SursaProtected() #apare initial subliniat cu rosu, apasam pe beculet si ii dam import

#Apelam metoda SursaProtected
test._internal_logger()
#=>
#Protected method
#Protected method

'''
O metoda protected nu poate sa fie apelata intr-un alt pachet. tehnic ea poate fi apelata dar nu este un googpractice....
Functia internal_logger definita in programul h_sursa_functie_protected din pachetul h_exemplu_protected_sursa
nu ar trebui sa poata fi apelata in programul h_import_functie_protected din pachetul h_exemplu_protected. Ar trebui sa 
avem eroare pt ca sunt in pachete diferite dar tehnic merge deci doar prin conventie nu ar trebui sa facem asta.
'''

# test._internal_logger() - functie definita cu _ trebuie sa fie apelata in aceiasi clasa sau in alta clasa doar daca
#face parte din acelasi pachet 