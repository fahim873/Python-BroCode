# iterables = An object/collection that can return its element one at a time,
#            allowing it to be iterable over in a loop

numbers = [1, 2, 3, 4, 5]
#numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number)

print()

for blablabla in numbers:
    print(blablabla, end=" ")

print()

for number in reversed(numbers):
    print(number)

print()

fruits = {"Apple", "Grapes", "Berry", "Strawberry", "Cherry"}

for fruit in fruits:
  print(fruit)

print()

for blablabla in fruits:
  print(blablabla)

print()

name = "Mohammad Fahim"

for character in name:
  print(character)
print()

for character in reversed(name):
  print(character)
print()

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key in my_dictionary:
  print(key)
print()

for value in my_dictionary.values():
  print(value)
print()

for key, value in my_dictionary.items():
  print(f"{key} : {value}")
print()
