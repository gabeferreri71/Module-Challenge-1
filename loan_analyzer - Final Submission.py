# coding: utf-8
import csv
from pathlib import Path

"Part 1: Automate the Calculations."


loan_costs = [500, 600, 200, 1000, 450]

print("          ")
print("PART I")
print("          ")
#variable loan_number set to len(loan_costs) followed by a print function

loan_number = len(loan_costs)
print(f"The total number of loans are {loan_number} loans.")
print("----------")


#variable loan_total set to sum(loan_costs [0:]) to encapsulate entire list

loan_total = sum(loan_costs [0:])
print(f"The total sum of the loans is ${loan_total: .2f}.") 
print("----------")

# previously set loan_total and loan_number used to calculate average

loan_avg = loan_total / loan_number
print(f"The average price of a loan is ${loan_avg: .2f}.")
print("----------")


"Part 2: Analyze Loan Data."

print("          ")
print("PART II")
print("          ")
# Given the following loan data, you will need to calculate the present value for the loan

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# using loan.get() to extract the future_value and remaining_months, followed by a print statement

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The future value is ${future_value: .2f} and the total remaining months are {remaining_months} months.")
print("----------")


# Note: "Annual Discount Rate" is noted to be used in the assignment, but below I have created a variable for the monthly discount rate, as the present value formula contains (1 + (Annual Discount Rate / 12))

annual_discount_rate = 0.20 
monthly_discount_rate = annual_discount_rate / 12


# Now using the monthly discount rate set from the annual discount rate to calculate the present value or "fair value" of the loan. future_value, monthly_discount_rate, and remaining_months are the input variables.
# Print statement made for present value of loan.

present_value = future_value / ((1+ monthly_discount_rate) **remaining_months) 
print(f"The present value of the loan is ${present_value: .2f}.") 
print("----------") 

#if_true and if_false variables set based on question parameters.

if_true = "The loan is worth at least the cost to buy it."
if_false = "The loan is too expensive and not worth the price."

# variable for cost created using loan.get() to get loan_price. 
# if statement created, where as if the present value (fair value) is greater than or equal to the cost variable,  the if_true string is printed, followed by an else statement printing the if_false string.
 
cost = loan.get("loan_price")
if present_value >= cost:
    print(if_true)
else:
    print(if_false)
print("----------")


"Part 3: Perform Financial Calculations."



# Given the following loan data, you will need to calculate the present value for the loan
print("          ")
print("PART III")
print("          ")

# Defining function calculate_present_value with variables new_loan_future_value, monthly discount rate (same as previous part; refer to monthly_discount_rate variable), and new_loan_months_remaining.
# within the function, the variable new_loan_present_value is set equal to the present value formula, with associated variables input.
# Return new_loan_present_value at end.

def calculate_present_value(new_loan_future_value, monthly_discount_rate, new_loan_months_remaining):
    new_loan_present_value = new_loan_future_value / ((1 + monthly_discount_rate)**new_loan_months_remaining)
    return new_loan_present_value 


new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Created cost_of_new_loan variable assigned to calculate the calculate_present_value function, with new_loan["future_value"], monthly_discount_rate, and new_loan["remaining_months"] as inputs.
# Print statement for the cost_of_new_loan to be generated.

cost_of_new_loan = calculate_present_value(new_loan["future_value"], monthly_discount_rate, new_loan["remaining_months"])
print(f"The present value of the loan is ${cost_of_new_loan: .2f}.")
print("----------")

"Part 4: Conditionally filter lists of loans."

print("          ")
print("PART IV")
print("          ")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# empty list for inexpensive_loans created.

# for loop created to analyze each current_loan for the loans dictionary, followed by an immediate if statement comparing each individual "loan_price" from current_loan, to see if 

# each "loan_price" <= 500

# Loans <= 500 are appended to the inexpensive_loans list using .append(current_loan) as the loops runs and analyzes each loan.

# The newly-appended inexpensive_oans list is now printed

inexpensive_loans = []  
for current_loan in loans:
    if current_loan["loan_price"] <= 500:
        inexpensive_loans.append(current_loan)
print("The list of inexpensive loans include the following:")
print("          ")
print(inexpensive_loans)


"Part 5: Save the results."

print("          ")
print("PART V")
print("          ")   
    

# csv_path variable created to hold the path object to the new csv file.

# print statement for debugging purposes created.

# To output the .csv file, with open() is used, with csv_path to pass the csv_path variable to the open function. "w" tells the programmer that we're making a writtable file.

# By typing as csvfile, we are creating a new variable to hold the file data

# csvwriter variable is created and assigned as csv.writer(csvfile, delimiter=","). csv is to call the module contents, .writer() function is calling the writer function within the module,
# and for (csvfile, delimiter=",") within the function, we are passing the csvfile through the writer with "," as the delimiter.

# To write the header to our file, the csvwriter.writerow(header) function was used to insert the header list in the top row of the inexpensive_loans.csv from csvwriter previously-set.

# Print statements made to help with debugging (should read "The following loans are present form the inexpensive_loans list")

#  for loop created within the "with" statement to add each applicable "loan" from "inexpensive_loans" 

# A similar csvwriter.writerow() will go within the for loop, with "loan.values()" going within the .writerow() function to write each applicable loan into the .csv file

# A final print(loan.values()) is made within the for loop to print each applicable loan.

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
csv_path = Path("inexpensive_loans.csv")
print("Writing the data to a CSV file...")
print("          ")
with open(csv_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    print("The following loans are present from the inexpensive_loans list:")
    print("          ")
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
        print(loan.values())

