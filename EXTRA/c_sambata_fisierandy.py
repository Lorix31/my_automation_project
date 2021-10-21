# #1
# username = input("alege utilizator") #luam date de la tastatura
# password = input("alege parola")
# dimensiune_parola = len(password) #functia len ne zice cate litere are parola
# # orice_string = "ab" * 3 => orice_string va fi "ababab" (doar un exemplu)
# parola_ascunsa = '*' * dimensiune_parola #generam un string care sa aiba caracterul '*' inmultit cu dimensiunea parolei
# print(f"The password for user {username} is {parola_ascunsa} and is {dimensiune_parola} characters long")
#
# #2
# day = input("alege o zi din saptamana")
# #inainte sa verificam ziua, vrem sa procesam datele ca sa mearga si pt litere mari si pt spatii
# day = day.lower() # salvam in day, fosta valoare din day fortata cu litere mici
# day = day.replace(' ', '') # inlocuim toate spatiile cu nimic
# # intra pe prima ramura TRUE, ATAT! se opreste
# if day == 'sambata' or day == 'duminica': # daca ziua este egala cu sambata SAU duminica
#     print('weekend!')
#     print('Happy')
#     if day == 'duminica':
#         print('biserica')
# elif day in ['luni', 'marti', 'miercuri', 'joi', 'vineri']: # daca ziua este in lista?
#     print('weekday')
#     print('not so happy')
# else:
#     print('zi invalida')
#
# #3
# # cu CTRL + CLICK pe numele functieie (adica istitle), ajungem la definitia functiei
# titlu = 'Luceafarul'
# print(titlu.istitle()) # este titlu? DA sau NU
#
# #4
# #liste = insiruire de elemente de orice tip, separate de virgula, care se definesc intre paranteze drepte
# lista_mea = ['alb', True, 3, 3.14, [1, 2, 3]] # putem pune orice elemente
# print(lista_mea)
# cars = ['Volvo', 'Audi', 'Dacia', 'BMW', 'Trabant']
#
# # elementele au index, index care incepe de la 0
# print(cars[0]) # => Volvo
#
# # slicing - adica parcugere mai smecherasa, de unde pana unde
# print(cars[1:]) # => ['Audi', 'Dacia', 'BMW', 'Trabant] (de la unu pana la final)
# print(cars[1:3]) # => ['Audi', 'Dacia'] (de la unu pana la 3, dar fara ultimul)
# print(cars[0:5:2]) # ['Volvo', 'Dacia', 'Trabant'] (de la 0 la 5 din 2 in 2) - 2 este pasul
# print(cars[::-1]) # ['Trabant', 'BMW', 'Dacia', 'Audi', 'Volvo'] (parcurgem lista invers)
# print(cars[3:1:-1]) # ['BMW', 'Dacia'] (parcurgem invers de la 3 la 1, dar fara ultimul, ultimul fiind 1)
#
# # cateva metode specifice listelor
# cars.append('Toyota') # adauga la final inca un element
# print(cars) # => ['Volvo', 'Audi', 'Dacia', 'BMW', 'Trabant', 'Toyota']
# cars.remove('Trabant') # scoate un element dupa nume (exact asa cum e el)
# print(cars) # => ['Volvo', 'Audi', 'Dacia', 'BMW', 'Toyota']
# cars.insert(1, 'Porche') # adauga un element la o anumita pozitie
# print(cars) # => ['Volvo', 'Porche', 'Audi', 'Dacia', 'BMW', 'Toyota']
# ultimul_element = cars.pop() # eliminam ultimul element dar il si returnam (adica il putem salva in variabila)
# print(ultimul_element) # => Toyota
# print(cars) # => ['Volvo', 'Porche', 'Audi', 'Dacia', 'BMW']
# print(cars.index('BMW')) # => 4
# cars.append('Volvo') # adauga inca un Volvo
# print(cars.count("Volvo")) # => 2
# print(cars.reverse()) # inverseaza lista dar o si salveaza, ca sa vedem rezultatul, mai printam o data lista
# print(cars) # => ['Volvo', 'BMW', 'Dacia', 'Audi', 'Porche', 'Volvo']
# cars.sort() # sortare alfabetica
# print(cars) # => ['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo']
# cars2 = cars.copy() #ne face un backup la lista, salvam lista intr-o noua lista
# print(cars2) # => ['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo']
# cars.clear() # sterge lista
# print(cars) # => [] (o lista goala)
# # PFEW! noroc ca aveam backup, aducem inapoi masinile
# cars = cars2.copy() # o aducem inapoi, cum? copiem in cars continutul listei cars2
# print(cars) # => ['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo'] (lista initiala)
# expensive_cars = ["Lamburghini", "Ferrari"]
# all_cars1 = cars + expensive_cars # aduna 2 liste
# print(all_cars1)
# cars.extend(expensive_cars) # modifica cars prin adaugarea elementelor din expensive_cars la final
# print(cars) # => ['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo', 'Lamburghini', 'Ferrari']
# print(len(cars)) # => cate elemenete avem in lista, adica 8
#
# #5
# #vreau sa printez PENULTIMUL element dintr-o lista
# culori = ['alb', 'rosu', 'albastru', 'verde', 'roz']
# index = len(culori)-2
# print(culori[index])
# # 77, 78 la fel cu 80
# print(culori[len(culori)-2])
#
# #6
# #lista cu 5 fotbalisti, facem o chimbare, scoatem jucatorul A, introducem jucatoryl B, afisam noua echipa
# #lista cu 5 fotbalisti si facem o schimbare, scoatem jucatorul a si introducem jucatorul f si afisam noua echipa
# lista = ['a', 'b', 'c', 'd', 'e']
# print(lista)
# jucator = input('jucatorul scos este ') # alegem un jucator pe care vrem sa-l scoatem
# if jucator in lista: #daca jucatorul este in lista
#     lista.remove(jucator) #il scoatem afara din lista prin metoda remove
#     print(f'jucatorul {jucator} a fost scos') # afisam un mesaj ca am scos jucatorul
# else : #altfel
#     print('jucatorul nu este pe teren') #afisam o eroare
# print(lista) # printam lista dupa ce incercam sa facem scoaterea jucatorului
#
# noul_jucator = input('jucatorul introdus este ') # alegem sa introducem un jucator
# if noul_jucator in lista: # daca noul jucator este in lista deja
#     print('jucatorul este deja in teren') # afisam ca el este deja pe teren, nu il putem introduce
# else: # altfel
#     lista.append(noul_jucator) # introducem noul jucator, finalizam schimbarea
#     print(f'am introdus jucatorul {noul_jucator}') # afisam un mesaj ca am introdus jucatorul
# print(lista) # printam echipa finala

# forme = ['cerc', 'dreptunghi', 'patrat', 'triunghi']
# index_triunghi = forme.index('triunghi')
# print(index_triunghi)
# forme.insert(index_triunghi+1, 'trapez')
# print(forme)

txt = input('alege un sir de caractere format doar din cifre')
if txt.isnumeric():
    if txt[0] == txt[len(txt)-1]:
        print('prima cifra egala cu utlima')
    else:
        print('prima cifra NU este egala cu ultima')
else:
	print('Nu ai introdus doar cifre')