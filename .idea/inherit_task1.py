class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def method(self):
        print(self.make,self.model)
class car(Vehicle):
    pass

obj=Vehicle("germen",2023)
obj.method()

#2
class Employee:
    def __init__(self,name,salary):
        self.name="fahad"
        self.salary=5700