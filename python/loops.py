#defining and assigning the value for list/array
arrylist = ['one','two','three','four','five']

interger = [1,2,3,4,5,6,7,8,9,10]


text = "this text is for demo, is this working text printing"

splitedText = text.split(",")
print(splitedText)

splitedText1 = text.split();
print(splitedText1)
print(len(splitedText1))
print(type(interger))

print("indexing/slicing to access the items")

print(interger[5])

print(interger[-1])
print(interger[2:5])
print(interger[2:])

print(interger[:2])

if 5 == 5:
    print("True")
else:
    print("False")

    
if 5 in interger:
    print("5 is in the list")

"""for text in splitedText:
    print(text)




for item in arrylist:
    print(item)

i = 0
while i < 10:
    print(i)
    i+=1


#example for break

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  """