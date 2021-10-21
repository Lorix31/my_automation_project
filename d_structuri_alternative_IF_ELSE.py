#STRUCTURI ALTERNATIVE IF- ELSE

# exercitiu
'''
Daca un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
Daca acel senior vrea sa calatoreasca in iarna,atunci cand cererea este mai mica, atunci i se va oferi o reducere aditionala de 10%
Daca seniorul alege sa calatoreasca la clasa intai, atunci va trebui sa plateasca o taxa suplimentara de lux 3%
Altfel seniorul va plati o taxa de gestiune a calatoriei de 1%.
Daca clientul nu are peste 65 de ani, atunci va plati doar taxa de lux in cazul in care alege sa calatoreasca
la clasa 1 sau taxa de gestiune in caz contrar.
Se aplica de asemenea reducerea sezoniera.
De asemenea vor avea o reducere de 10% in cazul in care au cel putin un copil.
'''

''' pseudocod = exprimare logica a codului astfel incat logica respectiva sa fie valabile, implementabile in orice limbaj de programare:
- INPUT = VARIABILA CARE SE VA EVALUA INTR-UN FLOW DECIZIONAL
- in cazul nostru : INPUT = Varsta, Sezon, Clasa, NrCopii

IF varsta > 65  
THEN reducere = 0.15
ELSE NrCopii >= 1 
THEN reducere = 0.10
ENDIF

IF Sezon == "Iarna" 
THEN reducere = reducere  + 0.10
ENDIF

IF Clasa == 1 
THEN taxa = 0.03
ELSE taxa = 0.01
ENDIF
pret = pret - pret * reducere + taxa '''

'''
Elementele componente ale unei scheme:
- Inputul se reprezinta intotdeauna intr-un paralelogram
- Decizia se reprezinta intotdeauna intr-un romb
- Instructiunile (statementurile) se reprezinta intotdeauna intr-un dreptunghi
- Oricare doua elemente sunt legate intre ele prin linii'''

# Exercitiu cu iepurasii: IL IAU CU COPY PASTE CAND POT SA DESCHID POWERPOINT-UL.....
no_male = int(input('Insert number of male rabbits '))
no_female = int(input('Insert number of female rabbits '))

if no_male > 0 and no_female > 0:
    breed = input('Do you want to breed? ')
    if breed == 'No':
        print('Keep female and male rabbits appart')

