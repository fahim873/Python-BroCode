def display_name(*args):
    for arg in args:
      print(arg, end=" ")

display_name("Md", "Fahim")
print()
display_name("Md","Muntasir","Fahim")
print()
display_name("Md","Muntasir","Al","Fahim")
print()
display_name("Md","Muntasir","Al","Asad","Fahim")
print()

def print_address(**kwargs):
    print(type(kwargs))

print_address(street = "No.14",
              city = "Uttara",
              state = "Dhaka",
              postal = "1230",
              country = "Bangladesh")
print()

def print_address(**kwargs):
    for value in kwargs.values():
      print(value)

print_address(street = "No.14",
              city = "Uttara",
              state = "Dhaka",
              postal = "1230",
              country = "Bangladesh")
print()

def print_address(**kwargs):
    for key in kwargs.keys():
      print(key)

print_address(street = "No.14",
              city = "Uttara",
              state = "Dhaka",
              postal = "1230",
              country = "Bangladesh")
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
      print(key)

print_address(street = "No.14",
              city = "Uttara",
              state = "Dhaka",
              postal = "1230",
              country = "Bangladesh")
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
      print(f"{key}:{value}")

print_address(street = "No.14",
              city = "Uttara",
              state = "Dhaka",
              postal = "1230",
              country = "Bangladesh")
print()
