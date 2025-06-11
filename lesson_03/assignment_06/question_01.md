# Question 1
Will the following functions return the same results?


```python
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())
```
Try to answer without running the code or looking at the solution.


## My solution
We are defining a function named first with no parameters, and in its body it returns a dictionary object with key 'prop1' and value "hi there". When called, first() will return the key/value pair from the dictionary.

We are defining another function named second with no parameters, and in its body it returns a dictionary with the same key/value pair, but the dictionary, including the curly braces it is wrapped in, is on the next line down from the return statement.

I think passing first() into print will return {'prop1': "hi there"}.
I think passing second() into print will raise a SyntaxError because the dictionary should be, or at least start, following return on the same line for the function to return its value.
```python
# Correction: My guess for second() was wrong. Having return by itself with cause the function to return None. Since the function will terminate after the return statement, the code following the line with the return statement is unreachable.
```