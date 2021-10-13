# greet = 'hello world'
# print(len(greet))
# print (greet[0:len(greet)])
# quote = 'to be or not to be'
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace('be', 'me'))
# name = 'lore'
# print(type(name))
# name= 1
# print(type(name))
#
# name= '1'
# print(type(name))
#
#
# # IMMUTABILITY
# selfish= 1
# print(selfish)
#
# selfish= '1212'
# print(selfish)
#
# selfish= 'test'
# print(selfish)
#
# selfish[0] = '1212'
# print(selfish)
#
# selfish=[1,45,'test','andreea']
# print(selfish)
#
# selfish='me me me'
# print(selfish[0])
# print(selfish[1:])
# print(selfish[1:5])
# print(selfish[0:len(selfish):2])
#
# selfish='ab cd ef'
# print(selfish[:5])
# print(selfish[::1])
#
# selfish='ab cd ef'
# print(selfish[::2])
#
# selfish='ab cd ef'
# print(selfish[-1])
#
# selfish='ab cd ef'
# print(selfish[-2])
#
# selfish='ab cd ef'
# print(selfish[::-1])
#
# selfish='ab cd ef'
# print(selfish[::-2])
#
test = 'Andrada'
       #0123456
test = 'Andrada P' # se suprascrie
#test[6] = 'i' # [6] nu va merge =>TypeError: 'str' object does not support item assignment pt ca nu utem schimba doar o parte din variabila ci trebuie sa reinlocuim toata variabila cu cea dorita
test = 'Andrada I' #adica o definim din nou si o suprascriem