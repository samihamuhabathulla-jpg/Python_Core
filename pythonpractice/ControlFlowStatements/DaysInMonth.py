month = int(input("Enter month : "))
year = int(input("Enter Year : "))

is_leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
    else:
        is_leap = True

if month == 1:
    print("January", year, "has 31 days")
elif month == 2:
    if is_leap:
        print("February", year, "has 29 days")
    else:
        print("February", year, "has 28 days")
elif month == 3:
    print("March", year, "has 31 days")
elif month == 4:
    print("April", year, "has 30 days")
elif month == 5:
    print("May", year, "has 31 days")
elif month == 6:
    print("June", year, "has 30 days")
elif month == 7:
    print("July", year, "has 31 days")
elif month == 8:
    print("August", year, "has 31 days")
elif month == 9:
    print("September", year, "has 30 days")
elif month == 10:
    print("October", year, "has 31 days")
elif month == 11:
    print("November", year, "has 30 days")
elif month == 12:
    print("December", year, "has 31 days")