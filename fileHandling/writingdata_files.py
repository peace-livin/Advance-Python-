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

f1=open("f1.txt","w")
f2=open("f2.txt","w")
f3=open("f3.txt","w")
f3.write(f1.read())
f3.write(f2.read())
f1.close()
f2.close()
f3.close()

print('data into files ')