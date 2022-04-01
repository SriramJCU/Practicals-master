"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SENTINEL = -1
sales = float(input("Enter sales value (or -1 to Quit): "))
while sales != SENTINEL:
    bonus = 0
    if sales >= 1000:
        bonus = sales * 0.15
    else:
        bonus = sales * 0.10

    print("Bonus value is ${}".format(bonus))
    sales = float(input("Enter sales value (or -1 to Quit): "))
