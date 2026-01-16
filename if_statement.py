#if = Do some code only IF some condition is true
#     Else do something else

age = int(input("Enter Your Age: "))

if (age >=100):
  print("You are too old")
elif (age >= 18):
  print("You are Eligable")
elif (age < 0):
  print("You haven't born yet")
else:
  print("You are not eligable")
