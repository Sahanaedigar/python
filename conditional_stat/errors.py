
# TypeError: 'int' object is not iterable means
'''
The error TypeError: 'int' object is not iterable means 
you're trying to loop through (or unpack) an integer, which is not allowed because 
integers are not iterable (unlike lists, strings, tuples, etc.).


for i in 10:
    print(i)
Error:

TypeError: 'int' object is not iterable
Here, 10 is an integer — not something you can iterate over with a for loop.

✅ Correct Example:
If you want to loop 10 times, use range(10) which is iterable:

for i in range(10):
    print(i)
    '''


#TypeError: 'str' object cannot be interpreted as an integer


'''The error TypeError: 'str' object cannot be interpreted as
an integer occurs when you try to use a string in a context that expects an integer,
 such as inside a range() function or for indexing.

🔍 Common Cause:You likely forgot to convert input from string to int.

❌ Example That Causes This Error:

n = input("Enter a number: ")  # input() always returns a string
for i in range(n):             # ❌ TypeError here
    print(i)
Error:

TypeError: 'str' object cannot be interpreted as an integer

✅ Correct Version:

n = int(input("Enter a number: "))  # Convert to integer
for i in range(n):
    print(i)'''