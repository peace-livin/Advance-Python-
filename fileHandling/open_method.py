# file handling
# how to open a file in python
# open (filenmae,openmode)

# '''
# opening mode:

# w: write mode (new file is created)
# r: read mode (new file won't be created)
# a: append mode (new file will be created)

# '''


# f=open("f1.txt","w")
# print('file opened')
# print('file is writable',f.writable())
# print('file is readable',f.readable())
# print('file name is',f.name)
# print('file is closed',f.closed)
# f.close()

# print('file is closed',f.closed)



# q1.) create a txt file and and find out  f1.txt files in the words and charcters

# f1=open("f1.txt","r")
# print(f1.read())
# f1.close()
# # text=open("f1.txt","r").read()
# word_count = len(text.split())
# char_count = len(text)
# print(word_count)
# print(char_count)
    
import csv  
    
# Open the file "f1.txt" in read mode and read its content
with open("f1.txt", "r") as f1:
    text = f1.read()

# Print the content of the file
print(text)

# Count the words and characters in the text
word_count = len(text.split())
char_count = len(text)

# Print the word and character counts
print("Word count:", word_count)
print("Character count:", char_count)

