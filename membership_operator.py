# Membership Operators = used to test wheather a value or varriable s found in a sequnece
#                        (string, lists, turple, set, or dictionary)
#                        1. in
#                        2. not in

word = "Apple"

letter = input("Guess a letter inn the secret word: ")

if letter in word:
  print(f"There is a {letter}")
else:
  print(f"{letter} was not found")

print()

if letter not in word:
  print(f"{letter} was not found")
else:
  print(f"There is a {letter}")

students = {"Fahim", "Nisha", "Shamim", "Sabbir", "Khairul"}

student = input("Enter a name of a student: ")

if student in students:
  print(f"{student} is present")
else:
  print(f"{student} is absent")

