a = ['Gfg is best', 'for Geeks', 'Preparing']
splitat=' '
res=[]
for i in a:
    splitWord=i.split(splitat)
    res.append(splitWord)
# print(res)
# split(' ') always returns a list of substrings


test_list = ["geeksforgeeks", "best", "geeks", "and"]
pref = "geek" 
for i in test_list:
    if i.startswith(pref):
        res.append(i)
print(res)

