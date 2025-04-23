

# super method keyword

# class Person:
#     def __init__(self,a):
#         print("Person class consrtuctor",a)
        
# class Employee(Person):
#     def __init__(self,a):
#         super().__init__(a) # callimng super class constructor
#         print("Employee class consrtuctor")
        
# e=Employee(100)



# Q1). create a class person and name and age as attributes and second is Student class and his roll no ,age  as attribute


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
        
# class Subject:               # class subject relationship with student
#     def __init__(self,subject_name,duration,price):
#         self.subject_name=subject_name
#         self.duration=duration
#         self.price=price


# class Student(Person):
#     def __init__(self,name,age,rollno,marks,subject_name,duration,price):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.marks=marks
#         self.subject_name=subject_name
#         self.duration=duration
#         self.price=price
        
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Roll no:",self.rollno)
#         print("Marks:",self.marks)
#         print("Subject:",self.subject_name)
#         print("duration:",self.duration)
#         print("price:",self.price)
        
        
# s=Student("Raj",20,101,90,"Maths",5,2000)
# s.display() 


#################################################################


# class Employee:
#     def __init__(self,name,eid,salary):
#         self.name=name
#         self.eid=eid
#         self.salary=salary
        
#     def __str__(self):
#         return f"Name:{self.name} Eid:{self.eid} Salary:{self.salary}"
    
# e=Employee("Akshay",101,2000)
# print(e)
 
 
 
#pin change exmple 

# class Account:
#     def __init__(self):
#         self.__pin=4444
        
#     def setPin(self,pin):
#         self.__pin=pin
    
#     def getPin(self):
#         return self.__pin
    
# a=Account()
# a.setPin(1234)
# print(a.getPin())
    
###### method default argument

class Test:
    def m1(self,a=0,b=10,c=0):
        print("m1() called")
        
t=Test()
t.m1()
t.m1(1)
t.m1(1,2)
t.m1(1,2,3)
