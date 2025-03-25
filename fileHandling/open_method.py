# file handling
# how to open a file in python
# open (filenmae,openmode)

'''
opening mode:

w: write mode (new file is created)
r: read mode (new file won't be created)
a: append mode (new file will be created)

'''


f=open("f1.txt","w")
print('file opened')
print('file is writable',f.writable())
print('file is readable',f.readable())
print('file name is',f.name)
print('file is closed',f.closed)
f.close()

print('file is closed',f.closed)

