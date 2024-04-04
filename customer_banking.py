# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    user_savings_balance = float(input("Enter your savings balance: "))
    user_interest_rate = int(input('Enter your interest rate: '))
    user_maturity = int(input('Enter the months on your account: '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(user_savings_balance, user_interest_rate, user_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # Format to 2 decimal places
    print(f'The updated savings account balance is ${updated_savings_balance:.2f} and the interest earned is ${interest_earned:.2f}')
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    user_cd_balance = float(input("Enter your cd balance: "))
    user_cd_interest_rate = int(input('Enter your cd interest rate: '))
    user_cd_maturity = int(input('Enter the months on your cd account: '))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(user_cd_balance, user_cd_interest_rate, user_cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # Format to 2 decimal places 
    print(f'The updated cd account balance is ${updated_cd_balance:.2f} and the interest earned is ${cd_interest_earned:.2f}')

if __name__ == "__main__":
    main()