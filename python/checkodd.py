#write a program that checks if a given number is even or odd.take userinput for the number,perform the check ,and print the result.Include comments explainning each parts of the code.


num=int(input("enter the number:") )#enter a input from a user
if(num%2==0):      # if the number you had enter is divisible by 2 then
    print(f"{num} is Even")    #it returns the number you had enter is even.
else:
    print(F"{num} is a Odd.")   #else it returns the number you had enter is odd.
