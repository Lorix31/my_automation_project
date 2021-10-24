#adunam 3 numere date de la tastatura

def addition(num1, num2, num3=0, data_type = 'str'):
    if data_type == 'str':
        return str(num1) + str(num2) + str(num3)

    return int(num1) +int (num2) +int(num3)


a = (input('Introduceti primul numar: '))
b = (input('Introduceti cel de al 2lea nr: '))
c = (input('introduceti cel de al 3lea nr: '))

print(addition(a, b, c, 'int'))
# print(addition(a, b, c))
print(type(a))
