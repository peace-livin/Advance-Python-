'''how to create a class in python

------------------------
syntax 

class ClassName:
    doc String
    constructor  
    static method
    class method
    instance method 
    
    
how to create an object in python 

syntax :
ref_variable = ClassName()

Students :
    name,marks ,rollno, gfname'''
    
    
class Student:
    def __init__(self):
        self.name = "akshay"
        self.marks = 99
        self.rollno = 32
        self.gfname = "ak"
        
s=Student()
print("student name is : ",s.name)
print("student marks is : ",s.marks)
print("student rollno is : ",s.rollno)
print("student gfname is : ",s.gfname)
        