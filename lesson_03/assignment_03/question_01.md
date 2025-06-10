# Question 1
Write two distinct ways of reversing the list without mutating the original list.


```python
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
```

## My solution
```python
# First way
list(reversed(numbers))

# Second way
numbers[::-1]
```