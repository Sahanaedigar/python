nums = [2, 2, 1]

hashmap = {}
for num in nums:
    if num in hashmap:
        hashmap[num] += 1
    else:
        hashmap[num] = 1

for key in hashmap:
    if hashmap[key] == 1:
        print(key)
        break

print(hashmap)
