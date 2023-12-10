starting_salary = float(input("Enter your starting salary:​ "))
months_salary = starting_salary/12
total_cost = 1000000.0
semi_annual_rate = .07
investment_return = 0.04
down_payment = total_cost * 0.25
r = 0.04
current_savings = 0.0
#months = 36
tolerance = 100
steps = 0
high = 1.0
low = 0.0
guess = (high+low)/2.0
total_salaries = 0.0
def calSavings(current_savings,months_salary,guess,month):
    for months in range(0,37):
        if  months%6==1 and months >1:
            months_salary=months_salary*(1+semi_annual_rate)
        current_savings = current_savings + months_salary * guess
        current_savings = current_savings * (1+0.04/12)
    return(current_savings)
current_savings = calSavings(current_savings,months_salary,guess,1)
while abs(current_savings-down_payment)>=100:
    if  current_savings < down_payment:
        low = guess
    elif current_savings > down_payment:
        high = guess
    else:
        print("It is not possible to pay the down payment in three years.")
        break
    guess = (low+high)/2
    steps = steps +1
print("Best saving rate: ", guess)
