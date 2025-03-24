# working with random numbers
# to generate random numbers


import random

# # random(): #it will return a float number between 0 and 1

# print(random.random())


# # uniform(a,b): #it will return a float number between low and high
# print(random.uniform(5,9))

# # randint(): # it will return an integer between a and b
# print(random.randint(5,9))


# #randrange(): # it will return an integer between a and b
# print(random.randrange(10))
# print(random.randrange(5,15))
# print(random.randrange(5,15,2))

# # choice(): it will return random object from seq 
# fruits=["apple","mango","orange","banana"]
# print(random.choice(fruits))


# Q1). generate  wap to generated 4 digit otp and number having space


for j in range(4):
    for i in range(4):
        print(random.randint(0,9),end="")
    print()