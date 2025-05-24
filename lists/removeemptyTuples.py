a = [(1, 2), (), (3, 4), (), (5,),0,1]
res=[]
for i in a:
    if i:
        res.append(i)
# print(res)


#print duplicate number in the list

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
# a=['s','a','h','a','n','a']
s=set()
dup=[]

for i in a:
    if i in s:
        dup.append(i)
    else:
        s.add(i)
# print(dup)
# print(s)


#add two lists
a = [1, 2, 3]
b = [4, 5, 6]

# Add all elements from list 'b' to the end of list 'a'
# a.extend(b)
# print(a)

#OR

# print(a+b)

#OR
res=[]
for i in a:
    res.append(i)
for i in b:
    res.append(i)

print(res)

'''
enumerate :In Python, enumerate() is a built-in function used to loop over an iterable while
 keeping track of the index.

enumerate(iterable, start=0)
iterable: Any iterable (like a list, tuple, string, etc.)
start: The index to start counting from (default is 0)
'''
fruits = ['apple', 'banana', 'cher  ry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

print(list(enumerate(fruits)))

#avg of list
a=[1,2,4,5]
b=[1,2]
avg=sum(a)/len(a)
print(avg)
# a.append(10)
# print(a)
a.insert(1,10)
print(a)
a.sort(reverse=True)
print(a[1])

#intersection of 2 lists

print(a and b)
print(a or b)

