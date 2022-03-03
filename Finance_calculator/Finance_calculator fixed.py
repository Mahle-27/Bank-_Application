import math
#user prompted to choose a bond or investment calculator
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("Investment - to calculate the amount of interest you'll earn in interest ")
print("Bond       - to calculate the amount you'll have to pay on a home loan \n")
#user inputs selection
choice = input("Enter your choice: ").lower()

print()        

if choice == "investment":
    deposit_amount = float(input("Please enter the amount of money you wish to deposit: \n"))                
    interest_rate = int(input("Please enter your interest rate as a number: \n"))
    num_years = int(input("Please enter the number of years you plan on investing for: \n"))
    interest_type = input("Please enter your investment choice type: (simple or compound) \n")

    if interest_rate == "simple":
            A_simple = (deposit_amount*(1+interest_rate*num_years))
            print(f"Your total simple interest is R{A_simple:.2f}")
    elif interest_rate == "compound":
            A_compound = (deposit_amount*math.pow((1+interest_rate),num_years))
            print(f"Your total compound interest is R{A_compound:.2f}")

elif choice == "bond":   
    house_value = int(input("Please enter the present value of the house: \n"))
    interest_rate = int(input("Please enter your interest rate as a number (e.g. 1, 2, 3 etc.): \n"))
    num_months = int(input("Please enter the number of months you plan to take to repay the bond: \n"))      
    monthly_payment = round((interest_rate/100/12 * house_value) / (1 - math.pow((1+ interest_rate/100/12), (-1 * num_months))), 2)
    print("Your monthly repayment amount for the home loan is equal to R{}.".format(monthly_payment))

else:
    print("You have made an incorrect selection. Please choose either 'investment' or 'bond'.")