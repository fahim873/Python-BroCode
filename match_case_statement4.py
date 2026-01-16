
def weekend(day):
    match day:
      case "Friday" | "Saturday":
        return True
      case "Sunday" | "Monday" | "Tuesday" | "Wednesday" | "Thursday":
        return False

day = (input("Day of Week: "))

print(weekend(day))
