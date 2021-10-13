# '''TEMA1:
# Scrieti un program in care sa verificati daca un numar este par sau impar.'''
#
# #REZOLVARE
# x = input("Enter the first number ")
# y = input("Enter second value ")
# output = int(x) % int(y)
# print(output)
# '''=>
# Enter the first number 20
# Enter second value 5
# 0 nu imi dau seama daca este nr par sau nu....'''
#
# '''TEMA2:
# Scrieti un program prin care sa definiti numele unui student, sa definiti notele pentru studentul respectiv la
# urmatoarele materii: Matematica, Chimie, Fizica, Biologie, Informatica. Faceti media notelor si afisati pe ecran
# urmatorul text: Media studentului "Nume_student" este "Media"
# Nume_student, Media trebuie sa fie definite ca variabile individuale si printate pe ecran cu ajutorul formarii (f)
# Indiciu: Inmultirea si impartirea au prioritate in fata adunarii si scaderii, motiv pentru care adunarile trebuie puse
#  intre paranteze'''
#
# #REZOLVARE
# #metoda 1
# elev = input('numele studentului este')
# matematica = int(input('nota la matematica este ')) #int schimba tipul de date din string in int (to cast)
# chimie = int(input('nota la chimie este '))
# fizica = int(input('nota la fizica este '))
# biologie = int(input('nota la biologie este '))
# informatica = int(input('nota la informatica este '))
# media = (matematica + chimie + fizica + biologie + informatica) / 5
# print(f"media este  {media}" )
#
# elev2 = input('numele studentului este ')
# matematica2 = input('matematica2 ')
# chimie2 = input('chimie2 ')
# fizica2 = input('fizica2 ')
# biologie2 = input('biologie2 ')
# informatica2 = input('informatica2 ')
# media2 = (int(matematica2)+int(chimie2)+int(fizica2)+int(informatica2))/5
# print(f'numele studentului este {elev2} si media este {media2}')
#

#metoda 2 - revin cand fac dict, liste,

'''TEMA 3:
 Scrieti un program care sa fie apelat dintr-un alt program(? - folosim import?). Vrem ca programul initial sa introduca numele utilizatorului si parola 
 de la tastatura, in programul de baza sa se printeze utilizatorul si parola, iar in al doilea program sa se printeze urmatorul 
 mesaj: daca utilizatorul si parola sunt corecte: Bine ati venit, Daca utilizatorul si parola nu sunt corecte: 
 Va rugam sa incerecati din nou

Indiciu: Trebuie folosita functia if cu ramura de else
'''

username = input("Enter username: ")
password = input("Enter password: ")

if username == 'Alina' and password =="abc123":
    authorized = 1
else:
    authorized = 0

if __name__ == "__main__":
    print(username)
    print(password)

#
# #daca un nr este +sau-
# x=-0
# if x==0:
#     print('neutru')
# elif x<0:
#     print('negativ')
# else:
#     print('pozitiv')
# #branch testing = testam cu valori astfel incat sa trecem prin fiecare ramura
# #tc1:x=3, expected result = pozitiv, actual result = pozitiv => pass
# #tc2:x=-5, expected result = negativ, actual result = negativ =>pass
# #tc3:x=0, expected result = neutru, actual result = neutru => pass
#
#
#
# #ex de trimis lui andi cu if, elif x 2,else cu 4 ramuri
# '''exemplu doar cu IF si ELSE: Daca un elev a luat la examen nota > sau = cu 5 sa afiseze mesajul ''A trecut examenul'',
# daca a luat nota <5 sa afiseze mesajul ''a picat examenul''  '''
#
# #REZOLVARE
#
# x=3
# if x==5:
#     print('a trecut examenul')
# elif x>5:
#     print('a trecut examenul')
# else:
#     print('a picat examenul')
# #branch testing = testam cu valori astfel incat sa trecem prin fiecare ramura
# #tc1:x=5, expected result = a trecut examenul, actual result = a trecut examenul=> pass
# #tc2:x>5, expected result = a trecut examenul, actual result = a trecut examenul =>pass
# #tc3:x<5, expected result = a picat examenul, actual result = a picat examenul => pass
#
#
# elev = input('numele elevului este ')
# nota_examen = input('nota la examen este ')
# print(f'numele elevului este {elev} si nota la examen este {nota_examen}')
# if nota_examen=='5':
#       print('A trecut examenul')
# elif nota_examen=='6':
#       print('A trecut examenul')
# elif nota_examen=='7':
#       print('A trecut examenul')
# elif nota_examen=='8':
#       print('A trecut examenul')
# elif nota_examen=='9':
#       print('A trecut examenul')
# elif nota_examen=='10':
#       print('A trecut examenul')
# else:
#       print('A picat examenul')
#
# #SAU
# elev = input('numele elevului este ')
# nota_examen = int(input('nota la examen este '))
# print(f'numele elevului este {elev} si nota la examen este {nota_examen}')
# if nota_examen==5:
#       print('A trecut examenul')
# elif nota_examen>5:
#       print('A trecut examenul')
# else:
#       print('A picat examenul')
#
# #SAU
# elev = input('numele elevului este ')
# nota_examen = int(input('nota la examen este '))
# print(f'numele elevului este {elev} si nota la examen este {nota_examen}')
# if nota_examen>=5:
#       print('A trecut examenul')
#
# else:
#       print('A picat examenul')