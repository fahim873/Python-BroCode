# while loop = execute some code While some condition remains true

name = input("Enter your name: ")

if name == "":
  print("You did not enter your name")
  name = input("Enter your name: ")
#print(f"Hello {name}")

else:
  print(f"Hello {name}")


