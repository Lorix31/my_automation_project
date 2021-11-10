'''
Clasa = este o definitie teoretica a unui concept (reteta / blueprint/schelet).- nu exista fizic.
Obiect = sunt reprezentari fizice / concrete ale claselor. Obiectele sunt instante ale claselor, respectand definitiile aferente

O clasa se trece cu keyword-ul class Cont (cu litera mare)
'''

class Cont:
    #primul lucru dintr-o clasa = constructor
    # constructor = are rolul de a initializa valorile proprietatilor/atributelor
    def __init__(self, nume_constructor, cnp, iban, sold): #constructor / self - keyword pt reprezentarea clasei (atributele clasei)
        self.nume_clasa = nume_constructor #se va folosi initializarea clasei. nume mai sugestive
        self.cnp = cnp #dar asa se gasesc in viata reala
        self.iban = iban # toate astea sunt atribute
        self.sold = sold

    # pe langa atribute, o clasa mai contine functii/metode(=actiuni)
    def interogare_sold(self):
        print(f'Soldul titularului {self.nume_clasa} este de {self.sold} euro ')

    def alimentare_cont(self, suma_de_adaugat):
        print(f'Ai adaugat suma de {suma_de_adaugat}')
        self.sold = self.sold + suma_de_adaugat

    def retragere_numerar(self, suma_de_retras):
        if suma_de_retras <= self.sold:
            self.sold = self.sold - suma_de_retras
            print(f'Ai retras suma de {suma_de_retras}')
        else:
            print('Fonduri insuficiente')
            print(f'Ai vrut sa retragi {suma_de_retras} dar mai ai in cont {self.sold}')


