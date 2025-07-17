a = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
res=''
for i in a:
    res+=''.join(i)

print(res)

'''
''.join(sublist): Concatenates each element of sublist into a single string.
res += ''.join(sublist): This adds the resulting string to the final res string this building it up as we loop through the matrix.
'''