a = ['gfg', 'is', 'best', 'for', 'geeks']

# List of characters to check for
remove_chars = ['g', 'e']
res=[]
for word in a:
    if not any (char in word for char in remove_chars) :
        res.append(word)
print(res)

'''
Key concepts:

any() returns True if ANY condition in the iterator is True
char in word checks if a character exists anywhere in the word
not any(...) means "only keep words that DON'T contain any of these characters"
Words containing 'g' OR 'e' (or both) get filtered out
'''