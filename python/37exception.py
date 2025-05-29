
try:
    num1=float(input("Enter Num1:"))
    num2=float(input("enter num2:"))
    sum=num1+num2
    print(f"total is {sum}")

except:
    print("please enter number only.")
finally:
    print("finally.our program is completed.")
