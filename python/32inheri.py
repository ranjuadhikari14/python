class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_info(self):
        print(f"name is {self.name} and age is {self.age}")
    
class student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade

    def get_info(self):
        super().get_info()
        print(f"Grade is {self.grade}")
    
s1=student(name="ram",age=19,grade=79)
print(s1.get_info())
