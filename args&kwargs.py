#    *args = Allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword - arguments
#            * unpacking operator
#            1. Positional, 2 Default, 3. Keyword, 4. ARBITRARY

#def add(a,b):
#    return a + b
#print(add(1,2))

#def add(*args):
#   print(type(args))
#print(add(1,2,3))

def add(*args):
    total = 0
    for arg in args:
      total += arg
    return total

print(add(1,2,3,4,5))

print()

def add(*nums):
    total = 0
    for num in nums:
      total += num
    return total

print(add(1,2,3,4,5))
