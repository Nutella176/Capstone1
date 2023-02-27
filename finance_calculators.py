import math 

#Ask user to input either investment or bond depending on the service required
calculation = input("""
investment - to calculate the amount of interest you'll earn on your investment 
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed: """).lower()

#Display error message if user inputs something other than investment or bond
if not calculation == "bond" and not calculation == "investment":
    print("Incorrect input, please enter either 'investment' or 'bond'")
    
#If user inputs investment- ask user for deposit amount, interest rate, lenght of investment and to input either simple or compound interest 
#Set additional condition depending if user inputs simple or compound interest, calculate and print return on investment
if calculation == "investment":
    amount = float(input("How much are you investing? "))
    rate = float(input("What's the interest rate? (enter percentage without %) ")) / 100
    years = float(input("How many years are you planning to invest? "))
    interest = input("Simple or compound interest? ")
    if interest == "simple":
        return_on_investment = amount * (1 + rate * years)
        return_on_investment = round(return_on_investment, 2)
        print(f"Based on the information provided, your return on investment would be £{return_on_investment}")
    elif interest == "compound":
        return_on_investment = (amount * math.pow((1 + rate), years))
        return_on_investment = round(return_on_investment, 2)
        print(f"Based on the information provided, your return on investment would be £{return_on_investment}")
        
#If user inputs bond- ask user for house value, interest rate and how many months to repay it
#Calculate monthly interest rate
#Calculate and print how much user needs to repay each month 
if calculation == "bond":
    house_value = float(input("What's the present value of the house? "))
    interest_rate = float(input("What's the interest rate? (enter percentage without %) ")) / 100
    months_payback = float(input("How may months will it take to repay the bond? "))
    monthly_interest_rate = interest_rate / 12
    pay_per_month = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-months_payback))
    pay_per_month = round(pay_per_month, 2)
    print(f"Based on the information provided, your monthly bond repayment is £{pay_per_month}")
    


