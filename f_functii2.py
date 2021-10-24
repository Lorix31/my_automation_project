
print('******** math operations ******')
# video 15 oct min 20

from math import sqrt
def mathOperations(num1, num2, operation):
    if operation == '+': # == se comporta ca o comparatie, = este o atribuire
        return num1+num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == 'radical':
        return sqrt(num1) # aici ne folosim de o functie predefinita in Python. prima data este cu rosu dar trebuie importat 'from math import sqrt'
    else:
        return print('other operation to be added')

print (mathOperations(56,8,'+')) # => 64
print (mathOperations(56,8,'-')) #=>48
print (mathOperations(56,8,'*')) #=>448
print (mathOperations(56,8,'radical')) #=>7,48331477
print (mathOperations(144,8,'radical')) #12.0
print (mathOperations(56,8,'/')) #=>other operation to be added') + None
#=> None -La celelate operatiuni a returnat un nr insa aici returneaza un print, si nr e none. functia asteapta o
# valoare pe care sa o afiseze si aici nu avem.
#daca lasam la else doar return 'other operation to be added' nu mai avem None, pt ca afiseaza o valoare text, nu un print...


