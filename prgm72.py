class Flower:
    def __init__(self,f):
        self.name = f
    def display(self):
        if(hasattr(self,'petalcolor')):
            print(self.petalcolor," ",self.name)
        else:
            print("Unknown Flower!!")
                
F1=Flower('tulip')
setattr(F1,'petalcolor','red')
F1.display()
