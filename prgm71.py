class Rectangle:
    def __init__(self):
        self.length = int(input("Enter the length:"))
        self.breadth  = int(input("Enter the breadth:"))

    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
R=Rectangle()
print("Area of the recatangle:",R.area())
print("Perimeter of the rectangle:",R.perimeter())

