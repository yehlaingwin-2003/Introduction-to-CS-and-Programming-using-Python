## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
no_of_months = 36

# lowest_rate_of_return = ?
cost_of_home = 800000
downpayment = (25/100) * cost_of_home

epsilon = 100

high = 1.0
low = 0.00
r = (high+low)/2;

steps = 1

amount_saved = initial_deposit * (1 + (r/12))**no_of_months


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################


while abs(amount_saved - downpayment) > epsilon and r < 1.0:
    steps += 1
    if amount_saved > downpayment:
        high = r
        r = (high+low)/2
        amount_saved = initial_deposit * (1 + (r/12))**no_of_months
    elif amount_saved < downpayment:
        low = r
        r = (high+low)/2
        amount_saved = initial_deposit * (1 + (r/12))**no_of_months

        
if r >= 1.0:
    r = None
    steps = 0
    print(f"Best savings rate: {r}")
    print(f"Steps in bisection search: {steps}")
else:
    print(f"Best savings rate: {r}")
    print(f"Steps in bisection search: {steps}")