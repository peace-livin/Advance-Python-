from threading import *

# def sayHello():
#     for i in range(10):
#         print("child thread")
        
# t = Thread(target=sayHello)  # ek thread banaya gaya hai jo sayHello function run karega
# t.start()                    # thread ko start kiya gaya

# for i in range(10):
#     print("main thread")     # yeh main thread ka kaam hai


import time
from threading import *

# class MYThread(Thread):
#     def run(self):
#         name="akshaydarade"
#         for c in name:
#             print(c)
#             time.sleep(2)
            
# t=MYThread()
# t.start()
# for i in range(6):
#     print(i)
#     time.sleep(2)


#without extending Thread class

# class MYThread:
#     def print_Char(self):
#         name="akshaydarade"
#         for c in name:
#             print(c)
#             time.sleep(2)
            
# t=MYThread()
# thread=Thread(target=t.print_Char)
# thread.start()
# for i in range(6):
#     print(i)
#     time.sleep(2)


# datetime function

import time
import datetime
from threading import *


# def double(list):
#     for i in list:
#         print('double is ',i*2)
#         time.sleep(2)
        
        
# def sqare(list):
#     for i in list:
#         print('square is ',i*i)
#         time.sleep(2)
        
# nums=[1,2,3,4,5,6,7,8,9,10]
# begining_time=datetime.datetime.now()

# t1=Thread(target=double,args=(nums,))
# t2=Thread(target=sqare,args=(nums,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("total time: ",datetime.datetime.now()-begining_time)




# join  method  
def f1():
    for i in range(10):
        print("child thread")
        time.sleep(2)
        
t1=Thread(target=f1)
t1.start()
t1.join()

for i in range(10):
    print("main thread")
    time.sleep(2)