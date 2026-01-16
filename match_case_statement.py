# Match-Case statement (Switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benifits: Cleaner and syntax is more readable

def day_of_week(day):
    if day == 1:
      return "It's Sunday!"
    elif day == 2:
      return "It's Monday!"
    elif day == 3:
      return "It's Tuesday!"
    elif day == 4:
      return "It's Wednesday!"
    elif day == 5:
      return "It's Thursday!"
    elif day == 6:
      return "It's Friday!"
    elif day == 7:
      return "It's Sunday!"
    else:
      return "---Invalid---"

day = int(input("Day of Week (input (1-7)): "))

print(day_of_week(day))
