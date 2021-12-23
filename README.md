Gabriel Ferreri's Loan Analyzer Challenge ReADME.md file


General Comments:

Print statements including those with ("----------"), ("PART I"), ("     "), etc are used for spacing answers in the terminal window.


PART I Comments:

Questions 1 and 2 require the use of the len() function followed by the sum() function. A variable of loan_number was set to len(loan_costs) followed by a print statement saying the total number of loans.
A variable loan_total was set to the sum(loan_costs[0:]) to encapsulate the contents of the list, followed by a print statement saying the total sum of the loans. 

Last, the variable loan_total was divided by loan_number to calculate the average, followed by a print statement stating the average price of a loan.


PART II Comments:

I first started by creating variables future_value and remaining_months and assigned loan.get() functions to get the "future_value" and "remaining_months" for each. A print statement to display both values followed.
**Please note: in this section, I created a variable monthly_discount_rate to be used in the present value formula as the "r" in the formula would be the (annual_discount_rate / 12) for monthly periods.
I next made a variable called present_value, which is equal to the present value formula provided in the assignment, with future_value, monthly_discount_rate, and remaining_months inserted. A print statement to print the calculated present value is then executed to show the answer.
if_true and if_false variables were created to determine if the loan is worth the cost to buy it in statement form. 
A variable cost was created and assigned to execute a loan.get("loan_price") to get the loan's specific price. An if statement follows, were if present_value >= cost, the if_true variable will print with else printing the if_false variable.


PART III Comments:

First we define a calculate_present_value function, with the parameters of new_loan_future_value, monthly_discount_rate (from prior), and new_loan_months_remaining. Within said function, the present value formula is used and assigned to the new_loan_present_value variable, with the formula inputs defined in the function. A return statement was created to then return new_loan_present_value.
For the cost of a new loan, a variable cost_of_new_loan was created and assigned to the calculate_present_value() function, with the function inputs of new_loan["future_value"], monthly_discount_rate, and new_loan["remaining_months]. Note that new_loan refers to the list we're analyzing.
A print statement is then ran to state the newly-calculated cost_of_new_loan.


PART IV Comments:

loans refer to the given dictionary.
I first created the inexpensive_loans empty list.
To look for and compare the specific "loan_price" from each loan, a for loop was created using current_loan in loans (for current_loan in loans:) to analyze each individual loan.
Within the loop, an if statement is then created to see if each individual "loan_price" from each loan from current_loan <= 500, written as "if current_loan["loan_price"] <= 500:".
If the if statement is checks-out, the inexpensive_loans list will be appended with the current_loan information, written as inexpensive_loans.append(current_loan).
The loop ends, with a subsequential print statement of "The list of inexpensive loans include the following:" for formatting, followed by another print statement print.(inexpensive_loans) to print the applicable loans' information. 


Part V Comments:

Variable csv_path is created to hold the project path of the new inexpensive_loans.csv file. For debugging purposes, a "Writing the data to a CSV file..." print function was created.
Next, "with open() as   :" was done with (csv_path, "w") and csvfile, where the csv_path variable in open() is to output the .csv file, and the "w" makes the file writtable. csvfile is a new variable to hold file data.
csvwriter is then assigned to csv.writer(csvfile, delimiter=","), where csv calls the module contents, .writer() calls the writer function within the module, csvfile within .writer() allows the passage of said csvfile through the writer with "," as the delimiter. At this point we have our unedited .csv file.
A csvwriter.writerow(header) function was then made to write out the list items from header in a row within the .csv file, followed by a print statement for spacing and debugging. 
Now, a for loop is created with the inexpensive_loans list and the variable loan. Within the for loop, to add each inexpensive loan to the .csv file, csvwriter.writerow(loan.values()) was input, where loan.values() add each applicable loan information to the .csv file. this is followed by a print statement of loans.values() to see all the rows present within the file.




