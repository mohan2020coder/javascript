#dictionary take key value pair

person = {
    "name":"raj",
    "address":'bangalore',
    'email':"raj@gmail.com"
}

#geting the keys
for p in person:
    print(p)

#getting only values
for p in person.values():
    print(p)

#getting both key and value
for p,v in person.items():
    print(f"  {p}  {v} ")

#get the keys
for p in person.keys():
    print(p)

# it will pop the last item
print(person.popitem())
print(person.pop("name"))

print(person)

person.update({"name":"varun","email":"varun@gmail.com"})

print(person)

del person['email']
print(person)
print(len(person))
print(type(person))
print(person.get("name"))


person.clear()
print(person)



#nesting dictionarys

child1 = {
    "name":"vikram",
    "profile":"engineer",
    "age":30,
    "place":"bangalore"
}
child2 = {
    "name":"karan",
    "profile":"business man",
    "age":33,
    "place":"mysore"
}
child3 = {
    "name":"kiran",
    "profile":"sys admin",
    "age":30,
    "place":"bangalore"
}

family = {
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(family)

for person,value in family.items():
    print(p)
    for d,i in value.items():
        print(f"   {d}   {i}")