def invest(amount, rate, years):
    year_count = 0
    while year_count < years:
        amount = amount + (amount*rate)
        year_count += 1
        print(f"year {year_count}: {round(amount, 2)}")

try:
    amount = float(input("Enter amount: "))
    rate = float(input("Enter rate: "))
    years = int(input("Enter years: "))
    invest(amount, rate, years)


except(ValueError, TypeError, NameError):
    print("Invalid input. Please enter a valid number.")
