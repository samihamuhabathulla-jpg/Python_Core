total_price = 0
while True:
    price = int(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item: "))
    total_price = total_price + (price * quantity)
    choice = input("Do you want to enter another item? (yes/no): ").lower()
    if choice == "no":
        break

print("Total Price:", total_price)