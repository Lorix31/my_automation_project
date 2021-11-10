#TEMA 1. Din ce 101 Dalmatiei il cautam pe Pogo (D7) si ne oprim.CU WHILE!!

dalmatian = 0
while dalmatian <= 101:
    dalmatian = dalmatian + 1
    print('Dalmatianul cu nr ' + str(dalmatian))
    if dalmatian == 7:
         print('L-am gasit pe Pogo, dalmatianul 7')
         break

#TEMA 2. Ex cu continue- vreau sa NU afisez parintii (D7 si D17) CU WHILE!!
print('_________________________________________________________')
dalmatian = 0
while dalmatian in range(0,101):
    dalmatian = dalmatian + 1
    if dalmatian == 7 or dalmatian == 17:
        continue
    print(f'Dalmatian:  {dalmatian}')



#TEMA 3. tineti 7 L de benzina intr-o variabila. Atata timp cat masina mai are benzina printati "Acceleram! Vruum Vruum!".
# De fiecare data cand masina accelereaza se consuma 1 L de benzina. La final, pe un else, afisati "STOP! Nu mai este benzina"
#Rezolvare cu while:
print('_________________________________________________________')
print('Tema 3. Rezolvare cu while')
rezervor = 7
while rezervor >= 1:
    print('Acceleram! Vruum Vruum!')
    rezervor = rezervor -1
else:
    print('STOP! Nu mai este benzina...')

#Rezolvare cu for:
print('Tema 3. Rezolvare cu for')
for rezervor in range(7):
    print('Acceleram! Vruum Vruum!')
else:
    print('STOP! Nu mai este benzina...')
