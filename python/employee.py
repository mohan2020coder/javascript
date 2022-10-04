print("Employee manangement")

emp_name = input("Enter the employee name:")
emp_address = input("Enter the address: ")
emp_email = input("Enter the email id: ")

print("Employee you have entered:")
print("Name : ",emp_name)
print("Address: ",emp_address)
print("Email Id: ",emp_email)

if emp_name == 'admin':
    print("Welcome to admin page")
else:
    print("Welcome to guest page")
    
if emp_name == "secret":
        print("Welcome to secret page")
        print("your secret code is : A 12321 ")


if emp_name == 'admin':
    print("Welcome to admin page")
elif emp_name == 'secret':
    print("Welcome to secret page")
    print("your secret code is : A 12321 ")
else:
     print("Welcome to guest page")





