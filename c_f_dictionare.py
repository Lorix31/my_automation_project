'''Dictionarele sunt colectii de date neordonate care stocheaza perechi cheie -valoare.
Vor fi folosite pentru API Testing
Exista doua feluri de a defini un dictionar:

Dictionarele se definesc intre {}


se pot adauga perechi key-value precum string(text), int(numar), key boolean si valoarea lista
si se poate aduga un alt dictionar in interiorul dictionarului'''

myDict = dict(a=1, b="Bella Ciao") # aici avem un sir de elemente cheie - valoare pe care l-am transformat in dcitionar cu functutia dict
print(myDict) #=>{'a': 1, 'b': 'Bella Ciao'}

myDict1 = {"a": "My data for a",
          "b": "My data for b",
          7: "Python",
          True: [5, 16, 45],
          "c": [dict(a=1, b="Bella"), dict(a=1, b="Ciao"), dict(a=1, b="aloha")]}
print(myDict1)
print(myDict1["c"][0]['b']) #=> Bella, am accesat elementul 'c' din disctionar care va fi fucntiona ca si nume de lista
#din lista repesctiva am scos primul element care este un dictionar, si din dictionar am scos elementul identificat prin cheia b

# cheia si valoarea sunt separate ingtre ele de :....ex "a' este cheie si My data for a' este valoatrea"
#=>{'a': 'My data for a', 'b': 'My data for b', 7: 'Python', True: [5, 16, 45], 'c': [{'a': 1, 'b': 'Bella'}, {'a': 1, 'b': 'Ciao'}, {'a': 1, 'b': 'aloha'}]}


# # Posibilitati de extragere a unui element dintr-un dictionar:
print(myDict["a"]) #=> 1
'''pentru a extrage un elemnt a dictionarului il punem intre [], diferenta dintre liste si disctionare este ca la liste
 trebuie sa specificam pozitia la care se afla elemntul iar la dictionare trebuie sa specificam acea cheie pe care vrem 
 sa o extragem '''

print(myDict1["a"]) #=>My data for a
'''s-a uitat la linia 15 unde am "a": "My data for a", si a vazut ca primul element cheie - valoare este my first data 
for a unde a este cheia si valoarea este my first data for a'''

print(myDict1["b"]) #=>My data for b
print(myDict[True]) #=> [5,6,45]
print(myDict[True][1]) #=> 6
print(myDict["b"][:5]) #=>Bella


print(myDict.get(7))