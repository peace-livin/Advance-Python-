# writting data to file

# f=open("f1.txt","w")
# f.write("akshay\n")
# f.write("vishal\n")
# f.write("deepak\n")


# drinks=["water\n","milk\n","juice\n","tea\n"]
# f.writelines(drinks)
# f.close()
# print('data into files ')

# reading data from file  (print karna padega har file ko )

# f=open("f1.txt","r") 
# data=f.read(3) # read first3 characters

# print(f.readline()) # read first line
# print(f.readlines()) # read all lines

# allLines=f.readlines()
# for line in allLines:
#     print(line)


# q1). create  3 files f1 f2 f3 and write data in each file


# f2=open("f2.txt","w")
# f2.write("aaa\n")
# f2.write("bbb\n")

# f2.close()

# f3=open("f3.txt","w")
# f3.write("ccc\n")
# f3.write("ddd\n")

# f3.close()

# f4=open("f4.txt","w")

# f2=open("f2.txt","r")# open file f2
# f3=open("f3.txt","r")# open file f3


# f4.write(f2.read())
# f4.write(f3.read())

# f4.close()

# print('data into files ')




# inshot form  **first text in files and second text in files and then write all data in file f4**

# f1=open("f1.txt","w")
# f2=open("f2.txt","w")
# f3=open("f3.txt","w")
# f3.write(f1.read())
# f3.write(f2.read())
# f1.close()
# f2.close()
# f3.close()

# print('data into files ')


# tell : it will return curent position of file pointer
# f=open("f1.txt","r")
# print('file pointer location :',f.tell())
# print(f.read(2))
# print('file pointer location :',f.tell())
# print(f.read(4))
# print('file pointer location :',f.tell())
# f.seek(12) # move pointer to 12th position
# print(f.read(4))


# q2). create txt file f5.txt and change last name ..smart! to ..stupid!

# f=open("f5.txt","w")
# f.write("All students are stupid")
# f.seek(17)
# f.write("smart!")
# f.close()


import csv
# # working with csv (comma separated values) files

# f=open("product.csv","w")
# # To write data inside csv file we can  create csv writer 
# csv_writer=csv.writer(f) 
# csv_writer.writerow(["name","age","gender"])
# csv_writer.writerow(["akshay","25","male"])
# f.close()
# print('data into files ')


# q4.) use input 3 time pid ,pname, price ,quantity how many produncts you want to save csv file
# f=open("product.csv","w")
# csv_writer=csv.writer(f)
# csv_writer.writerow(["pid","pname","price","quantity"])

# pid=101
# ak=int(input("how many products you want to save: "))
# for i in range(ak):
#     pid=int(input("enter product id:"))
#     pname=input("enter product name:")
#     price=int(input("enter product price:"))
#     quantity=int(input("enter product quantity:"))
    
#     csv_writer.writerow([pid,pname,price,quantity])
   
#     pid=pid+1
# f.close()
    
# print('data into files ')




# reader #

import csv
# # f=open("product.csv","r") # To read data inside csv file we can  create csv reader
# # data=csv.reader(f)
# # for row in data:
# #     for record in row:
# #         print(record,end=" ") # end is used to print space after each record
# #     print()
    
# #* working with binary files: image ,pdf, audio,video*

# f=open("/workspaces/Advance-Python-/fileHandling/supercar.jpg","rb") # open binary file
# f2=open('mysupercar.jpg','wb') # open binary file
# f2.write(f.read()) # write 100 bytes
# print('data into files ')


# without with statement

# f=open("f1.txt","r+")
# print(f.read())
# f.write("\n this is new data " )
# print("kya ye file closed hai:",f.closed)
# f.close()
# print("kya ye file closed hai:",f.closed)


#with statement

# #is we open file in with statement then it will automatically close the file
# with open("f1.txt","r+") as f:
#     print(f.read())
#     f.write("\n hello akshay " )
#     print("kya ye file closed hai:",f.closed)
# print("kya ye file closed hai:",f.closed)


# q3.) create file f6.txt and read data from file f6.txt and line state with A is 2 and B is 3 and C is 

f=open("f6.txt","r")
data=f.read()
print(f.readlines)
a_count=0
b_count=0
c_count=0
for line in data :
    if line.startswith("A"):
        a_count=a_count+1
    elif line.startswith("B"):
        b_count=b_count+1
    elif line.startswith("C"):
        c_count=c_count+1
        
print("line start with A is ",a_count)
print("line start with B is ",b_count)
print("line start with C is ",c_count)


