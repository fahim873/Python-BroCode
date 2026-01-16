
def weekend(day):
    match day:
      case 1:
        return False
      case 2:
        return False
      case 3:
        return False
      case 4:
        return False
      case 5:
        return False
      case 6:
        return True
      case 7:
        return False
      case _:
        return False

day = int(input("Day of Week (input (1-7)): "))

print(weekend(day))
