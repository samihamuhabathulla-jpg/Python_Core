class NoMatchException(Exception):
    pass
try:
    aadhar = input()
    name = input()
    city = input()
    state = input()
    country = input()
    if country != "India":
        raise NoMatchException
    print("Citizen Details:")
    print("Aadhar Number:", aadhar)
    print("Name:", name)
    print("City:", city)
    print("State:", state)
    print("Country:", country)
except NoMatchException:
    print("Country name does not match 'India'")