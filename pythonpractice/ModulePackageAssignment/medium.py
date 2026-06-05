#1. vowel count
from utilities.string import count_vowels
from utilities.number import is_prime

s=input("Enter string: ")
n=int(input("Enter number: "))

print(count_vowels(s))
print(is_prime(n))

#2.Random Password
import random

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
n=int(input("Enter length: "))
pwd=""
for i in range(n):
    pwd=pwd+random.choice(chars)

print("Generated password:",pwd)

#3 Square Root and Factorial
import math

n=int(input("Enter number: "))
print("Square root:",math.sqrt(n))
print("Factorial:",math.factorial(n))

#4 Random Item from List
import random

l=input("Enter list values: ").split()
print(random.choice(l))