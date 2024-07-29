1
n = int(input("Enter the number of terms: "))

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
2
s = input("Enter a string: ")
print("Reversed string:", s[::-1])
3
temp = float(input("Enter temperature: "))
scale = input("Enter scale (C for Celsius, F for Fahrenheit): ")

if scale.upper() == 'C':
    converted = (temp * 9/5) + 32
    print(f"{temp}C is {converted}F")
elif scale.upper() == 'F':
    converted = (temp - 32) * 5/9
    print(f"{temp}F is {converted}C")
else:
    print("Invalid scale")
4
lst = [1, 2, 3, 4, 5]
print("List:", lst)

lst.append(6)
print("After appending 6:", lst)
lst.remove(3)
print("After removing 3:", lst)
lst.sort()
print("Sorted list:", lst)
lst.reverse()
print("Reversed list:", lst)

5
s = input("Enter a string: ").replace(" ", "").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
6
s = input("Enter a string: ").replace(" ", "").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
7
s = input("Enter a string: ")
vowels = "aeiou"
count = sum(1 for char in s.lower() if char in vowels)
print("Number of vowels:", count)
8
import time

seconds = int(input("Enter time in seconds: "))

while seconds:
    mins, secs = divmod(seconds, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    time.sleep(1)
    seconds -= 1

print("Time's up!")
9
import random

words = ["python", "java", "ruby", "javascript"]
word = random.choice(words)
guesses = set()

print("Guess the word!")

while True:
    guess = input("Enter a letter: ").lower()
    
    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses.add(guess)

    if all(letter in guesses for letter in word):
        print(f"Congratulations! You've guessed the word: {word}")
        break
    else:
        print("Keep guessing!")
10
squares = [x**2 for x in range(10)]
print("Squares:", squares)
