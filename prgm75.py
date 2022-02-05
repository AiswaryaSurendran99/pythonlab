class Rectangle:
    def __init__(self,l,b):
        self.__length = l
        self.__breadth  = b
    def area(self):
          return self.__length*self.__breadth
    def __gt__(self,other):
        if(self.area()>other.area()):
            return True
        else:
            return False
     
R1=Rectangle(6,5)
R2=Rectangle(5,4)
print("area of R1=",R1.area())
print("area of R2=",R2.area())

if(R1>R2):
    print("R1 has larger area")
else:
    print("R2 has larger area")

