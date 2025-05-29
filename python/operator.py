
### program for a person to withdraw amount from ATM
user_id=101
user_pin=1424
userenter_id=int(input("enter the userid:"))
userenter_pin=int(input("enter the valid pin :"))
if(user_id==userenter_id and user_pin==userenter_pin):
    print("login successfully.")
else:
    print("login failed.")