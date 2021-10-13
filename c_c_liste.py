''' Se definesc intre []'''

a = [1,2,3]
b = ['banane', 'mere', 'gutui']
c = [4, 'struguri', True]
print(a)
print(b)
print(c)
print(a,b,c) #=> le afiseaza pe acelasi rand [1, 2, 3] ['banane', 'mere', 'gutui'] [4, 'struguri', True]
print(a[0]) #=> printeaza primul element din lista a => 1
print(a[0], b[0], c[0]) #=>, banane, 4 = printeaza primul element din fiecare lista
print('primul element din fiecare lista este urmatorul: ' , a[0], b[0], c[0]) #=> primul element din fiecare lista este urmatorul:  1 banane 4, putem adauga si text
print(a[2],b[2],c[2]) # ne printeaza elementul de pe index 2, care acum este ultimul =>3 gutui True
print(a[-1],b[-1],c[-1]) # ne printeaza mereu ultimul emelen =>3 gutui True
# print(a[3]) # => list index out of range , ne da eroare pt ca nu exista element pe index 3
print(a[0:2]) #=> ne afiseaza toate elementele care au index mai mic ca 2 =>[1, 2]
print(b.count('mere'))#numara cate mere avem in lista => 1

c[-1] = 'portocale'
print(c) #=> inlocuieste un singur element din lista => din true in portocale [4, 'struguri', 'portocale']

print(sum(a)) #=>6 aduna
a.clear() #=> sterge lista a => []adica lista e goala
print(a)
a.append(3) #adauga un element la finalul listei => 3
print(a)
print(3 in a)#=> verifica daca elementul 3 se afla in lista a => True
