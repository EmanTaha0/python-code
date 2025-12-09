# Compound Interest Calculator with Goal Prediction
# Author: [EMAN TAHA]
# Date: [11/13/2025]

# Function to validate numeric input and ensure it's positive (or non-negative for goal)
def get_valid_input(str_prompt, b_allow_zero=False):
    while True:
        try:
            flt_value = float(input(str_prompt))
            if flt_value < 0 or (not b_allow_zero and flt_value == 0):
                print("Input must be a positive numeric value" if not b_allow_zero else "Input must be 0 or greater")
            else:
                return flt_value
        except ValueError:
            print("Input must be a positive numeric value")

# Get and validate user inputs
flt_deposit = get_valid_input("What is the Original Deposit (positive value): ")
flt_interest_rate = get_valid_input("What is the Interest Rate (positive value): ")
int_months = int(get_valid_input("What is the Number of Months (positive value): "))
flt_goal = get_valid_input("What is the Goal Amount (can enter 0 but not negative): ", b_allow_zero=True)

# Convert interest rate to monthly decimal
flt_monthly_rate = (flt_interest_rate / 100) / 12

# Compound interest calculation for specified months
flt_balance = flt_deposit
for int_month in range(1, int_months + 1):
    flt_interest = flt_balance * flt_monthly_rate
    flt_balance += flt_interest
    print(f"Month: {int_month} Account Balance is: ${flt_balance:,.2f}")

# Goal prediction loop
if flt_goal > 0:
    flt_balance = flt_deposit
    int_goal_months = 0
    while flt_balance < flt_goal:
        flt_balance += flt_balance * flt_monthly_rate
        int_goal_months += 1
    print(f"It will take: {int_goal_months:,} months to reach the goal of ${flt_goal:,.2f}")
