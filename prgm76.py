class Time:
   def __init__(self,hour=0,min=0,sec=0):
       self.__hour = hour
       self.__min = min
       self.__sec = sec
   def show(self):
     print(self.__hour,':',self.__min,':',self.__sec)
   def __add__(self,other):
    h=self.__hour+other.__hour
    m=self.__min+other.__min
    s=self.__sec+other.__sec
    if s==60:
        s=0
        m+=1
    if m==60:
         m=0
         h+=1
    return Time(h,m,s)
t1=Time(4,10,15)
t2=Time(3,30,30)
t1.show()
t2.show()
t3=t1+t2
t3.show()
