"""

Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType




Python divides the operators in the following groups:

Arithmetic operators 
Assignment operators 
Comparison operators
Logical operators


https://www.w3schools.com/python/python_operators.asp
"""


text = "this text is for demo, is this working text printing"


print(text.capitalize())

print("text word is repeated for : ",text.count("s"),"times")


print("s is repeated for( based on position) : ",text.count("s",5,15),"times")

print("string ends with( printing or not): ",text.endswith("printing"))

print("searching for demo: ",text.find('demo'))

print("hello is alpha character: ","hello".isalpha())

print("Converting LOWER case".lower())
print("Coverting upper case".upper())

print(text.replace("working","playing"))
print(text)



