'''
- Functions to find the maximum out of 3 input numbers - vezi fisierul functii 2 functia max3
- Functions to find the maximum out of 3 input numbers with nested functions
- Definirea  a 4 functii care efectueaza operatii de baza
- O functie definita in interiorul unei clase se numeste metoda
- OOP = Object Oriented Programming / POO = Programare Orientata pe Obiecte
'''


# from d_functii2 import mathOperations
from e_functii2 import mathOperations


class Calculator:
    def __init__(self, num1,num2,num3):
        self._num1 = num1
        self._num2 = num2
        self._num3 = num3

    def _max2(self, num1, num2):
        if num1 > num2:
            return num1
        else:
            return num2

    def max3(self, num1, num2, num3):
        return self._max2(num1, self._max2(num2, num3))

    def test_max3(self):
        return self.max3(45,8,69)

    def max3v2(self):
        def max2v2(nr1, nr2):  #nested functions (funcii impricate)
            if nr1 > nr2:
                return nr1
            else:
                return nr2
        return self._max2(self._num1, max2v2(self._num2, self._num3))

    def math_operation(self,a,b,operation):
        return mathOperations(a,b,operation)

''' instructiuni care se pot executa cu constructor implicit '''
# calculator = Calculator() # aici obiectul a fost creat cu ajutorul unui consftructor implicit
# print(calculator) #=><__main__.Calculator object at 0x000001BE4E7F9FD0>
# print(calculator.test_max3()) #=> 69
# print(calculator.max3(20, 56, 28)) #=>56
# print(calculator._max2(256, 325)) #=>325
# print(calculator.math_operation(20,60,'+')) #=>80

''' instructiuni care se pot executa cu constructor explicit'''
calculator = Calculator(5, 9, 20)
print(calculator.max3v2())

