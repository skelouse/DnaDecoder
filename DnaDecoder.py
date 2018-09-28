#Open your DNA file with "python3 DnaDecoder.py dnafile.txt"
from sys import argv
import os
script, filename = argv

file = open(filename, 'r')
txt = file.read()



#Function to replace the tabs in a string with spaces
def replace_string_tabs(finish):
    length = len(finish)
    x = 0
    final = ''
    while x < length:
        if finish[x] == '\t':
            final = final + ' '
            x += 1
        else:
            final = final + finish[x]
            x += 1
        
    return final

#Creates a new file to paste into
def new_file():
    txt_new = open('apple', 'w')
    txt_new.write(replace_string_tabs(txt))
    txt_new.close()


#Counts the occurences of x in the file
def count(x):
    file_new = open('apple', 'r')
    txt_new = file_new.read()
    count = (f"Number of times {x} :" + str(txt_new.count(x)))
    file_new.close()
    return count

#Calling the new_file function to switch all tabs to spaces
new_file()

#Calling count function for each combination

#GG
print (count('G G'))
#GT
print (count('G T'))
#GA
print (count('G A'))

#TG
print (count('T G'))
#TT
print (count('T T'))
#TA
print (count('T A'))

#AG
print (count('A G'))
#AT
print (count('A T'))
#AA
print (count('A A'))

#00
print (count('0 0'))

#Removes the temp file without tabs
os.remove('apple')

#Closes the beginning file
file.close()
