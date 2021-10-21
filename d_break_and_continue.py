''' sunt utile in structurile repetitive'''

for x in range(10):
    if x == 7:
        break
    print(f'The number is {x}') # sau se poate scrie si asa  print('the number is ', x) dar nu e de preferat

''' =>
the number is 0
the number is 1
the number is 2
the number is 3
the number is 4
the number is 5
the number is 6
nu merge mai departe de 7'''

print('--------------')

for x in range(10):
    if x == 7:
        continue
    print(f'The number is {x}')

''' =>
the number is 0
the number is 1
the number is 2
the number is 3
the number is 4
the number is 5
the number is 6
the number is 8
the number is 9
a printat tot mai putin 7, cu continue i-am spus sistemului sa sara peste 7, cand ajunge la 7 sa nu execute instructiunile
si sa mearga mai departe'''

'''
x = 0 => 0 == 7 se executa print(f'The number is {x}')
x = 1 => 1 == 7 se executa print(f'The number is {x}')
x = 2 => 2 == 7 se executa print(f'The number is {x}')
x = 3 => 3 == 7 se executa print(f'The number is {x}')
x = 4 => 4 == 7 se executa print(f'The number is {x}')
x = 5 => 5 == 7 se executa print(f'The number is {x}')
x = 6 => 6 == 7 se executa print(f'The number is {x}')
x = 7 => 7 == 7 se executa nu se executa print-ul
x = 8 => 8 == 7 se executa print(f'The number is {x}')
x = 9 => 8 == 7 se executa print(f'The number is {x}')'''