'''
input = functie cu care luam date de la tastatura sau salvam datele de la tastatura intr-o variabila
tipuri de date:
- strig = sir de caractere, exemplu: 'an nastere!'
- int = un nr intreg, ex 124
- float = nr zecimal, ex: 3.14
- boolean/bool = true or false
- structuri de date:
    - list = o structura de date - o lista de mai multe elemente care stau toate in aceiasi variabila
    - tuples = memoreaza o secventa imutabila de valori.
    - dictionare/dict = memoreaza perechi cheie-valoare
    - set = memoreaza elemente care au voie sa apara o singura data
'''

expectedUsr='LORE' #declarare si intitializare a unei variabile. expectedUsr = variabila, LORE este data introdusa in variabila de tip string
expectedPass='abcd'
expectedPass = 'efg'#suprascriere, ia ultima valoare introdusa, scrie peste ce am scris initial

user=input('enter user ') #user este variabila = input este functie si intre () si '' se introduce parametru
# / parametru=datele de input (de intrare) dintr-o functie
print(user)
assert user==expectedUsr #assert verifica daca expresia ce urmeaza este adevarata; == este un operator de comparare

