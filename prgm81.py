class Person:
     def getp(self,n,m):
        self.name=n
        self.phno=m
class Dept:
    def getd(self,n1,l):
        self.name1=n1
        self.location=l
        
class Employee(Person,Dept):
    def gete(self,n,m,n1,l,d,s):
          self.getp(n,m)
          self.getd(n1,l)
          self.designation=d
          self.salary=s

    def display(self):
        print("DETAILS\n")
        print("Name=",self.name)
        print("Phno=",self.phno)
        print("Deptname=",self.name1)
        print("Location=",self.location)
        print("Designation=",self.designation)
        s=self.salary+0.1*self.salary
        print("Salary=",s,",\n")
    def __eq__(self,other):
        if(self.name1==other.name1):
             return True
        else:
             return False
    def __ge__(self,other):
        if(self.salary>=other.salary):
             return True
        else:
             return False
          
       
E1=Employee()
E2=Employee()
E1.gete("Arya",9999999999,"HR","Bangalore","Manager",50000)
E1.display()
E2.gete("Annie",9743123456,"Computer","America","Asst.Manager",60000)
E2.display()
if(E1==E2):
     print("Equal Departments.")
else:
     print("Different Departments.")
if(E1>=E2):
     print("\nE1 has greater salary!!!")
else:
     print("\nE2 has greater salary!!!")
     
