def shipping_label(*args, **kwargs):
    for arg in args:
      print(arg, end=" ")
    print()
#    for value in kwargs.values():
#      print(value, end=" ")
    if "street" in kwargs:
      print(f"{kwargs.get('Street')} {kwargs.get('City')}")
    elif "Country" in kwargs:
      print(f"{kwargs.get('Country')}")
    else:
      print(f"{kwargs.get('State')} {kwargs.get('ZIP')}")



    print(f"{kwargs.get('Street')}")
    print(f"{kwargs.get('City')}")
    print(f"{kwargs.get('State')}")
    print(f"{kwargs.get('Country')}")
    print(f"{kwargs.get('ZIP')}")

shipping_label("Md", "Muntasir", "Al", "Fahim",
               Street = "Sector-6",
               City = "Uttara",
               State = "Dhaka",
               Country = "Bangladesh",
               ZIP = "1230")

