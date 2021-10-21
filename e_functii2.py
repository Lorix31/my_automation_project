'''Function used to get the max out of three numbers
Another approach for the same problem using nested functions
Define four functions for basic calculator operations'''

# embeded function - functie predefinita
print(max(7, 5, 12))

def max2(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def max3(num1, num2, num3):
    return max2(num1, max2(num2, num3))

print(max2(5, 9))
print(max3(8, 12, 95))
print("-------------------------------------")
print("** nested functions **")

a = 5   #functie globala
def max3v2(num1, num2, num3):
    a = 3
    def max2v2(nr1, nr2):        # functie locala
        if nr1 > nr2:
            return nr1
        else:
            return nr2
    print(a)
    return max2v2(num1, max2v2(num2, num3))

print(max3v2(9, 7, 31))
print(a)

print('____________________________________________')
print('******** math operations ******')
from math import sqrt
def mathOperations(num1, num2, operation):
    if operation == '+':
        return num1+num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == 'radical':
        return sqrt(num1)
    else:
        return print('other operation to be added')

print (mathOperations(56,8,'+')) # => 64
print (mathOperations(56,8,'-')) #=>48
print (mathOperations(56,8,'*')) #=>448
print (mathOperations(56,8,'radical')) #=>7,48331477
print (mathOperations(144,8,'radical')) #12.0
print (mathOperations(56,8,'/')) #=>other operation to be added') None - de completat explicatia din video



