#ecapsulations 

# class Account:
#     def __init__(self):
#         self.__pin=1111
        
        
#     def setPin(self, pin):
#         uname=input("Enter your name: ")
#         if (uname=="akshay"):
#             self.__pin=pin
#         else:  print("Invalid person")
            
#     def getPin(self):
#         uname=input("Enter your name: ")
#         if (uname=="akshay"):
# #             return self.__pin
#         else:  return "Invalid person"
        
        
# a=Account()
# a.setPin(1111)
# print(a.getPin())



       # Q10.create  a class and create addition in calculater
        
        
# class Calculator:
#     def add (self,*args):
#         print('adding:',sum(args))
        
# t=Calculator()
# t.add(1,2,3,4,5)
 
 
#mehod overriding##


class Parent:
    def property(self):
        print(" Cash | gold")
        
    def marry(self):
        print("marry with any girl")
        
class Child(Parent):
    def marry(self):
        print("marry with any katrina")
        
        
c=Child()
c.marry()
c.property()
    
    
    