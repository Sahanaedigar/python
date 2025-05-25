a = ['Geeks', 'for', 'Geeks']
res=[]
for i in a:
    res.append(i[::-1])

'''
i[::-1] means:

start: default (from end)

stop: default (to start)

step: -1 (move backwards)
'''

print(res)

res=list(map(lambda x: x[::-1],a))

print(res)