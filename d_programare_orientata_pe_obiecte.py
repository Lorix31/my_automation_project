'''Function used to get the max out of three numbers
Another approach for the same problem using nested functions
Define four functions for basic calculator operations'''

'''embeded function = functie predefinita in Python'''
print(max(7,5,12))

def max2(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2
max2(50,100) # = nu printeaza nimic, ca sa printeze tb print
print(max2(50,100))

def max3(nr1,nr2,nr3):
    return max2(nr1,max2(nr2,nr3))
print(max3(85,25,99))
print('--------------------------')

'''nested functions = functii care se definesc in interiorul altor functii (functii imbricate)'''
def max3v2(num1,num2,num3):
    def max2v2(nr1,nr2):
        if nr1>nr2:
            return nr1
        else:
            return nr2
    return max2v2(num1,max2v2(num2,num3))
print(max3v2(31,51,35))

