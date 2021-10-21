''' O functie se defineste cu def
Functia nu se executa decat daca o apelam.Apelarea functiei se face prin specificarea numelui functiei urmata de
parametrul utilizat pus intre paranteze
La definire o functie are intre paranteza argumente, iar la apelare, acele argumente se numesc parametri'''

def sayHello(name):  # name = argument
    # print("Buna " + name)
    print(f"Buna {name}")

def sayHello2(name, email):
    return f"Bine ai venit {name}\n" + f"Adresa ta de mail este {email}"

def sayHello3(name, email, password = "abc123"):
    return f"Bine ai venit {name}\n" + f"Adresa ta de mail este {email}\n" + f"Si parola ta este {password}"

def sayHello4(*nume):        # * - identificare parametru dupa index
    print("Hello", nume[1])

def sayHello5(**test):       # ** - identificare parametru dupa key
    print("Your name is", test["name"])
    print("Your salary is", test["salary"])
    print("Your email is", test["email"])

# apelare functie
# sayHello("Gigel")  # Gigel = parametru
# nume = "George"
# sayHello(nume)
#
# x = sayHello("Ionel")
# print(x)

# y = sayHello2("Maria", "maria@yahoo.com")
# print(y)
# print(sayHello2("Maria", "maria@yahoo.com"))

# print(sayHello3("Vasile", "vasile@yahpp.com"))
# print(sayHello3("Vasile", "vasile@yahpp.com", "abcdef"))
# print(sayHello3(email = "Vasile", name = "vasile@yahpp.com", password = "abcdef")) #nu este recomandat

# sayHello4("Vasile", "Marius", "Bogdan")

sayHello5(name = "John Snow", salary = 2000, email = "johnsnow@yahoo.com")
