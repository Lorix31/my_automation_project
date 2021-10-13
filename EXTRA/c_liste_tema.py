'''avand o lista de forme geometrice
forme = ['cerc', 'triunghi', 'dreptunghi', 'patrat']
 introduceti in lista, un 'trapez'. Dar acesta sa fie tot timpul pozitionat dupa triunghi. Indiferent unde ar fi acesta
 rezultat => rezultat: ['cerc', 'triunghi', 'trapez', 'dreptunghi', 'patrat'].
codul trebuie sa mearga la fel de bine, fara alte interventii si pentru o lista care arata asa ['cerc', 'dreptunghi', 'triunghi', 'patrat']
 sau asa ['cerc', 'dreptunghi', 'patrat', 'triunghi']
'''

#rezolvare
#1 - verificare cu if
forme = ['cerc', 'triunghi', 'dreptunghi', 'patrat']
print(forme)
if 'triunghi' in forme:
    forme.insert(forme.index('triunghi')+1, 'trapezul') # =>['cerc', 'triunghi', 'trapezul', 'dreptunghi', 'patrat']
    print(forme)
else:
    print('Nu se poate adauga trapez pentru ca triunghi nu este in lista')


#2
forme = ['triunghi','cerc', 'dreptunghi', 'patrat']
print(forme)
forme.insert(forme.index('triunghi')+1, 'trapez')
print(forme) #=>['triunghi', 'trapez', 'cerc', 'dreptunghi', 'patrat']






