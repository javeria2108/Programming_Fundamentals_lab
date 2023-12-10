#Part B, Saving with a raise

#The user shiuld enter annual salary
annual_salary= float(input("Enter your annual salary: "))
#The user should enter the portion of the salary to be saved in decimals
portion_saved= float(input("Enter the percent of your salary to save, as a decimal: "))
#The user should enter the cost of dream house
total_cost= float (input("Enter the cost of your dream home: "))
#enter raise after 6 months
semi_annual_raise=float (input("Enter the semi-­annual raise, as a decimal:"))



portion_down_payment= 0.25*total_cost
current_savings= 0
r=0.04
months=0
while current_savings<=portion_down_payment:
    months+=1
    current_savings+= (current_savings*r/12)+(annual_salary*portion_saved/12)
    if months%6==0:
        annual_salary+=annual_salary*semi_annual_raise
       
    
print ("Number of months: ",months)
        


#%% Part C Finding the right amount to save away
starting_salary = int(input("Enter the starting salary: "))
semi_annual_rise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25
months = 36

min_rate = 0        # 0%
max_rate = 10000    # 100%

portion_saved = int((max_rate + min_rate) / 2)
steps = 0
found = False

while abs(min_rate - max_rate) > 1:
    steps += 1
    annual_salary = starting_salary
    monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)
    current_savings = 0.0

    for i in range(1, months + 1):
        monthly_return = current_savings * (annual_return / 12)
        current_savings += monthly_return + monthly_saved

        if abs(current_savings - portion_down_payment) < 100:
            min_rate = max_rate
            found = True
            break
        elif current_savings > portion_down_payment + 100:
            break

        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_rise
            monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)

    if current_savings < portion_down_payment - 100:
        min_rate = portion_saved
    elif current_savings > portion_down_payment + 100:
        max_rate = portion_saved

    portion_saved = int((max_rate + min_rate) / 2)

if found:
    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search", steps)
else:
    print("Is is not possible to pay the down payment in three years") 