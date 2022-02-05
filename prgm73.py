class Book:
    def __init__(self):
        self.title = input("Enter the title of the book:")
        self.author = input("Enter the author of the book:")
    def display(self):
        if(hasattr(self,'publisher')):
            print(self.title," written by ",self.author," is published by ",self.publisher)
        else:
            print("Unknown Publisher!!")
                
B1=Book()
setattr(B1,'publisher','dc')
B1.display()
