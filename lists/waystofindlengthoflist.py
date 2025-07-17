a = [10, 20, 30, 40, 50]
count=0
# print(len(a))
for i in a:
    print(i)
    count+=1

print(count)

'''
shallow copy= copied list references to the original list does not create new one 
whatever the changes makes that reflects on both

deepcopy= copied to new list whatever the changes makes that does not reflects on original
 '''