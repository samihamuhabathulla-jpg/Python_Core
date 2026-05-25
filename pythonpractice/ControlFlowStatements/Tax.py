income = int(input())
if income <= 250000:
    print("You are exempted from tax")
else:
    tax = 0
    
    if income > 1200000:
        tax = tax + (income - 1200000) * 0.30
        tax = tax + (1200000 - 500000) * 0.20
        tax = tax + (500000 - 250000) * 0.10
    elif income > 500000:
        tax = tax + (income - 500000) * 0.20
        tax = tax + (500000 - 250000) * 0.10
    else:
        tax = tax + (income - 250000) * 0.10
    print(int(tax))