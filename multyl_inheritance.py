class Grandfather():
    def __init__(self,height):
        self.height=height
        print(self.height)
class Grandmother():
    def __init__(self,colour):
        self.colour=colour

        print(self.colour)
class Father(Grandfather,Grandmother):
    def __init__(self,height,colour,name):
        super().__init__(height)
        super().__init__(colour)
        self.name = name
        print(self.name)
obj=Father('180cm','pink','subash')


