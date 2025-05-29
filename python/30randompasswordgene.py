import random;
import string;
def gen_password(length=12):
    if length < 4:
         print("value must be at least 4 character length")
    character=string.punctuation
    capital=string.ascii_uppercase
    small=string.ascii_lowercase
    number=string.digits
    words=character+capital+small+number
    generate_password=[
        random.choice(capital),
        random.choice(small),
        random.choice(number),
        random.choice(character),
        
    ]
    generate_password+=random.choices(words,k=length-4)
    random.shuffle(generate_password)
    return''.join(generate_password)

try:
    password_length= int(input("enter the user password:"))
    print("generated password:",gen_password(password_length))
except ValueError as e:
        print(f"Error: Please enter valid numbers:{e}")

   