valid_user = ['raju', 'ramesh','mahesh']

name = input("enter the name: ")
password = input('enter the password')


if name in valid_user:
    print("Thank you for visiting the web page again")
else:
    print("Thank you user,  your data will be saved")
    valid_user.append(name)


print(valid_user)