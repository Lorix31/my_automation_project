#stackowerflow.com - site unde putem sa gasim raspunsuri
#w3school.com - site unde putem sa gasim raspunsuri si exercitii
# cream un dosar cu click dr pe proiect - new - directory

''' Variabile = zone din memorie, care fac referire la un tip de data/structura de date
Variabilele incep cu litera mica, nu pot sa contina spatii, pot sa contina cifre dar sa nu inceapa cu cifre, si sunt legate
de _ sau al 2lea cuvand cu litera mare '''

#PRINCIPALELE 4 TIPURI DE DATE
nume_utilizator = 'loredana roman! '   #string (str)= sir de caractele delimitat de ghilimele
print(nume_utilizator)
varstaUtilizator = 32   #integer(int) = numar intreg
print(varstaUtilizator)
inaltime_utilizator = 1.72   #float = numar zecimal
print(inaltime_utilizator)
meniu_vegetarian = False  #boolean(bool) = notiunea de adevarat sau fals
print(0>1) #afiseaza din start False in consola

'''TIPURI DE DATE INTR-O VARIABILA:
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

#STRING FORMAT = cand vrem sa concatenam/adunam un string cu un numar
print(f'Numele este {nume_utilizator} si are varsta de {varstaUtilizator}') # =>Numele este Loredana Roman!  si are varsta de 32
print('Numele este ' + nume_utilizator)#este varianta simpla cand lucram doar cu string-uri =>Numele esteLoredana Roman!
#print('Numele este' + nume_utilizator + 'si are varsta de' + varstaUtilizator) # nu merge pt ca nu poate aduna str+int
        # de aceea este nevoie de formatare =>TypeError: can only concatenate str (not "int") to str
print('Numele este' + nume_utilizator + 'si are varsta de' + str(varstaUtilizator)) #am fortat cu str sa citeasca si varsta ca str nu ca int
# to cast = a face schimbul de date intre int si str, intre str si int, sau bool. Pe scurt am schimbat tipul de date dintr-o variabila

#suprascriere = cand ii dam o alta valoare unei variabile existente
varstaUtilizator = 33
varstaUtilizator = varstaUtilizator + 1
print(varstaUtilizator) #ne afiseaza doar ultima varsta pt ca suprascrie

#METODA/FUNCTIE AJUTATOARE STRING-URI (se leaga cu . de o variabila)
print(nume_utilizator.lower()) #scrie totul cu litera mica

#Un sir de caractere este ca o lista iar fiecare caracter are un index pornit de la 0.
print(nume_utilizator[0].upper() + nume_utilizator[1:].lower()) #[1:] se numeste sliceing pt ca vrem sa afisam doar anumite felii si
            #specificam de unde pana unde sa afiseze lista. daca nu specificam pana unde vrem sa mergem pune [1:] =>Loredana roman!
print(nume_utilizator[0].upper() + nume_utilizator[1:14].lower()) #=>Loredana roman
print(nume_utilizator[::-1]) #parcurgem string-ul invers
print(nume_utilizator[0:14:2]) #parcurge sirul din 2 in 2 - -1 de dinainte este in pas invers

#inlocuim o litera
print(nume_utilizator.replace('r', '')) # am inlocuit R cu nimic =>loedana oman!

print(nume_utilizator.count('o')) # numaram de cate ori apare un substring intr-un string (o-ul in Loredana Roman)

txt = "Hello World"[0:10] # l-am facut sa apara fara ultimul d
print(txt[::-1]) # il parcurgem invers asa cum stim ca merge

nume = 'orice'
print(nume.islower()) # islower - true sau false

#INPUT - METODA PENTRU A LUA DATE DE LA TASTATURA - daca nu specificam altceva, ele vor ramane string
numararul1 = input('alege numarul 1 ') #mesajul dintre paranteze va aparea in consola/terminal
numararul2 = input('alege numarul 2 ')
print(numararul1 + numararul2) #va concatena (aduna) cele 2 numere ca fiind 2 string-uri(=> ex 3+7 = 37) adica
# nu face adunarea numerelor pt ca nu le citeste ca int ci ca string si atunci lipeste cele 2 string-uri
#ca sa facem operatii matematice trebuie sa castam, adica sa schimbam din str in int
print(int(numararul1) + int(numararul2)) #acum le citeste ca int (ex3+7=10)
print(float(numararul1) + float(numararul2)) #ne arata rezultatul cu virgula (ex 3+7=10.0)



