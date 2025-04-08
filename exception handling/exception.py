# try-except-else-block
# else block is excuted only when there is no exception in try block
# try:
#     print("try block")
#     # print(10/0)
# except ZeroDivisionError as msg:
#     print(msg)
# else:
#     print("else block")
    
    
    
# try-except-finally-block
#finally : it is excuted always, it is used to clean resources
# try:
#     print("try block")
#     print(10/0)
# except ZeroDivisionError as msg:
#     print(msg)
# finally:
#     print("finally block")
    
# try:pass
# except:pass
# else:pass
# finally:pass



# try:pass
# finally:pass  . valid syntax

# try:pass
# else:pass     .invalid syntax

# try:pass  invalid syntax


# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# try:
#    akshay=a/b
#    print("the result is",akshay)
# except ZeroDivisionError as msg:
#     print("cannot divide by zero",msg)



# try:
#     n1=int(input("enter the number: "))
#     n2=int(input("enter the number: "))
#     try:
#         print(n1/n2)
#     except ZeroDivisionError :
#         print("cannot divide by zero")
# except Exception:
#     print("invalid input")