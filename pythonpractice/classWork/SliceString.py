str='HELLO'
print(str[3:3])

str_1='Good Day'
print(str_1[::-2])

greetings ="Hello world!"
new_greeting ='J'+greetings[-6:-1]
print(new_greeting)

word ='banana'
word.find('na',3)
word ='Good Day'
index =word.find('a')
print(index)
word.find('Da')

word ='Good Day'
new_word=word.replace('Good','Happy')
print(new_word)

text="python is easy to learn"
text.endswith("to learn.")
text.startswith("python")

n =input('Enter String:')
if n==n[::-1]:
    print(n,"is palindrome String")
else:
    print(n,"is not palindrome String")