'''You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.
'''
def cat_hat(input):
    catcount=input.count('cat')
    hatcount=input.count('hat')
    if catcount==hatcount:
        return True
    else:
        return False

    
st=input().lower()
print(cat_hat(st))
    
