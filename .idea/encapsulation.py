class Employee:
    def __init__(self):
        self.name="fahad"
        self.__salary=5400

    def method(self):
        return self.__salary
    def set_datat(self):
        self.__salary=6200



epm=Employee()
print(epm.method())
epm.set_datat()

print(epm.method())


