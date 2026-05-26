oldSalary = float(input("Enter the salary : "))
rating = float(input("Enter the rating : "))
def salaryHike(salary,hike):
    ans = salary + (salary*(hike/100))
    return ans
if rating>=1 and rating<=4:
    newSalary = salaryHike(oldSalary,10)
    print("Salary after hike is ",newSalary)
elif rating>4 and rating<=7:
    newSalary = salaryHike(oldSalary,25)
    print("Salary after hike is ",newSalary)
elif rating>7 and rating<=10:
    newSalary = salaryHike(oldSalary,30)
    print("Salary after hike is ",newSalary)
else:
    print("Invalid input")