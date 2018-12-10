
from os import path




path.exists("numbers.txt")

#
# os.path.exists()
# Using path.exists you can quickly check that a file or directory exists. Here are the steps



print ("file exist:"+str(path.exists('numbers.txt')))
print ("directory exists:" + str(path.exists('C:\Program Files')))



# os.path.isfile()
# We can use the isfile command to check whether a given input is a file or directory.


print ("Is it File?" + str(path.isfile('numbers.txt')))
print ("Is it File?" + str(path.isfile('C:\Program Files')))



# os.path.isdir()
# If we want to confirm that a given path points to a directory, we can use the os.path.dir() function

print("Is it Directory?" + str(path.isdir('numbers.txt')))
print("Is it Directory?" + str(path.isdir('C:\Program Files')))
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""



file=open("data/numbers.txt", "a+")

for i in range(3):
     file.write("Appended line %d\r\n" % (i+1))

file.close()

# Open the file back and read the contents
file=open("data/numbers.txt", "r")
if file.mode == 'r':
    contents =file.read()
    print(contents)

lines =file.readlines()
for line in lines:
    print(line)


file.close()