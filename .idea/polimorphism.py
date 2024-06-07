class Vehicle:
    def speed(self):
        print("speed 190km")
    def engine(self):
        print("v3 engine")


class Mustang(Vehicle):
    def speed(self):
        print("speed 320km")
        Vehicle.speed(self)
    def engine(self):
        print("v12 engine")
        super().engine()


obj=Mustang()
obj.speed()
obj.engine()
