lst1=[1,2,3,4,4]
lst2=[7,8,9,0,1]
print(sorted(lst1))
print(lst1)

lst2.sort()
print(lst2)


unionofsets = list(set(lst1)|set(lst2))
unionofsets = list(set(lst1)& set(lst2))
print(len(unionofsets))


'''can't use union operator on list and tuples directly to use that convert into set 
    then use 
.sort() sorts the list in place and does not return anythingn and.
sorted sorts and returns the result
'''


