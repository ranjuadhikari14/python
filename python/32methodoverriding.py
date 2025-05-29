class Vehicles:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def get_info(self):
        return f"vehicle make is :{self.make} and vehicle model is {self.model}"
    
class Car(Vehicles):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year=year

    def get_info(self):
       base_info= super().get_info()
       return (f"{base_info},year is {self.year}")


c1=Car(make="Honda",model="civic",year=2018)
v1=Vehicles(make="Toyata",model="corolla")
print(c1.get_info())
print(v1.get_info())


