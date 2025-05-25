test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
repl_chr = '*'
ret_chr = 'G'

st=''.join(test_list)
res=''
print(st)
for char in st:
    if char !='G':
       res+="*"
    else:
        res+=char


print(res)

'''
conver string into int in the list
Using list comprehension
List comprehension provides a more Pythonic and concise way to convert a list of 
strings to integers as it combines the conversion and iteration into a single line of code.

'''

x=[2, 4, 6, 8]

a = ['2', '4', '6', '8']
b = [str(item) for item in x] # change data type which to u want to convert
print(b)

'''
Sometimes we may have a string that looks like a list but is just text. We might want to 
convert that string into a real list in Python. The easiest way to convert a string that looks 
like a list into a list is by using the json module. This function will evaluate the string written 
as JSON list as a Python list. If the string is in JSON format (which looks like a Python list), we can use json.loads().
'''
import json  

# Use json.loads() to parse 
#the string and convert it into a Python list
s = '["Geeks", "for", "Geeks"]'  
a = json.loads(s)  
print(a)