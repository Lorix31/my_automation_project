#1. metoda care sa returneze aria cercului
def aria_cercului(raza):
    aria = 3.14 * (raza*raza)
    return aria
print(aria_cercului(2)) #=> 12.56
print(aria_cercului(10)) #=>314.0


#2. metoda care sa afiseze cel mai mic din 3 numere
def cel_mai_mic_numar(nr1, nr2, nr3):
    if nr1 <= nr2 and nr1 <= nr3:
        numarulMic = nr1
    elif nr2 <= nr1 and nr2 <= nr3:
        numarulMic = nr2
    else:
        numarulMic = nr3
    return "Cel mai mic numar este", numarulMic

print(cel_mai_mic_numar(1,2,3)) # daca nr1<nr2 si nr1<nr3 =>1
print(cel_mai_mic_numar(1,1,3)) # daca nr1=nr2 si nr1<nr3 =>1
print(cel_mai_mic_numar(1,2,1)) # daca nr1<nr2 si nr1=nr3 =>1
print(cel_mai_mic_numar(5,4,7)) # daca nr2<nr1 si nr2<nr3 =>4
print(cel_mai_mic_numar(4,4,7)) # daca nr2=nr1 si nr2<nr3 =>4
print(cel_mai_mic_numar(5,4,4)) # daca nr2<nr1 si nr2=nr3 =>4
print(cel_mai_mic_numar(53,42,7)) # else =>7

# Aici asa ma gandisem si eu cu if, primul if si le scrisesem bine insa ma incurcasem cu return si am cautat pe net


#3. metoda care sa mareasca si sa returneze salariul marit.
# ca si parametru dau salariul si procentul, de ex 2000 si 5, rezultat 2100. deci am facut o marire de 5% si am aflat rezultatul
def salariu(s):
    salariuMarit = s + (s * 0.05)
    return 'Salariul recalculat dupa marire este ', salariuMarit

print(salariu(2000)) #=>('Salariul recalculat dupa marire este ', 2100.0)
#Nu imi dau seama de ce mie imi pune toate rezultatele in consola in ()??