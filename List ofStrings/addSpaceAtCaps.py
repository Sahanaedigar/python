test_list = ["gfgBest", "forGeeks", "andComputerScience"]
def add_spaceatcaps(string):
    res=''
    for index,char in enumerate(string):
        if index>0 and char.isupper():
            res+=' '
        res+=char
    return res


li=['sahanaEdigar','saVi']
res=[add_spaceatcaps(word) for word in li]
print(res)

'''
How it works:
enumerate(s) gives us both the index and character for each position in the string.
The logic:

Start with empty result string
For each character, check two conditions:

i > 0 - Not the first character (avoid adding space at the beginning)
char.isupper() - Current character is uppercase


If both conditions are true, add a space to result
Always add the current character to result

Key points:
i > 0 prevents adding a space before the very first character
Only uppercase letters (after the first position) trigger space insertion
The character itself is always added after the optional space

Why it's "less elegant" than regex:

More verbose (8 lines vs 1 line with regex)
Manual iteration instead of pattern matching
But it's easier to understand for beginners!
'''