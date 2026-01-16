def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill is ${amount:.2f} is due: {due_date}")

display_invoice("Fahim", 10, "01/02/2026")
display_invoice("Nisha", 20, "05/02/2026")
