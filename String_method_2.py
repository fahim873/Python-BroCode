# validate user input exercise
# 1. Username is not more than 12 characters
# 2. Username must not contain space
# 3. Username must not contain digits

username = input("Enter an username: ")

if len(username) > 12:
    print("The username can't be more than 12 characters")

elif " " in username:
    print("Your username can't contain spaces")

elif not username.isalpha():
    print("Your username can't contain numbers")

else:
    print(f"Welcome {username}")


