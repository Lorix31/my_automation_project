print('__________________________________________________________________________________________________________')

#1. tema Larisa - DE VERIFICAT DACA AM INTELES!!!!
''' Remove first n characters from a string (n il cititi de la tatatura)
"Ana are mere" daca n=3 va afisa " are mere"'''
# hint Andy - am cautat pe google asa ' how to remove first n chars from string python" si
# am ajuns aici  https://www.kite.com/python/answers/how-to-remove-first-n-characters-from-a-string-in-python
#apoi solutia este
n = int(input('alege valoarea lui n '))
ana = "Ana are mere"
sliced = ana[n:] #sliced este o functie care ce face exact?
print(sliced)
'''
1. citim pe n de la tastatura si il fortam sa fie INT
2. declaram si initializam variabila ana'''


print('__________________________________________________________________________________________________________')
#2. alt exemplu
my_string = 'buna ziua'
print(my_string[1:]) #=>una ziua

propozitie = "Ana are mere"
sliced = propozitie[0:] #=> ana are mere
print(sliced)

print('__________________________________________________________________________________________________________')

#3. Vreau sa va arat un exercitiu rezolvat. sa imi ziceti daca intelegeti de ce e asa. Rolul este sa intelegem inca o data
# functia len() si sa vedem ca putem avea un string creat asa. ana = 'a' * 3
username = input("alege utilizator ") #luam date de la tastatura
password = input("alege parola ")
dimensiune_parola = len(password) #functia len ne zice cate litere are parola
# ana = "a" * 3 => ana va fi "aaa"
parola_ascunsa = '*' * dimensiune_parola #generam un string care sa aiba caracterul '' inmultit cu dimensiunea parolei
print(f"The password for user {username} is {parola_ascunsa} and is {dimensiune_parola} characters long")

#inca o data rezolvarea + filmare
username = input("alege utilizator") #luam date de la tastatura
password = input("alege parola")
dimensiune_parola = len(password) #functia len ne zice cate litere are parola
# orice_string = "ab" * 3 => orice_string va fi "ababab" (doar un exemplu)
parola_ascunsa = '*' * dimensiune_parola #generam un string care sa aiba caracterul '*' inmultit cu dimensiunea parolei
print(f"The password for user {username} is {parola_ascunsa} and is {dimensiune_parola} characters long")

print('__________________________________________________________________________________________________________')

print('''EXERCITII DE PE NET DE REZOLVAT''')

''' 4. Crea??i c??te o variabil?? de tipul: string, int ??i float, dup?? cum urmeaz??:
Variabila de tip int va re??ine valoarea 20.
Variabila de tip float va re??ine valoarea 10.
Variabila de tip string re??ine valoarea ???python???.
'''
#Rezolvare:
variabila_int = 20
variabila_float = 10.0
variabila_str = 'python'

print('__________________________________________________________________________________________________________')

'''5. Utiliz??nd func??ia type, determina??i tipul urm??toarelor variabile:
restanta = 0
notaFinala = 10.0
laborator = ???Introducere in informatica???'''
# Rezolvare
restanta = 0
notaFinala = 10.0
laborator = 'Introducere in informatica'
print(type(restanta)) # => <class 'int'>
print(type(notaFinala)) # => <class 'float'>
print(type(laborator)) # => <class 'str'>

print('__________________________________________________________________________________________________________')
''' 6. Crea??i o list?? cu numele fetelor din grupa voastr?? (numele nu trebuie s?? fie distincte). Respect??nd ordinea cerin??elor rezolva??i urm??toarele cerin??e:
Sorta??i lista de nume.
Utiliz??nd o list?? auxiliar??, determina??i num??rul de apari??ii al fiec??rui nume.
Determina??i numele care apare de cele mai multe ori ??n lista ini??ial??.
Determina??i numele care apare de cele mai pu??ine ori ??n lista ini??ial??.
Revenind la lista ini??ial?? de nume, inversa??i ordinea elementelor.'''
#Rezolvare
#Sorta??i lista de nume.
lista = ['Lore', 'Giorgi', 'Andra', 'Ale', 'Ramona', 'Gianina', 'Roxana', 'Diana']
lista.sort()
print(lista)
# => ['Ale', 'Andra', 'Diana', 'Gianina', 'Giorgi', 'Lore', 'Ramona', 'Roxana']

#Utiliz??nd o list?? auxiliar??, determina??i num??rul de apari??ii al fiec??rui nume.
lista_auxiliara = ['Ana', 'Lore', 'Maria', 'Giorgi', 'Claudia', 'Lore', 'Andra'. 'Lore']

#Determina??i numele care apare de cele mai multe ori ??n lista ini??ial??.
#Determina??i numele care apare de cele mai pu??ine ori ??n lista ini??ial??.
#Revenind la lista ini??ial?? de nume, inversa??i ordinea elementelor

print('__________________________________________________________________________________________________________')
''' 7. Crea??i cu ajutorul unui dic??ionar o baz?? de date ??n care s?? re??ine??i numerele de telefon ale colegilor de grup??.'''
# Rezolvare


print('__________________________________________________________________________________________________________')
'''8. Scrie??i o secven???? de cod care s?? afi??eze ??n consol?? toate numerele pare divizibile cu 7 din intervalul 
[0, 3463]. Hint: utiliza??i func??ia xrange. Ajusta??i codul astfel ??nc??t la apari??ia primului multiplu al lui 666, 
algoritmul s?? se opreasc??.'''
#Rezolvare:

print('__________________________________________________________________________________________________________')
'''9. Crea??i o clas?? denumit?? ???FamiliaMea???, iar obiectele asociate acesteia s?? corespund?? membrilor familiei voastre.
 Clasa va con??ine variabilele ???nume???, ???prenume???, ???v??rst?????, o list?? de pasiuni, denumit?? ???pasiuni??? ??i o func??ie denumit?? 
 ???motto???, care s?? afi??eze motto-ul familiei voastre.'''
#Rezolvare

print('__________________________________________________________________________________________________________')

'''10. tema petruta - 1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ??????the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

2. Define a Book class with the following attributes: Title, Author (Full name), Price.
Set the View() method to display information for the current book.
Write a program to testing the Book class.

3.  Create a Vehicle class with name,  max_speed and mileage instance attributes

Asta e mai grea. cat puteti din ea
:)
1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. 
Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
'''

#Rezolvare

print('__________________________________________________________________________________________________________')


