# import login
#
#
# while login.username != "Roxana" and login.password != "abcd":
#     print("Incorect credentials. Please try again!\n")
#     login.username = input("Enter username: ")
#     login.password = input("Enter password: ")
#     if login.username == "Roxana" and login.password == "abcd":
#         print("Welcome!")


import login

# while login.authorized == 0:
#     print("Please try again")
#     login.username = input("Enter username: ")
#     login.password = input("Enter password: ")
#     if login.authorized == 1:
#         print("You are now authenticated")



if login.authorized == 1:
    print("You are authenticated")
else:
    print("Please try again")
    login.username = input("Enter username: ")
    login.password = input("Enter password: ")
