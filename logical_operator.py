# Logical Operators = Evalute multiple conditions (or, and, not)
#       Or= at least one condition must be true
#       And = bot conditions must be true
#       not = Inverts the condition (not false, not true)

temp = 90
is_raining = False

if temp > 35 or temp < 0 or is_raining:
  print("The outdoor event is cancel")
else:
  print("The outdoor event is still sceduled")

temp = 90
is_sunny = True

if temp >=28 and is_sunny:
  print("It is hot outside 🥵")
  print("It is Sunny 🌞")

elif temp <= 0 and is_sunny:
  print("It is cold outside")
  print("It is Sunny")

elif 28 > temp > 0 and is_sunny:
  print("is is warm outside")
  print("Is is Sunny")

if temp >=28 and not is_sunny:
  print("It is hot outside 🥵")
  print("It is cloudy 🌞")

elif 28> temp >0 and not is_sunny:
  print("It is warm outside")
  print("Is is cloudy")

else:
  pass
