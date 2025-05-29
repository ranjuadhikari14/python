balance=20000
print("welcome to simple bank ATM")
while True:
    input_text="""What do you want to do?
    1. Check Balance
    2. Deposit amount
    3. Withdraw amount
    4. Exit
"""
    user_input = int(input(input_text))
    if user_input == 1:
        print(f"your balance is {balance}")
    elif user_input == 2:
        amount=float(input("enter the amount to deposit:"))
        balance += amount
        print(f" Deposit successful.your new balance is {balance}")
    elif user_input ==3:
        amount=float(input("enter the amount to withdraw:"))
        if(balance>=amount):
            balance -=amount
            print(f" Withdraw Succesfully.your balance is {balance}")
        else:
            print("Insufficient Balance")
    elif user_input ==4:
        print("Thankyou for your ATM Service")
        break
    else:
        print("Invalid choice.Please Try Again")