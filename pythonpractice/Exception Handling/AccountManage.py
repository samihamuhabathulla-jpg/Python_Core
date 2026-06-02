class PayOutOfBoundsException(Exception):
    pass

try:
    balance=80000
    limit=30000
    amount=int(input("Enter withdraw amount: "))
    if amount>limit:
        raise PayOutOfBoundsException
    if amount>balance:
        raise PayOutOfBoundsException
    balance=balance-amount
    print("Withdrawal successful.")
    print("Updated balance:",balance)

except PayOutOfBoundsException:
    print("Error: Transaction amount exceeds insufficient balance.")