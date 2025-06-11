# Question 9
Consider these two simple functions:

```python
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")
```
What will the following function invocation return?

```python
bar(foo())
```

## My solution

The function invocation will return False. 

The function foo, with no arguments passed to it, is given the default parameter value of "no", but in the function body, the value "yes" in the return statement will be returned regardless of the argument passed to foo(). 

The "yes" argument returned by foo() is passed to bar(). In the body of bar(), the comparison operator and checks the first operand, and seeing that the argument "yes" is not equal to "no", the operator short-circuits the evaluation and returns False, which is then returned by bar().