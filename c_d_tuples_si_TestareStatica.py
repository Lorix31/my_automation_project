''' se definesc intre ()'''
my_tuples = (1, 2, 5, 7)
print(my_tuples[3])  # =>7
# print(my_tuples[5]) # eroare, pt ca acceseaza o pozitie care nu exista =>IndexError: tuple index out of range
print(5 in my_tuples)  # => True
print(14 in my_tuples)  # => False verifica daca elementul se afla in tuple sau nu
print(my_tuples.count(5))  # => 1 verifica de cate ori apare 5 in my tuples
# my_tuples[0] = 8 # => 'tuple' object does not support item assignment tuplurile nu se pot modifica
tup = 2, 3, 4
print(type(tup))  # =><class 'tuple'> NU AM INTELES CE FACE CAND PUNEM PARANYTEZE SAU NU PUNEM PARANTEZE
