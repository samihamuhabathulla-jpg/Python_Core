total = int(input("Enter total number of animals: "))
rabbits = int(input("Enter number of rabbits: "))
deer = int(input("Enter number of deer: "))
birds = int(input("Enter number of birds: "))
squirrels = int(input("Enter number of squirrels: "))
actual = rabbits + deer + birds + squirrels
if actual == total:
    print("Baby lion is well behaved")
elif actual < total:
    print("Baby lion is mischievous")
else:
    print("Counted wrongly")