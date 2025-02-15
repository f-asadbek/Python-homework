def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount *= (1 + rate / 100)
        print(f"Year {i}: ${round(amount, 2)}")

amount = float(input("Enter the initial amount you want to invest: "))
rate = float(input("Enter an annual percentage rate: "))
years = int(input("Enter number of years: "))
invest(amount, rate, years)