## 6.100A PSet 1: Part A
## Name: Ye Hlaing Win
## Time Spent: 1hr 
## Collaborators: None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("The cost of your dream house is: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
monthly_salary = yearly_salary/12


# down payment of the house
portion_down_payment = 0.25 # (25 %)
down_payment_of_house = cost_of_dream_home * portion_down_payment


# saving related information
amount_saved = 0 # initially zero for the first month
r = 0.05 # (5%) yearly return rate
# monthly_return is amount_saved * (r/12)


# the number of months set initially to zero
months = 0



###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved < down_payment_of_house: 
    # monthly saved amount for each month and return for each month
    monthly_saved_amount = monthly_salary * portion_saved
    return_each_month = amount_saved * (r/12)
    
    # increase amount saved for each month until it reaches the downpayment
    amount_saved += monthly_saved_amount + return_each_month
    
    # increase each month until saving reaches downpayment
    months += 1
    
 
print(f"Number of months: {months}")