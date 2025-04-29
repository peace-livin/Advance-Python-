# operator overloading

print(1+2)
print("java"+"python")
print(1*2)
print("java"*6)



class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
       print("adding magic method")
       return self.pages+other.pages
   
b1=Book(100)
b2=Book(200)

print('total pages',b1+b2)


# q1).create a class employee and name ,salary 2 obect using magic method greter than 


class Employee:
    def __init__(self,name,salary):
       self.name=name
       self.salary=salary
    def __gt__(self,other):
       print("greater than magic method")
       return self.salary>other.salary
   
e=Employee("akshay",3000)
e1=Employee("vijay",2000)   
print("akshay salary is greater than vijay",e>e1)
   
   
   
# q2). cretae a class Mobile and add basicphone and smartphone using call method
   
class Mobile:
    def __init__(self,brand,color):
       self.brand=brand
       self.color=color
    
class BasicPhone(Mobile):
    def call(Mobile):
       print("calling basicphone...")
       
class SmartPhone(Mobile):
    def call(Mobile):
       print("calling smartphone...")
  
m1=BasicPhone("samsung","black")
m2=SmartPhone("nokia","white")
m1.call()
m2.call()