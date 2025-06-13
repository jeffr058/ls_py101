# Question 5
What do you expect to happen when the greeting variable is referenced in the last line of the code below?


```python
if False:
    greeting = "hello world"

print(greeting)
```

## My solution
I think it will raise an error because the greeting variable will only be initialized if the condition in the if statement is truthy, and False is falsy.