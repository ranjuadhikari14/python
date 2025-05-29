class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def get_info(self):
        return f"length is {self.length} and breadth is {self.breadth}"
    
    def find_area(self):
        return f"area of the rectangle is :{ self.length*self.breadth}"

s1=Rectangle(length=5,breadth=10)
print(s1.get_info())
print(s1.find_area())
                
    