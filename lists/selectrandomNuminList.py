'''
Using random.choice()
random.choice() picks an element at random without any need for indexing,
 making it ideal for quick selections. This method is fast and widely used when you need to 
 randomly pick one item from a collection.
 
 

Using secrets.choice()
secrets.choice() is part of the secrets module, designed for cryptographic applications where security is important.
 It provides a randomly 
chosen element from a list using a cryptographically secure method, making it more secure than random.choice().

 '''

import random
a=[1,5,7,0,9]
res=random.choice(a)
print(res)

import secrets
a = [1, 4, 5, 2, 7]
res = secrets.choice(a)
print(res)