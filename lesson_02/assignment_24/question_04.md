# Question 4
What will the following code print and why? Don't run it until you have tried to answer.

```python
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()
```

## My solution
The code will print Hello World.

When invoked by outer(), inner() accesses and prints outer_var along with locally initialized inner_var. When outer() is invoked, print() prints its arguments as a string.