from EXTRA.OOP.g_clase_angajat import Angajat

angajat1 = Angajat('Loredana', 3000, 32, 9) #=>Te angajam la 8 ore
angajat2 = Angajat('Gigi', 0, 7, 0) #=>Nu te putem angaja
angajat3 = Angajat('Maria', 500, 15, 1) #=>Te angajam la 4 ore

angajat1.descriere_salariat()
'''=>
Nume salariat: Loredana
Salariu angajat: 3000
Varsta salariat: 32
Vechime salariat: 9
Salariu anual: 36300
Numar ore lucrate: 8
'''

angajat1.marire_salariu(10)
angajat1.descriere_salariat()
'''=>
Nume salariat: Loredana
Salariu angajat: 3630.0
Varsta salariat: 32
Vechime salariat: 9
Salariu anual: 43860.0
Numar ore lucrate: 8
'''

angajat3.descriere_salariat()
angajat3.marire_salariu(5)
angajat3.vechime = 7
angajat3.descriere_salariat()
'''=>
Nume salariat: Maria
Salariu angajat: 500
Varsta salariat: 15
Vechime salariat: 1
Salariu anual: 6100
Numar ore lucrate: 4

Nume salariat: Maria
Salariu angajat: 630.0
Varsta salariat: 15
Vechime salariat: 1
Salariu anual: 7660.0
Numar ore lucrate: 4
'''