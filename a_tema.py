''' tema 1 da, tema 2 nu'''


# De ce nu am aici venv si main.py? - am creat eu manual new-new python file si am copiat codul

#TEMA 1: Comparatia pentru password si sold de la tastatura prin consola adica definiti o noua variabila sold si
# adaugati doua inputuri noi pentru sold si parola, pe care sa le comparati cu valorea variabilelor definite de voi.
#Hint: variabila sold ar trebui sa faca referire la un numar de articole vandute sau este o variabila booleana?
# = Înseamnă sold ul pe care îl aveți pe cont. Noi încercăm sa simulam informatiile dintr jn cont bancar.
# Și sa zicem că verificam ca userul știe ce are pe cont ca o metoda de verificare

#REZOLVARE:
expectedPass = 'a12345'
expectedSold = 500
pasword = input('enter pasword')
sold = input('enter sold')
assert pasword==expectedPass
assert sold==expectedSold


#TEMA 2:Sa scrieti un set de cazuri de testare pentru o functionalitate de login -> Scrieti doua test case-uri complete,
# iar pentru celalalte functionalitati definiti doar conditiile de testare

#REZOLVARE
'''
TEST CONDITION 1: verifica faptul ca utilizatorul s epoate loga cand user si aprola sunt corecte
TEST CASE 1:
Summary:
Preconditii:
Pasi de reproducere:
Rezultatele asteptate:

TEST CONDITION 2: verifica faptul ca utilizatorul nus e poate loga daca nu itnroduce parola sau userul
TEST CASE 2:
Summary:
Preconditii:
Pasi de reproducere:
Rezultatele asteptate:'''
