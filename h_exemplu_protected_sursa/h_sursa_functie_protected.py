class SursaProtected:
    def _internal_logger(self):
        print('Protected method ')

#instantiere obiect (creare obiect)
apelare_functie = SursaProtected()
#apelare functie
apelare_functie._internal_logger() #=>Protected method

