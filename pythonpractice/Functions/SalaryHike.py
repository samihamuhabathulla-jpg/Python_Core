oldSalary = float(input("Enter the salary : "))
hike = float(input("Enter the hike in percentage : "))
def salaryHike(salary,hike):
    ans = salary + (salary*(hike/100))
    return ans
newSalary = salaryHike(oldSalary,hike)
print("Salary after hike is ",newSalary)