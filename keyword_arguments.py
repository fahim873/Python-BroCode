# Keyword Arguments = an argument preceded by an identifier
#                     helps with readability
#                     oder of argumenets doesn't matter
#                     1. Positional, 2. d=Default, 3. KEYWORD, 4. Arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Mohammad", "Muntasir", "Fahim")
print()

hello("Hello",  title="Mohammad", last="Fahim", first="Muntasir" )
print()

for x in range (1,11):
  print(x, end=" ")
print()
print()

print("1", "2", "3", "4", "5", sep="-")
print()

def get_phone(country, sim, first, last):
    return(f"{country}{sim}{first}-{last}")

phone_num = get_phone(country=880, sim=17, first=817, last=99873)

print(phone_num)
