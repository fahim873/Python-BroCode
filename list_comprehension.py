# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = []
for x in range(1,11):
  doubles.append(x * 2)

print(doubles)
print()

#doubles2 = [expression for value in iterable]
doubles2 = [x * 2 for x in range(1,11)]
triples = [x * 3 for x in range(1,11)]
squares = [x * x for x in range(1,11)]

print(doubles2)
print()
print(triples)
print()
print(squares)
print()

fruits = ["Apple", "Grapes", "Berry", "Strawberry", "Cherry"]

fruits = [fruit.upper() for fruit in ["Apple", "Grapes", "Berry", "Strawberry", "Cherry"]]
print(fruits)
print()

fruits = [fruit.lower() for fruit in ["Apple", "Grapes", "Berry", "Strawberry", "Cherry"]]
print(fruits)
print()

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)
print()

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

print(positive_nums)
print()
print(negative_nums)
print()
print(even_nums)
print()
print(odd_nums)
print()

grades = [85, 42 , 79, 90, 56, 61, 30]
passing = [grade for grade in grades if grade >= 60]

print(passing)
print()
