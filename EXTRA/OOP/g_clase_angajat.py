class Angajat:
    def __init__(self, nume_angajat, salariu, varsta, vechime):
        self.nume_clasa = nume_angajat
        self.salariu = salariu
        self.varsta = varsta
        self.vechime = vechime
        if varsta <= 0:
            print('Varsta invalida')
        elif varsta < 14:
            print('Nu te putem angaja')
        elif varsta >= 14 and varsta < 18:
            print('Te angajam la 4 ore')
            self.nr_ore = 4
        else:
            print('Te angajam la 8 ore')
            self.nr_ore = 8

    def bonus_craciun(self):
        if self.vechime <= 3:
            self.salariu = self.salariu + 100
        elif self.vechime >3 and self.vechime >=5:
            self.salariu = self.salariu + 300
        else:
            self.salariu = self.salariu + 500
        return self.salariu #cand avem nevoie de acest raspuns pt altceva /de ex sa o folosim in alta functie

    def salariu_anual(self):
        salariu_anual = (self.salariu * 11) + self.bonus_craciun()
        return salariu_anual

    def marire_salariu(self, valoare_procentuala):
        self.salariu = self.salariu + (self.salariu* valoare_procentuala/100)

    def descriere_salariat(self):
        print(f'Nume salariat: {self.nume_clasa}')
        print(f'Salariu angajat: {self.salariu}')
        print(f'Varsta salariat: {self.varsta}')
        print(f'Vechime salariat: {self.vechime}')
        print(f'Salariu anual: {self.salariu_anual()}')
        print(f'Numar ore lucrate: {self.nr_ore}')




