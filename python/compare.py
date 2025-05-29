#write a program that takes the ages of two people as input from the user .compare their ages using comparision operators(==,!=,>,<,>=,<=)and print message indicating the results .(eg:"person1 is older than person2").


person1=20
person2=10
person1=int(input("enter the age of person1: "))
person2=int(input("enter the age of person2:"))
if( person1==person2 ):
    print("they are of same age")
if(person1!=person2):
        print("person1 and person2 arenot of the same age")
        if(person1>person2):
            print("person1 is older than the person2")
            if(person1<person2):
                print("person1 is younger than the person2")
                if(person1>=person2):
                    print("person1 is older or of equal age")
                    if(person1<=person2):
                        print("person1 is younger or of equal age")



   
                    
    
    
    
