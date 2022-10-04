#this program is example show how to get inputs 
#from the user and print it

# variables
"""

A variable can have a short name (like x and y)
 or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or
 the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric
 characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age
 and AGE are three different variables)

 myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Camel Case
Each word, except the first, starts with a capital letter:

myVariableName = "John"


Pascal Case
Each word starts with a capital letter:

MyVariableName = "John"


Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"
"""

x = 5 # it is integer
y = "hello world" # string value
a = 7.5 # float value
b = False  #boolean
c = False


a_input = input("enter the first integer: ")

print(a_input)
#type casting 

x = str(3)
y = int(3)
z = float(3)



print(type(x))
print(type(y))
print(type(z))

#comments
# indentation 

#conditions

if b:
    print("this is boolean True\n")
elif c == False:
    print('this is False block\n')