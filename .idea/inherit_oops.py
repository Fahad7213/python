# class Vehicle:
#     def __init__(self,speed,colour):
#         self.speed = speed
#         self.colour = colour
#     def method1(self):
#         print(self.method1())
#
# class Engine(Vehicle):
#     def __init__(self,model,capacity):
#         self.model = model
#         self.capacity = capacity
#     def method2(self):
#         print(self.method2())
#
# obj=Engine("v12","12ltr")
# obj=Vehicle(120,"black")


#super
# class Vehicle:
#     def __init__(self,speed,colour):
#         self.speed = speed
#         self.colour = colour
#     def method1(self):
#         print(self.method1())
#
# class Engine(Vehicle):
#     def __init__(self,model,capacity,speed,colour):
#         self.model = model
#         self.capacity = capacity
#         super().__init__(speed,colour)
#     def method2(self):
#         print(self.model,self.capacity)
#         print(self.speed,self.colour)

# obj=Engine("v12","12l",320,"black")
# obj.method2()


#eg of supr
class Vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model
        print("Vehicle")

class Child(Vehicle):
    def __init__(self,speed,mileage,name,model):
        self.speed=speed
        self.mileage=mileage
        super().__init__(name,model)
        print(self.speed,self.mileage,self.name,self.model)

obj=Child("320km","14","swift","2024")