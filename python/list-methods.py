"""
list methods

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

fruits = ['apple', 'banana', 'cherry']
print(type(fruits))

#appends the item to last position of the list
fruits.append("orange")

print(fruits)
for i in range(1,10):
    print(i)
    for j in range(5,10):
        print(j)


for fruit in fruits:
    if fruit == 'orange':
        print('Successfully added in above append() method')
    print(fruit)

#copys the data of the fruits list into x
x = fruits.copy()

print(x)
print(type(x))


cars = ['Ford', 'BMW', 'Volvo','cherry']


# adding list to the exiting list
fruits.extend(cars)
print(fruits)

countFruits = fruits.count('cherry')
print(countFruits)

index = fruits.index("apple")
print(index)

fruits.insert(1, "grape")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.reverse()
print(fruits)

cars.sort()
print(cars)
#fruits.clear()