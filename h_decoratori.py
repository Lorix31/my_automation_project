'''Un decorator este o proprietate din Python care ne ajuta pe noi sa schimbam/alteram comportamentul unei metode/functii.
Decoratorii sunt ca niste functii care au in interiorul lor alte functii. - nested functions
'''

'''
o functie care este definita in interiorul unei clase se numeste METODA, iar o functie care se defineste in interiorul altei
functii se numeste FUNCTIE.'''

def my_unit_test(func): #funct prin conventie inseamna ca urmeaza sa ii dam ca parametru o alta functie
    def wrapper(a): # aici am definit o alta functie numita wrapper. se numeste functie si nu metoda pt ca nu este in interiorul unei clase
        print(f"My unit test started with input value {a}")
        func(a) #apelare functie
        print("Unit test finished")

    return wrapper # rezultatul functiei my_unit_test este un wrapper???? return este o proprietate prin care noi scoatem informatii
                # din interiorul functiei in exterior.

@my_unit_test # decorator
def test_1(input_value):
    assert sum([1, 12], input_value) == 15

@my_unit_test # decorator
def test_2(input_value):
    assert input_value in [1,2,3,4,5,6]


# test_1(2)
# test_2(8)
x = my_unit_test(test_1)
x(2)

#=>Codul de mai sus printeaza urmatoarele mesaje:
'''My unit test started with input value 2
My unit test started with input value 2
Unit test finished
Unit test finished

De ce afiseaza de doua ori? Pentru ca o data se afiseaza din functia my_unit_test si a doua oara din functia test_1 
care preia comportamentul functiei my_unit_test (asta apropo de ce va spuneam ca un decorator schimba comportamentul unei metode)

'''