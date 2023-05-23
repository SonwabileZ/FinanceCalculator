import math

#Prompt user
print("Select an option from\n1.Investment \n2.Bond")

#Input from user starts conditional statements
inv_bond = input(str("Choose either 'Investment' or 'Bond'\n" )).lower()

if inv_bond  == "investment":
    #if 'investment' is selected code executes
    if True:
        
        pr = float(input("Enter amount you are depositing:\n"))
        rate = float(input("Enter amount of interest rate: \n" ))
        r = (rate/100) / 12
        time = float(input("Enter duration for investment in years: \n"))
        simple_compound = str(input("Select either 'Simple' or 'Compound' interest. \n")).lower()

    if simple_compound == "simple":

        "simple" == simple_compound
        simple_compound = pr*(1 + r * time)
        total = simple_compound
        print (f"Interest earned over {time} years: {total:.2f}".format())

    elif simple_compound:
        # math.pow returns a value of x to the power of y (e.g math.pow(2, 3) gives output of 8)
        simple_compound = pr*math.pow((1+r),time)
        total = simple_compound
        print (f"Interest earned over {time} years: {total:.2f}".format())
        
#Bond is another conditional
elif inv_bond == "bond":
    #if 'bond' is selected code executes
    if True:

        pri = float(input("Enter the current value of the house: \n"))
        intr = float(input("Enter the interest rate: \n" ))
        i = ((intr/100)/12)/12
        no = float(input("Enter the duration in months: \n"))
        # math.floor rounds off to the nearest whole number
        monthly = float(math.floor((i*pri)/(1 - (1+i)**(-no))))
        print(f"Monthly repayment: {monthly:.2f}".format())

#if not Investment or Bond the code below executes
else:
    print("You entered an invalid input!\nPlease enter a valid input.")