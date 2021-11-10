'''Tema: De calculat numarul maxim dintr-o lista de 10 numere date de la tastatura folosind o instructiune
repetitiva (while, for)'''

#REZOLVARE LUATA DE PE NET INSA MA PIERD IN NOTIUNI
# def nrMax_lista_numere(numere): # definim o functie care 1 parametru-numere. dar de ce nu trecem aici 10 parametri
#     max = numere[0] # logica problemei. variabila max trebuie sa fie egala cu?????????
#     for nr in numere:
#         if nr > max: # daca nr este mai mare ca 0?
#             max = nr
#     return max
#
# #Apelare functie????
# numar = int(input('Cate numere vrei sa compari? : ')) # asta este o chestie foarte faina dar nu inteleg cum functioneaza
# lista = []
#
# for nr in range(numar):
#     numar = int(input('Introdu numar '))
#     lista.append(numar) # append adauga nr?
#
# print("Cel mai mare numar din lista este :",nrMax_lista_numere(lista))



# Rezolvarea mea incepea asa:
# lista_numere = []
# a = int(input('Introdu nr1: '))
# b = int(input('Introdu nr2: '))
# c = int(input('Introdu nr3: '))
# d = int(input('Introdu nr4: '))
# e = int(input('Introdu nr5: '))
# f = int(input('Introdu nr6: '))
# g = int(input('Introdu nr7: '))
# h = int(input('Introdu nr8: '))
# i = int(input('Introdu nr9: '))
# j = int(input('Introdu nr10: '))
#
#
# # def nrMax_lista():
# #     for nr in lista_numere:
# #         max =

print('_________________________________________________________')
max = 0
lista = []
for n in range(0,5):
    lista.append(int(input('Introdu nr urmator: ')))
print(lista) # =>[5, 6, 7, 4, 10]

def calculeaza_max(lista_parametru):
    max = 0
    for i in range (0, len(lista_parametru)): # intervalul este 0,1,2,3,4
        print('Valoarea curenta a lui i este: ', i)
        print('Maximul curent este: ', max)
        if max < lista_parametru[i]:
            max = lista_parametru[i]
    return max

#apelare
print(calculeaza_max(lista))




