def invest(amount, rate, years):
    new_amount = amount
    for index in range(1,years+1):
        new_amount = round(new_amount * (1+rate), 2)
        print(f'year {index}: ${new_amount}')

amount = float(input('Enter the principal amount: '))
rate = float(input('Enter the annual percentage rate:'))
years = int(input('Enter the number of years: '))
invest(amount, rate, years)