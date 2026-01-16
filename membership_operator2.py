grades = {"Fahim": "3.89", "Nisha": "3.77", "Shamim": "4.00", "Khairul": "3.88"}

student = input("Enter the name of a student: ")

if student in grades:
  print(f"{student}'s grade is {grades[student]}")
else:
  print("{student} was not found")
print()

email = "fahim873@gmail.com"

if "@" in email and "." in email:
  print("Valid email")
else:
  print("Inavlid email")
