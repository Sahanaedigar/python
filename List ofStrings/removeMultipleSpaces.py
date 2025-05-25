li = ["Hello   world", "   Python is  great  ", "   Extra  spaces here  "]
print(li)
# Remove multiple spaces in each string using split and join
res=[]

for string in li:
    newstr=' '.join(string.split())
    res.append(newstr)
print(res)

'''
How string.split() and ' '.join() work together:

string.split() (without arguments):

Splits on ANY whitespace (spaces, tabs, newlines)
Removes leading/trailing whitespace
Treats multiple consecutive spaces as ONE separator
Returns a list of words


' '.join():

Joins the list of words back with single spaces



Step by step execution:

string = "Hello   world":

string.split() → ['Hello', 'world']
' '.join(['Hello', 'world']) → 'Hello world'


string = "   Python is  great  ":

string.split() → ['Python', 'is', 'great']
' '.join(['Python', 'is', 'great']) → 'Python is great'


string = "   Extra  spaces here  ":

string.split() → ['Extra', 'spaces', 'here']
' '.join(['Extra', 'spaces', 'here']) → 'Extra spaces here'



Output: ['Hello world', 'Python is great', 'Extra spaces here']
Why this works so well:

split() without arguments is smart - it handles all types of whitespace issues
The combination automatically normalizes spacing to single spaces
It's a common Python idiom for cleaning up messy text
'''

test_list = ["gfgBest", "forGeeks", "andComputerScience"]
def add_spaceatcaps(string):
    res=''
    for index,char in enumerate(string):
        if index>0 and char.isupper():
            res+=' '
        res+=char
    return res


add_spaceatcaps('sahanaEdigar')
