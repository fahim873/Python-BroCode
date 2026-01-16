# return = statement used to end a function
#          and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

def mul(x,y):
    z = x * y
    return z

def div(x,y):
    z = x / y
    return z

print(add(3,4))
print()

print(sub(5,2))
print()

print(mul(3,4))
print()

print(div(12,3))
print()

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("mohammad", "fahim")
print(full_name)
