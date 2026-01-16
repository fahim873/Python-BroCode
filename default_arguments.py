# default arguments = A default value for certain parameters
#                      default is used when that argument is ommited
#                      make your functions more flexible, reduce #(number) of arguments
#                      1. Positional, 2. DEFAULT, 3. keyword, 4. Arbitrary

def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
print()

def net_price(list_price, discount = 0.01, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print()

#print(net_price(500,0.1,0.1))
