#tema Larisa - DE VERIFICAT DACA AM INTELES!!!!
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



#alt exemplu
my_string = 'buna ziua'
print(my_string[1:]) #=>una ziua

propozitie = "Ana are mere"
sliced = propozitie[0:] #=> ana are mere
print(sliced)

#Vreau sa va arat un exercitiu rezolvat. sa imi ziceti daca intelegeti de ce e asa. Rolul este sa intelegem inca o data
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