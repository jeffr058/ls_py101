# Question 2
What will the following code print and why? Don't run it until you have tried to answer.

```python
num = 5

def my_func():
    num = 10

my_func()
print(num)
```

## My solution
The code will print 5 because the num inside the function shadows the num in the global scope, and is only accessible inside the function. When num prints, the global num is being printed.