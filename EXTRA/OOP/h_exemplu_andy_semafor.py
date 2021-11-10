'''
V-am pregatit o mica surpriza. O alta abordare a unui semafor. Sa vedeti ca imaginatia noastra este limita :)

copiati de aici, dati run
apoi studiati putin codul si incercati sa intelegeti de ce merge asa

acest semafor se va schimba automat cate secunde decideti voi

'''

from time import sleep

class Semafor:

    culoare = ''
    pornit = False
    sunet_verde = 'Ding Ding!'

    def __init__(self, strada):
        self.strada = strada

    def start_semafor(self, secunde_dorite):
        self.pornit = True
        print(f'Pornim semaforul de pe strada {self.strada}')
        print(f'Va merge {secunde_dorite} secunde apoi se va opri singur')

        # contorizam aici cate secunde au trecut de la pornire, incepem de la 0
        secunde_trecute = 0

        while self.pornit == True: # atat timp cat semaforul este pornit

            self.culoare = 'verde'
            print(f'Culoarea semaforului este {self.culoare}')
            print(self.sunet_verde)

            #asteptam 5 secunde la verde
            secunde_trecute = secunde_trecute + 5
            sleep(5)

            self.culoare = 'galbena'
            print(f'Culoarea semaforului este {self.culoare}')
            print('ATENTIE!')

            # asteptam 2 secunde la galben
            secunde_trecute = secunde_trecute + 2
            sleep(2)

            self.culoare = 'rosie'
            print(f'Culoarea semaforului este {self.culoare}')
            print('STOP!')

            # asteptam 5 secunde la rosu
            secunde_trecute = secunde_trecute + 5
            sleep(5)

            # cand trec secundele, oprim semaforul
            if secunde_trecute >= secunde_dorite:
                self.pornit = False
                print('Oprim semaforul')


semafor1 = Semafor('Primaverii')
semafor1.start_semafor(20) #aici decideti cate secunde doriti sa mearga