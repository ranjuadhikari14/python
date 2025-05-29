#program with no parameter no return type
def country():
    print("we are in Nepal")
country()

#program with parameter but no return type
def full_name(first_name,last_name):
    print(f"your full name is {first_name} {last_name}")

full_name("ranju","adhikari")



#program with parameter and return type
def full_name(first_name,last_name):
    fullname=f"{first_name} {last_name}"
    return fullname

fn=full_name("Ranju","Adhikari")
print(fn)


#no parameter and return type
  
def voter_age():
    return 18
ram_age=16
if ram_age >= voter_age():
    print("Ram is a voter")
else:
    print("Ram isnot a voter")