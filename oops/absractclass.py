# Absract class :partly implemented class
# Any python which is chaild of ABC class is called abstract class in python
# ABC class is present inside abc module


from abc import ABC,abstractmethod
#abc module is present inside python
#ABC is a class which is present inside abc module
#abstract method is a method which is present inside abc module
#abstract method is a method which is present inside abc module
from abc import *
class Test(ABC):
    def m1(self):
        print("m1()")
        
t=Test()
t.m1()

# ex2. 

class Test:
    def m1(self):
        print("m1()")
    @abstractmethod
    def m2(self):
        pass
    
t=Test()
t.m1()
t.m2()

# ex3.


class Test(ABC):
    def m1(self):
        print("m1()")
    @abstractmethod
    def m2(self):
        pass