# Question 6
What will the following code print and why? Don't run it until you have tried to answer.

```python
def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()
```

## My solution
The code will print the following because where inner_funt1() accesses and prints the value of the x variable that is in its local scope, inner_func2() accesses and prints the x variable that is in the outer scope.

Inner 1: 25
Inner 2: 15