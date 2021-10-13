#import b_b_basic_operators
import b_tema

if b_tema.authorized == 1:
    print("You are authenticated")
else:
    print("Please try again")
    b_tema.username = input("Enter username: ")
    b_tema.password = input("Enter password: ")