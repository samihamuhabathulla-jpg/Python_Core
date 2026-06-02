class NoMatchException(Exception):
    pass
try:
    aadhar=input("Enter Aadhar Number: ")
    name=input("Enter Name: ")
    city=input("Enter City: ")
    state=input("Enter State: ")
    country=input("Enter Country: ")

    if country!="India":
        raise NoMatchException
    print("Citizen Details:")
    print("Aadhar Number:", aadhar)
    print("Name:", name)
    print("City:", city)
    print("State:", state)
    print("Country:", country)

except NoMatchException:
    print("Country name does not match 'India'")