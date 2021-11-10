'''ENCAPSULARE - video 29 oct'''
'''pt definirea claselor scriem keyword-ul class si  pt numele clasei sa inceapa cu litera mare si folosim structura
CamelCase (ex: BaseTest) si nu snake_case
constructor este un bloc de cod care este folosit pt a putea sa creem un obiect care instantiaza clasa repectiva. se trece in corpul clasei.'''

from abc import ABC
class BaseTestModel(ABC): #ABC prescurtare de la abstract base class, anuntam sistemul ca urmeaza sa creem o clasa abstracta
   def test_def(self):
       raise NotImplemented
   def test_exe(self): # metoda de executare a unui test case
       raise NotImplemented


class BaseTest:
    def __init__(self, name, nr_steps): #constructor
        self._name = name  # definim parametrii constructorului, adica valorile pe care le vom folosi atunci cand vom defini un obiect
                           #prin conventie in interiorul constructorului scrie _name ca sa nu confundam cu name-ul pe care il dam intre ().
        self._nr_steps = nr_steps
    def test_rep(self):
        print('Generate a report')

test_case = BaseTest('TestCase1', 3) # test_case este obiectul instantiat iar BaseTest este numele clasei care apeleaza
# constructorul cu argumentele TestCase1 pt numele test case-ului(name) si 3 pt nr_steps
# o metoda se va putea apela prin intermediul unui obiect
#pt a putea sa accesam metoda def_rep o sa scriem numele obiectului
test_case.test_rep() #=>Generate a report

# # RECAPITULARE PT ABSTRACTIZARE
from abc import ABC, abstractmethod
class BaseTestModel(ABC):
    @abstractmethod
    def test_def(self):
       raise NotImplemented

    @abstractmethod
    def test_exe(self): # metoda de executare a unui test case
       raise NotImplemented


class BaseTest(BaseTestModel):
    def __init__(self, name, nr_steps): #constructor
        self._name = name
        self._nr_steps = nr_steps
    def test_rep(self):
        print('Generate a report')
    def test_def(self):
        print('I am currently starting the test case')
    def test_exe(self):
        print(f'Running {self._nr_steps} steps from Test Case {self._name}')

#Apelam metodele
test_case = BaseTest('TestCase1', 3) #instantiere obiect
test_case.test_rep() #=>Generate a report
test_case.test_def() #=>I am currently starting the test case
test_case.test_exe() #=>Running 3 steps from Test Case TestCase1


'''
Un constructor este ca un fel de lucrator/zidar, care construieste obiectul. 
de ex test_case = BaseTest('TestCase1', 3) noi declaram o noua variabila careia sa ii dam niste valori. obiectul va fi construit 
pe baza constructorului, dar si constructorul are nevoie de materiale/valori. Valorile pe care noi le-am pasat constructorului sunt 
TestCase1', 3. A trebuit sa ii dam 2 argumente pt ca in momentul in care am definit constructorul i-am spus ca avem nevoie de 2 argumente
(aici: 
    def __init__(self, name, nr_steps): #constructor
        self._name = name
        self._nr_steps = nr_steps
)

Cand am instantial obiectul test_case = BaseTest('TestCase1', 3)
TestCase1 = este argumentul pe care l-am dat parametrului de la linia 231 adica _name (de la definirea constructorului)


'''

# DACA SCHIMBAM CEVA IN EXERCITIU(linia286 cu print(f'Running {self._nr_steps} steps from Test Case {_name}')
from abc import ABC, abstractmethod
class BaseTestModel(ABC):
    @abstractmethod
    def test_def(self):
       raise NotImplemented

    @abstractmethod
    def test_exe(self): # metoda de executare a unui test case
       raise NotImplemented


class BaseTest(BaseTestModel):
    def __init__(self, name, nr_steps): #constructor
        self._name = name
        self._nr_steps = nr_steps
    def test_rep(self):
        print('Generate a report')
    def test_def(self):
        print('I am currently starting the test case') #atunci cand suprascriem o metoda inseamna ca ii face override (suprascriem o metoda) ?????????
    def test_exe(self, _name):
        print(f'Running {self._nr_steps} steps from Test Case {_name}')
    def tear_down(self):
        print('Quit driver connectivity') # CE AM FACUT CU ASTA...?

#Apelam metodele
test_case = BaseTest('TestCase1', 3) #instantiere obiect
test_case.test_exe('TestCase 2') #=>Running 3 steps from Test Case TestCase2
test_case.test_exe('TestCase 3') #=>Running 3 steps from Test Case TestCase3

# aici am schimbat la def test_exe si am pus si parametru _name intre ().
# La print am folosit formatarea.
# La rularea codului avem '' =>Running 3 steps from Test Case TestCase2 '' self._nr_steps ne citeste datele din constructor.
#stie sa citeasca din constructor in cauza ca am pus self in fata.
# rezultatul este 3 pt ca atunci cand am apelat metoda am pus 3 test_case = BaseTest('TestCase1', 3)
# Mai departe in print name nu il mai citeste din constructor pt ca nu are self in fata si il citeste din apelare
# test_case.test_exe('TestCase 2')

'''ENCAPSULARE - video 29 oct min 57 - pana acum cred ca nu vorbiem de incapsulare si tot de abstractizare....'''
from abc import ABC, abstractmethod
class BaseTestModel(ABC):
    @abstractmethod
    def test_def(self):
       raise NotImplemented

    @abstractmethod
    def test_exe(self): # metoda de executare a unui test case
       raise NotImplemented


class BaseTest(BaseTestModel):
    def __init__(self, name, nr_steps): #constructor
        self._name = name
        self._nr_steps = nr_steps
    def test_rep(self):
        print('Generate a report')
    def test_def(self):
        print('I am currently starting the test case') #atunci cand suprascriem o metoda inseamna ca ii face override (suprascriem o metoda) ?????????
    def test_exe(self, _name):
        print(f'Running {self._nr_steps} steps from Test Case {_name}')
    def tear_down(self):
        print('Quit driver connectivity') # CE AM FACUT CU ASTA...?
    def internal_logger(self):
        print('Public methods ') # O metoda publica este o metoda ce poate fi apelata de oriunde
    def _internal_logger(self):
        print('Protected method ') # O metoda protected este o metoda ce poate sa fie apelata din aceiasi clasa sau din
                                    # aceiasi clasa dar din acelasi pachet???????(se trece cu _)
    def __internal_logger(self):
        print('Private method') # O metoda privata este o metoda ce poate sa fie apelata doar din aceiasi clasa (se trece cu __)
# in viitor metoda privata se va scoate pt ca este trecuta __ pt ca se folosesc de obicei metodele speciale de sistem
    def internal_logger_public(self):
        self.__internal_logger() # ????? aici am apelat metoda internal_logger_public????


test_case = BaseTest('TC1', 4 ) #instantiere obiect
test_case.internal_logger() #=>Public methods
test_case._internal_logger() #=>Protected method
# test_case.__internal_logger() #=> ne da eroare, nu putem sa apelam o metoda privata in afara clasei astfel ca am scris mai sus self.__internal_logger()
test_case.internal_logger_public() #=> Private method. Apelam o metoda privata printr-o metoda publica


'''
MAI DEPARTE AM CREAT 2 PACHETE: h_exemplu_protected si h_exemplu_protected_sursa.

Un pachet este o colectie de programele pe care vreau fie sa le grupez ca au acelasi obiectiv fie ca vreau sa 
restrictionez anumite informatii.
Un pachet poate sa reprezinte o grupare de programe de pycharm.

In interiorul fiecarui pachet creat avem deja niste fisiere __init__py.
Acel fisier face ca acel folder sa fie un pachet (folderul are si un punct)
__init__py este un fisier care ramane gol.

In interiorul pachetului h_exemplu_protected_sursa creem un fisier new python file numit h_sursa_functie_protected.
la fel si ptntru h_exemplu_protected creem un fisier new python file numit h_import_functie_protected
'''