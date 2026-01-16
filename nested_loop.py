# Nested Loops= A loop within another loop (Outer, Innner)
#               Outer Loop:
#                     Inner Loop:

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbols = (input("Enter the number of symbols: "))

for x in range(rows):
  for y in range(cols):
    print(symbols, end=" ")
  print()

