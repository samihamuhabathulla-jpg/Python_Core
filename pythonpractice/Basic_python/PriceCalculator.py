income = int(input("Enter your monthly income : "))
inputOfSpendings = (input("Enter the spendings : "))
spendSplit = inputOfSpendings.split()
spendings = 0
for i in spendSplit:
    spendings+=float(i)
savings = income - spendings
print("Remaining Budget : ",savings)