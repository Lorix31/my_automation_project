
# o insiruire de elemente de orice tip , separate de virgula, care se definesc intre []

cars = ['Volvo', 'Audi', 'Dacia', 'BMW', 'trabant']

#elementele au un index, index catre incepe de la 0
print(cars[1]) #=>Audi

#slicing - parcurgere mai smecherasa, de unde pana unde
print(cars[1:]) #=>'Audi', 'Dacia', 'BMW' - parcurge de la 1 pana la final
print(cars[1:3]) #=>'Audi', 'Dacia' - de la 1 pana la 3 dar fara 3
print(cars[0:5:2]) #=>['Volvo', 'Dacia', 'trabant']( de la 0 la 5 din 2 in 2 - 2 este pasul
print(cars[::-1]) #=>['trabant', 'BMW', 'Dacia', 'Audi', 'Volvo'] - parcurgerea liste invers
print(cars[3:1:-1]) #=>['BMW', 'Dacia'] - parcurgem invers, porneste de la 3 la 1 dar fara ultimul, ultimul fiind 1

#Cateva metode specificr listelor. se introduc astfel: variabila.metoda
cars.append('Toyota')
print(cars) #=>adauga la final inca un element ['Volvo', 'Audi', 'Dacia', 'BMW', 'trabant', 'Toyota']
cars.remove('trabant')
print(cars) #=> ['Volvo', 'Audi', 'Dacia', 'BMW', 'Toyota']
cars.insert(1, 'Porche') # chiar daca e index nu il punem intre [] pt ca functia recunoaste indexul fara
print(cars) #=> ['Volvo', 'Porche', 'Audi', 'Dacia', 'BMW', 'Toyota'] adauga un element la o anumita pozitie data de index
ultimul_element = cars.pop() #=>eliminam ultimul element dar il si returnam (adica il putem salva in variabila)
print(ultimul_element) #=>Toyota
print(cars)#=>['Volvo', 'Porche', 'Audi', 'Dacia', 'BMW']
print(cars.index('BMW')) #=>4 , iti da indexul
cars.append('Volvo') # adauga inca un Volvo
print(cars) #=>['Volvo', 'Porche', 'Audi', 'Dacia', 'BMW', 'Volvo']
print(cars.count('Volvo')) #=>2
#-reverse DE COMPLETAT
cars.sort()
print(cars) #sortare alfabetica =>['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo']

cars2 = cars.copy()
print(cars2) # => ne face un backup la o lista, ne creaaza o noua lista identica
cars.clear()
print(cars) # sterge lista cars =>[] - noroc ca avem cars2:))
cars = cars2.copy()
print(cars)

expensive_cars = ['lamborghini', 'ferrari']
# cars.append(expensive_cars)
print(cars) #=>['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo', ['lamborghini', 'ferrari']] nu e bine pt ca ne ia lista in lista si ne citeste cele 2 masini ca un singur element
all_cars1= cars + expensive_cars
print(all_cars1) #=>['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo', 'lamborghini', 'ferrari'] - anuna 2liste
cars.extend(expensive_cars) #modifica lista de cars prin adaugarea elementelor din expernsive_cars la final
print(cars) #=>['Audi', 'BMW', 'Dacia', 'Porche', 'Volvo', 'Volvo', 'lamborghini', 'ferrari']
print(len(cars)) #cate elemente avem in lista =>8

#exercitiu - vreau sa printez penultimul element dintr-o lista.
culori=['alb', 'rosu', 'albastru']
print(culori[1]) #=> rosu doar ca eu vreau sa vad mereu penultimul element si eu mai adaug alte elemente nu mai vad tot timpul penultimul
culori=['alb', 'rosu', 'albastru', 'verde']
print(culori[len(culori)-1]) #=>verde
culori=['alb', 'rosu', 'albastru', 'verde', 'roz']
print(culori[len(culori)-2]) #=>verde
#sau
index = (len(culori)-2)
print(culori[index]) #=>verde, este la fel ca varianta de mai sus

# lista cu 5 fotbalisti. scoatem jucatorul A si introducem jucatorul B si afisam noua lista
echipa = ['A', 'B', 'C', 'D', 'E']
print(echipa) #=>['A', 'B', 'C', 'D', 'E']
jucator = input('jucatorul scos este ')
# echipa.remove('F')
# print(echipa) #=>eroare ca nu exista in lista
if jucator in echipa: #daca jucatorul este in lista
    echipa.remove(jucator) #scoate jucatorul cu remove
    print(f'jucatorul {jucator} a fost scos')
else:
    print('jucatorul nu este pe teren') # altfel afisam o eroare
print(echipa)
# A =>['B', 'C', 'D', 'E']
# jucatorul scos este A
#jucatorul scos este F
#jucatorul nu este pe teren

noul_jucator = input('noul jucator este ')
if noul_jucator in echipa:
    print('jucatorul este deja in teren')
else:
    echipa.append(noul_jucator)
    print(f'Am introdus jucatorul {noul_jucator}')
print(echipa)
''' pt jucator scos A si jucator nou B 
jucatorul A a fost scos
['B', 'C', 'D', 'E']
noul jucator este B
jucatorul este deja in teren
['B', 'C', 'D', 'E']

=>pt jucator A scos si jucator F introdus jucatorul scos este A
jucatorul A a fost scos
['B', 'C', 'D', 'E']
noul jucator este F
Am introdus jucatorul F
['B', 'C', 'D', 'E', 'F'] '''


