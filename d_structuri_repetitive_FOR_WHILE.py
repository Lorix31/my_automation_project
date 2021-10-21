# '''STRUCTURI REPETITIVE  FOR SI WHILE'''
#
#
# '''FOR = poti sa executi un set de instructiuni pana nu se mai indeplineste o anumita conditie
# - este folosit in principiu pt a parcurge o lista'''
#
my_list = [2,3,4,5,43]
n = 0
for i in my_list:
    n = n + i
    # i = 2 => n = 0+2
    # i = 3 => n = 2+3
    # i = 4 => n = 5+4
    # i = 5 => n = 9+5
    # i = 43 => n = 14+43
    print(n) #=> 57 adica 14+43

else:
    print('We are done with the sum')


'''WHILE - executa un set de instructiuni pe baza unei conditii'''
my_list = [1,2,3,4,5,43]
n=0
position = 0
while position<len(my_list):
    n = n + my_list[position]
    position = position + 1 # sau putem scrie si position+=1
print(n) #=>58

'''position = 0 => position<6  n = 0+1
position = 1 => position<6  n = 1+2
position = 2 => position<6  n = 3+3
position = 3 => position<6  n = 6+4
position = 4 => position<6  n = 10+5
position = 5 => position<6  n = 15+43
position = 6 => position<6  NU, se iese din bucla'''



'''WHILE LOOP'''
'''my_list = [1,2,3,4,5,43]
n=0
position = 0
while position<len(my_list):
    n=n+my_list[position]
    print(n)'''

