class InvalidUsernameException(Exception):
    pass
class InvalidPasswordException(Exception):
    pass
try:
    username=input("Enter username: ")
    password=input("Enter password: ")
    if len(username)<6 or len(username)>30:
        raise InvalidUsernameException

    if not username[0].isalpha():
        raise InvalidUsernameException

    if len(password)<8:
        raise InvalidPasswordException

    if not any(i.islower() for i in password):
        raise InvalidPasswordException

    if not any(i.isupper() for i in password):
        raise InvalidPasswordException

    if not any(i.isdigit() for i in password):
        raise InvalidPasswordException

    print("Welcome",username)
except InvalidUsernameException:
    print("Invalid username or password.")
    print("Username length should be between 6 and 30 characters.")

except InvalidPasswordException:
    print("Invalid username or password.")
    print("Password is not valid.")