#Task 2: Bank Interest If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year.
#So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

#Writing algorithm to define savings account, interest rate, and total amount of interest + savings account.
savings_account = 9010
interest = savings_account * .07

total_amount = savings_account + interest

#printing to show user result
print("After 1 year your total savings account with your interest counted will be", total_amount, "starting from", savings_account)