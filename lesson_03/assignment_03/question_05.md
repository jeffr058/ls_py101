# Question 5
How would you verify whether the data structures assigned to the variables numbers and table are of type list?


```python
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
```

## My solution
```python
# Use isinstance():
isinstance(numbers, list)
isinstance(table, list)

# Check what the type is:
type(numbers)
type(table)
```