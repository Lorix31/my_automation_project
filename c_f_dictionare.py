'''Dictionarele sunt colectii de date neordonate care stocheaza perechi cheie -valoare. Nu au index.
Vor fi folosite pentru API Testing
Exista doua feluri de a defini un dictionar:

1. Prin a specifica valorile intre acolade { }
2. Prin a enumera un sire de elemente cheie:valoare intre paranteze ( ) si prin a folosi keyword-ul dict


deci primul ex de mai jos este un sir transformat in dictionar, cu keyword-ul dict, si  nu este dictionar


-se pot adauga perechi key-value precum string(text), int(numar), key boolean si valoarea lista
- si se poate aduga un alt dictionar in interiorul dictionarului
'''

myDict = dict(a=1, b="Bella Ciao") # aici avem un sir de elemente cheie - valoare pe care l-am transformat in dcitionar cu functia dict
print(myDict) #=>{'a': 1, 'b': 'Bella Ciao'}
print(type(myDict)) #=> <class 'dict'>


myDict1 = {"a": "My data for a",
          "b": "My data for b",
          3: "Python",
          True: [5, 6, 45],
          "c": [dict(a=1, b="Bella"), dict(a=1, b="Ciao"), dict(a=1, b="aloha")]}
''' myDict1 este un dictionar definit intre { } care are CHEILE a (de tip string) ,b (de tip string) ,3 (de tip int, True (de tip boolean)
si c (de tip string)   VALORILE  My data for a/b/Python((de tip string) , [5,6,45) de tip lista si la c o lista de 3 dicitonare)'''

# # cheia si valoarea sunt separate intre ele de :....ex "a' este cheie si My data for a' este valoarea"
# #=>{'a': 'My data for a', 'b': 'My data for b', 7: 'Python', True: [5, 16, 45], 'c': [{'a': 1, 'b': 'Bella'}, {'a': 1, 'b': 'Ciao'}, {'a': 1, 'b': 'aloha'}]}


print(myDict1)
#=>{'a': 'My data for a', 'b': 'My data for b', 3: 'Python', True: [5, 16, 45], 'c': [{'a': 1, 'b': 'Bella'},
# {'a': 1, 'b': 'Ciao'}, {'a': 1, 'b': 'aloha'}]}

# # # Posibilitati de extragere a unui element dintr-un dictionar:
# '''pentru a extrage un elemnt a dictionarului il punem intre [], diferenta dintre liste si disctionare este ca la liste
#  trebuie sa specificam pozitia la care se afla elemntul iar la dictionare trebuie sa specificam acea cheie pe care vrem
#  sa o extragem '''

print(myDict['a']) # extragem un element din colectie prin incadrarea lui in []  la lista trebuia sa alegem indexul,
# la dicitonare alegem cheia pe care vrem sa o extragem => 1
print(myDict['b']) # => Bella Ciao

print(myDict1['a']) #=> My data for a
print(myDict1[3]) #=> Python
print(myDict1[True]) #=> [5,6,45]
print(myDict1[True][1]) # vrem sa accesam din cheia True doar valoarea 6 din disctionar  => 6
print(myDict1['c'])
# vrem sa printam doar elementul Bella din MyDict1 de la cheia c =>[{'a': 1, 'b': 'Bella'}, {'a': 1, 'b': 'Ciao'}, {'a': 1, 'b': 'aloha'}]

print(myDict['b'][:5]) #=> Bella DE CEEEEEE????????????????

print(myDict1["c"][0]['b']) #=> Bella, am accesat elementul 'c' din disctionar care va fi funCtiona ca si nume de lista
#din lista repesctiva am scos primul element care este un dictionar, si din dictionar am scos elementul identificat prin cheia b

print(myDict.get(7)) # de ce a printat =>None ????????????????




'''MIE NU IMI DESCHIDE DICITIONARE TEXT???????? 
Dupa ce il deschide sa mut acolo codul:

{
"a": "My data for a",
"b": "My data for b",
name = 'Loredana'
'varsta' = 32
}

asa arata un ex de request in jason cand facem testare de API
=> deschidem un google chrome si scrie postman request, mergem pe imagini si avem un ex pe care nu l-am inteles :) dar 
poate inteleg mai tarziuu ce e
API - APLICATION PROGRAMMING INTERFACE un fel de modalitate de a comunica cu browserul 
'''



