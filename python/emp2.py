
print("IIHT PVT LTD")

print("********")

print("welcome to the testing depatment")


employe_name = ["Rajesh", "suresh", "ramesh", "abc", "xyz"]

print(employe_name)

salary = input("enter the salary name wise\n").split()

for n in range(0, len(salary)):
    
    salary[n] = int(salary[n])
    
print("each employe salary", salary)

total_salary = 0

for to_salary in salary:
    
    total_salary += to_salary
    
print("average of salary", total_salary)

print("total cost of Company", total_salary)
    
min_salary = 0

print("Max salary ", max(salary))

print("min salary", min(salary))