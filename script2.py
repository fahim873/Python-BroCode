from script1 import *

print()
#print(__name__)

def fav_drink(drink):
    print(f"Your Favorite drink is {drink}")

def main():
  print("This is script 2")
  fav_food("Soup")
  fav_drink("Coffe")
  print("GoodBye")
  print()

print("This is script 2")
fav_food("Soup")
fav_drink("Coffe")
print("GoodBye")

if __name__ == '__main__':
    main()
