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


