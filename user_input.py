# input() = A function that prompts the user to enter data Returns the entered data as a string
name = input("What's your name?: ")
age = input ("How old are you: ")

age = int(age)
age = age + 1

print(f"Hello {name}!")
print(f"You are {age} years old.")

#Exercise -- 01 Rectangle area calculation

length = input ("Enter the length: ")
width = input ("Enter the width: ")

length = float(length)
width = float(width)

area = length*width

print(area)

#Exercise -- 02 Shooping Cart Program

item = input("What should you like to buy: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like: "))
total = price*quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Grand total: ${total}")
