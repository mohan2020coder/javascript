print("---------------------------------")
print('Welcome to Techjini')
print("___________________________________")
print("This program will display the salary details\n of the department")

employees = ['Rajesh','Ramesh','Suresh']
department = input("Enter the department name:")
salarys_list = []

for employee in employees:
    salarys_list.append(int(input(f"Enter salary of {employee} :")))

print(salarys_list)

highest_salary = 0
for salary in salarys_list:
    if salary > highest_salary:
        highest_salary = salary

lowest_salary = highest_salary
for salary in salarys_list:
    if salary < lowest_salary:
        lowest_salary = salary

sum_salary =0
for salary in salarys_list:
    sum_salary += salary


print(f"The highest salary   is: {highest_salary}")
print(f"The lowest salary   is: {lowest_salary}")
print(f"The total cost to the company of {department}  is: {sum_salary}")
print(f"The average salary is: {sum_salary/len(salarys_list)}")
