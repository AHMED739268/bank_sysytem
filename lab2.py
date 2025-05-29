import re
import random

# def generate(length, start):



#     result = []
#     for i in range(length):
#         number = start + i
#         result.append(number)
#
#     return result
#
# print(generate(5,1))
#
# #task2
#
#
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
# print(fizz_buzz(9))

#task3
# def reverse_string(text):
#     stack = []
#
#     for char in text:
#         stack.append(char)
#
#     reversed_text = ""
#
#     while stack:
#         reversed_text += stack.pop()
#
#     return reversed_text
#
# text='ahmed'
# print(reverse_string(text))
#task4


#
# def is_valid_email(email):
#     pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
#     return re.match(pattern, email)
#
# def get_valid_name():
#     while True:
#         #strip like trim
#         name = input("Enter your name: ").strip()
#         if name and not name.isdigit():
#             return name
#         else:
#             print("Invalid name. Please enter a valid name (not empty or numbers only).")
#
# def get_valid_email():
#     while True:
#         email = input("Enter your email: ").strip()
#         if is_valid_email(email):
#             return email
#         else:
#             print("Invalid email format. Please enter a valid email.")
#
#
# name = get_valid_name()
# email = get_valid_email()
#
#
# print("Name:", name)
# print("Email:", email)
#
#
# #task 5
# def longest_alphabetical_substring(s):
#     longest = ""
#     current = ""
#
#     for i in range(len(s)):
#         if i == 0 or s[i] >= s[i - 1]:
#             current += s[i]
#         else:
#             current = s[i]
#
#         if len(current) > len(longest):
#             longest = current
#
#     print("Longest substring in alphabetical order is:", longest)
#
# longest_alphabetical_substring('harbiahmedsalah')

#task6

# def read_numbers():
#     total = 0
#     count = 0
#
#     while True:
#         user_input = input("Enter a number (or type 'done' to finish): ")
#
#         if user_input.lower() == 'done':
#             break
#
#         try:
#             number = int(user_input)
#             total += number
#             count += 1
#         except ValueError:
#             print("Error: Please enter a valid number.",ValueError)
#
#     if count > 0:
#         average = total / count
#         print("\nTotal:", total)
#         print("Count:", count)
#         print("Average:", average)
#     else:
#         print("No valid numbers were entered.")
#
#
# read_numbers()
#task7



listword = ["python", "c", "java"]
word = 'youssef'
display = list("_" * len(word))
print(display)

guesses = []
attempts = 7

while attempts > 0:
    print("\nWord: " + ' '.join(display))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guesses:
        print("You already guessed that letter!")
        continue

    guesses.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("✔️ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

    if "_" not in display:
        print("\n🎉 You won! The word was:", word)
        break

if "_" in display:
    print("\n💀 Game over! The word was:", word)


