'''seturie se definesc intre {} '''
my_set = {13, 5, 67, 42}
print(my_set) #=>{13, 42, 67, 5}
my_set = {13, 5, 67, 42, 5}
print(my_set) #=>{13, 42, 67, 5} nu afiseaza de 2 ori elementul 5
my_list = [13,5,67,42,5]
print(my_list) #=>[13, 5, 67, 42, 5]
my_set.add(7)
print(my_set) #=> {67, 5, 7, 42, 13} - adauga un element nou insa nu e clar de ce il adauga pe acea positie
my_set.add(7.5)
print(my_set) #=>{67, 5, 7, 7.5, 42, 13}
my_set.add('Ana')
print(my_set) #poate adauga si string =>{67, 5, 7, 7.5, 42, 13, 'Ana'}
# print(my_set[0]) #=> da eroare pt ca este o colectie de date neordonate

print(set(my_list)) #=> transforma lista my_list in set si afiseaza o singura data valoarea 5 =>{5, 67, 42, 13}
print(list(set(my_list))) #=> transforma din set in lista apoi iar in set iar din set in lista [5, 67, 42, 13]
