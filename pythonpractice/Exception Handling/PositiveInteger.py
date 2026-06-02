def get_positive_integer():
    try:
        val = int(input())
        if val <= 0:
            raise ValueError
        print(val)
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer.")
get_positive_integer()