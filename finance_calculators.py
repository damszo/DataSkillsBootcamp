# The user inputs whether he/she wants to calculate interest earned on an investment or calculate the amount needed to be paid on a home loan.
# The program outputs final calculations.

import math

selection = input("Please enter either 'investment' or 'bond': ").lower()

# The following block of code calculates interest (either simple or compound) on investment.

if selection == "investment" :
    deposit = int(input("Please enter the amount of deposit: "))
    interest_rate = int(input("Please enter the interest rate: "))
    invest_years = int(input("Please enter the amount of years you plan on investing: "))
    interest = input("Please enter either 'simple' or 'compound' interest: ").lower()

    if interest == "simple" :
        simple_int_calc = deposit * (1 + interest_rate/100 *  invest_years)
        print(f"The total amount when simple interest is calculated is {simple_int_calc}.")

    elif interest == "compound" :
        compound_int_calc = deposit * math.pow((1 + interest_rate/100),invest_years)
        print(f"The total amount when compound interest is calculated is {compound_int_calc}.")

# The following block of code calculates the monthly repayment on the bond.

    if selection == "bond" :
        house = int(input("Please enter the present value of the house: "))
        interest_rate_bond = int(input("Please enter the interest rate: "))
        months = int(input("Please enter the number of months you plan to repay the bond: "))

        bond_repayment = (interest_rate_bond/100/12 * house) / (1 - (1 + interest_rate_bond/100/12) ** (-months))
        print(f"You will have to repay {bond_repayment} each month.")

else :   
    print("You haven't entered either 'investment' or 'bond'. Please re-enter.")


