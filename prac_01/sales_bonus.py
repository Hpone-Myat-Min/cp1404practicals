"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MAX_SALES_POINT = 1000                        # point to decide the amount of bonus
BONUS_OPTION_1 = 0.1
BONUS_OPTION_2 = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < MAX_SALES_POINT:
        bonus = sales * BONUS_OPTION_1
    else:
        bonus = sales * BONUS_OPTION_2
    print(f"For ${sales} sales, bonus = ${bonus}")
    sales = float(input("Enter sales: $"))
