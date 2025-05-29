#write a python program that takes the age and citizenships status as a input from the users.use logical operators (and,of,not)to determine if the person is eligible to vote (age>=18 and is a citizen).print an appropriate message based on the result.

age=int(input("enter the age of a person"))
citizen=input("are you a citizen?(yes/no):").strip().lower()
if age>=18 and citizen=="yes":
    print(" you are eligible to vote")
else:
    print("you arenot eligible to vote")


    #write a program that initializes a list of books available in a library.Take the name of a book as a input from the user and check if it is available in the library using membership operator(in,not in).print a message indicating the book is available or not.

books=["software engineering","compiler","E-governance","e-commerce","c#","technical writting"]
name_book=input("enter the name of the book:").strip()
if name_book in books:
    print(f"{name_book} is avilable in the library.")
else:
    print(f"{name_book} is not available in the library")
