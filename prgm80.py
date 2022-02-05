class Publisher:
    def __init__(self,name="htc"):
        self.__name=name
    def display(self):
        print("Book Details\n")
        print("Name=",self.__name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.__title=title
        self.__author=author
    def display(self):
        super().display()
        print("Title:",self.__title)
        print("Author:",self.__author)
class Python(Book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.__price=price
        self.__pages=pages
    def display(self):
        super().display()
        print("Price:",self.__price)
        print("No of Pages",self.__pages)
a=Python('HMT Books','Programming in Python ','Jade',300,500)
a.display()
