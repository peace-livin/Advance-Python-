# n=int(input("enter the number: "))
# print("* "*n)


# n=int(input("enter the number: "))
# for i in range(n):
#     print("* "*n)


# n=int(input("enter the number: "))
# for i in range(n):
#     print((str(i+1)+" ")*n)


# n=int(input("enter the number: "))
# for i in range(n):
#     print((chr(i+65)+" ")*n)
    
   # reverse format
# n = int(input("Enter the number: "))
# for i in range(n-1, -1, -1):  # Start from n-1 and go down to 0
#     print((str(i + 1) + " ") * n) 
   
   
# n=int(input("enter the number: "))
# for i in range(n):
#     for j in range(n):
#         print(j+1,end=" ")
#     print()
    
    
# reversed format
# n=int(input("enter the number: "))
# for i in range(n):
#     for j in range(n-1,-1,-1):
#         print(str(j+1),end=" "*n)
#     print()


# A 
# A A 
# A A A creat these patterns

# n=int(input("enter the number: "))
# for i in range(1,n+1):
#    print("A "*i)

# q1)
# 1
# 2 2
# 3 3 3 solve this pattern

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     print((str(i) + " ") * i)

# reverse format
# n = int(input("Enter the number: "))
# for i in range(n):
#     print((str(n - i) + " ") *(i+1) )


# Q3).
# a 
# b b
# c c c (same as '*')

# n=int(input("enter the number: "))
# for i in range(n+1):
#    print((chr(i+64)+" ")*i)


# n=int(input("enter the number: "))
# for i in range(n+1):
#    print("* "*i)

#  reverse star format

# n=int(input("enter the number: "))
# for i in range(n,0,-1):
#    print("* "*i)


#n = int(input("Enter the number: "))         #c
#for i in range(n):                           #b b 
 #   print((chr(n-i+96)+" ")*(i+1))           #a a a
 

# Q5.) solve this pattern in nested loop
#A 
#A B 
#A B C
#A B C D

# n=int(input("enter the number: "))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(j+65),end=" ")
#     print()
        
    
# reverse devending format


# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(chr((n-j)+64),end=" ")
#     print()



# n=4
# for i in range(n-1,-1,-1):                  # c b a
#     for j in range(i):                        c b
#         print(chr((n-j)+63),end=" ")          c
#     print()

#     a 
#   a  a
# a  a   a. make this pattern

def print_pattern(n):
    for i in range(1, n+1):
        # Print leading spaces
        print(" " * (n - i), end="")
        
        # Print the 'a' characters with spaces in between
        for j in range(1, i + 1):
            print("a", end=" ")
        
        # Move to the next line
        print()

# Specify the number of rows
n = 3
print_pattern(n)

