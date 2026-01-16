# dictionary  = a collection of {key:value} pairs
#               orderes and changeable. No duplicate

capitals= {"USA" : "New York",
           "Bangladesh" : "Dhaka",
           "Pakistan" : "Islamabad",
           "Turkey" : "Istanbul",
           "Azerbaizan" : "Baku",
           "Iran" : "Isfahan"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("Iran"))
#print(capitals.get("Japan"))
print()

if capitals.get("Japan"):
  print("That capital exists")
else:
  print("That capital does not exists")
print()

if capitals.get("Turkey"):
  print("That capital exists")
else:
  print("That capital does not exists")
print()

#capitals.update({"Germany" : "Berlin"})
#capitals.update({"Bangladesh" : "Jahangirnagar"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
#capitals = capitals.keys()
#print(capitals)

keys = capitals.keys()

for key in capitals.keys():
  print(key)
print()

values = capitals.values()
for value in capitals.values():
  print(value)
print()

items = capitals.items()
#print(items)
for key, values in capitals.items():
  print(f"{key} -> {value}")
