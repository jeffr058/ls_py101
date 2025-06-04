# Question 3
What will the following code print and why? Don't run it until you have tried to answer.

```python
num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)
```

## My solution
The code will print 10 because the invoked function accesses the global num variable and reassigns it globally to 10.