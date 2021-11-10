''' O functie se defineste cu def
Functia nu se executa decat daca o apelam.Apelarea functiei se face prin specificarea numelui functiei urmata de
parametrul utilizat pus intre paranteze
La definire o functie are intre paranteza argumente, iar la apelare, acele argumente se numesc parametri'''

# EXEMPLU 1
def sayHello(name):    # def= ii spunem sistemului ca urmeaza sa apelam o functie /sayHello=numele functiei / name = argument al functiei
        # print("Buna " + name) #=> nu se vede nimic pt ca nu este apelata functia
        print(f'Buna {name}') # face acelasi lucru dar e scrisa sub alta forma
#Apelare functie1
nume = 'Lore'
sayHello('Ana')     # La apelare ('Ana') este parametru => Buna Ana
sayHello(nume)  # => este acelasi lucru insa la argument punem o variabila =>Buna Lore

'''dam rezultatul functiei Hello unei variabile'''
x = sayHello('Ionel') # am apelat functia sayHello cu parametru Ionel =>Buna Ionel
print (x) #=> None pt ca nu avem return......

print('____________________________________________________________________________')

# EXEMPLU 2
def sayHello2(name, email):
        return f'Bine ai venit {name}\n' + f'Adresa ta de mail este {email}' #  \n-escape charater anunta sistemul sa treaca pe randul urmator tot ce este dupa el
#Apelare functie2
y = sayHello2('Maria', 'maria@yahoo.com')
print(y)
print(sayHello2("Ioana", "ioana@yahoo.com"))

'''Diferenta intre print si return
Print este o instructiune care se exceuta imediat pe ecran.
Return este rezultatul unei functiii. Functia trebuie sa aduca inapoi niste rezultate, printul doar printeaza ceva pe consola.
Return nu garanteaza ca printeaza ceva pe consola decat daca ii dau eu rezultatul.
Return il folosim doar daca vrem ca metoda respectiva sa ne intoarca un rezultat iar printul daca vrem sa ne afiseze acel rezultat pe ecran.
'''

print('____________________________________________________________________________')

# EXEMPLU 3
def sayHello3(name, email, password = "abc123"):
    return f"Bine ai venit {name}\n" + f"Adresa ta de mail este {email}\n" + f"Si parola ta este {password}"

#Apelare functie3
print(sayHello3("Vasile", "vasile@yahoo.com")) # chiar daca noi am dat 3 argumente la functie si 2 parametri la apelarea functiei
                                                # o sa functioneze pt ca este definit in fcuntie
                                                #=>Bine ai venit Vasile / Adresa ta de mail este vasile@yahoo.com/Si parola ta este abc123

#sau se mai poate scrie si asa:
m = sayHello3("Grigore", "grigore@yahoo.com")
print(m) #=>Bine ai venit Grigore / Adresa ta de mail este grigore@yahoo.com / Si parola ta este abc123

print(sayHello3("Mirabela", "mira@yahoo.com", "abcdef"))
#=>Bine ai venit Mirabela / Adresa ta de mail este mira@yahoo.com / Si parola ta este abcdef
# aici a schimbat parola din functie cu cea pe care am folosit-o la apelare, are prioritate apelarea

print(sayHello3(name = 'Nerecomandat', email = "nop@yahoo.com", password = "abcdef"))
#=>Bine ai venit Nerecomandat / Adresa ta de mail este nop@yahoo.com / Si parola ta este abcdef
#Am definit valorile cand am apelat functia.

print(sayHello3(email = "nop@yahoo.com", name = 'Nerecomandat', password = "abcdef"))
# putem sa si amestecam parametrii intre ei si tot avem un rez corect insa nu este de recomandat sa facem asa
# =>Bine ai venit Nerecomandat / # Adresa ta de mail este nop@yahoo.com /# Si parola ta este abcdef

print('____________________________________________________________________________')

# EXEMPLU 4
def sayHello4(*nume):        # * - identificare parametru dupa index
    print("Hello", nume[0])

#Apelare functie4
sayHello4("Vasile", "Marius", "Bogdan") # => afiseaza doar primul nume Hello Vasile


print('____________________________________________________________________________')

# EXEMPLU 5
def sayHello5(**test):       # ** - identificare parametru dupa keyword. Notam asa cand nu stim cati parametrii avem la definirea functiei
    print("Your name is", test["name"]) # nu printeaza nimic pana nu apelam functia
    print("Your salary is", test["salary"])
    print("Your email is", test["email"])

# Apelare functie5
sayHello5(name = "John Snow", salary = 2000, email = "johnsnow@yahoo.com")
sayHello5(name = "Deneris", salary = 2500, email = "danny@yahoo.com")
#=> Your name is John Snow / Your salary is 2000 / Your email is johnsnow@yahoo.com
#=> Your name is Deneris / Your salary is 2500 / Your email is danny@yahoo.com - am apelat functia de 2 ori de aceea arata si Joh si Deneries

# se aseamana foarte bine cu dictionarele. Folosim parametru cu ** cand vrem sa identificam un parametru pe baza de keyword

print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')

# PARTEA A 2 A !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''Function used to get the max out of three numbers
Another approach for the same problem using nested functions
Define four functions for basic calculator operations'''

# EXEMPLU 1
# embeded function - functie predefinita
print(max(7, 5, 12)) # max este un cuv predefinit in Python => 12

# EXEMPLU 2
def max2(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

#Apelare functie 2
(max2(50, 100)) # -  nu printeaza nimic, trebuie print ca sa vedem in consola:
print(max2(50, 100)) #=>100

# EXEMPLU 3 - vrem sa aflam max dintre 3 numere cu apelarea unei functii in alta functie
def max3(nr1, nr2, nr3):
    return max2(nr1, max2(nr2, nr3)) # fct max 2 are 2 argumente

#Apelare functie 3
print(max3(85, 25, 36))
# aici amd at ca si parametrii nr 85,25,36. in fct max 3 a comparat cele 3 numere si a rezultat 85 ca fiind cel mai mare.
# in return-ul din functie nr 1 = 85. 85 a fost apoi comparat cu maximul dintre 25 si 36 cu functia max 2 de unde rezulta 36. apoi a comparat 85 cu 36

print(max3(85,25,99)) #> ar trebui sa rezulte 99 => corect


print("------------------------------------------------------------------")
print("** nested functions **")

# EXEMPLU 4
'''NESTED FUNCTIONS = functii care se definesc in interiorul altei functii (functii emricate) '''


def max3v2(num1, num2, num3):
    def max2v2(nr1, nr2):        # functie locala. o variabila care se defineste in interiorul unui alt element (functie, clase, etc)
        if nr1 > nr2:
            return nr1
        else:
            return nr2
    return max2v2(num1, max2v2(num2, num3))

# Apelare functie ex4
print(max3v2(80, 55, 30)) #=> 80
'''La apelare a identificat functia max3v2, aluat parametruu num1=80, num2=55,num3=30.
In interiorul functiei max3v2 este definita o noua functie max2v2 care este apelata la return. La return a luat functia max2v2
si a calculat max dintre num1=80 si max dintre num2=55 si num3=30 a rezultat 55. in final a calculat max dintre 80 si 55 =>80
'''


'''max2v2 o subliniaza cu rosu pt nu o gaseste, functia este cunoscuta doar in interiorul functiei max3v2, cu alte cuvinte este
o functie locala,'''


# EXEMPLU 5 -acelasi exemplu dar scris altfel
'''NESTED FUNCTIONS = functii care se definesc in interiorul altei functii (functii emricate) '''
a=5
def max3v2(num1, num2, num3):
    a=3
    def max2v2(nr1, nr2):        # functie locala
        if nr1 > nr2:
            return nr1
        else:
            return nr2
    print(a) # => 3
    return max2v2(num1, max2v2(num2, num3))

# Apelare functie ex5
print(max3v2(80, 55, 30)) #=> 80
# print(a)  => daca il trecem aici, la fel nu o sa afiseze pt ca variabila 'a' supravietuieste doar in interiorul functiei, unde a fost definita
#dar ca inainte de functie trecem a=2 si la apelare print(a) o sa ne dea rezultat. scopul acestui exemplu este sa vedem ca este important unde dam print-ul

