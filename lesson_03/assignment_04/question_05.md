# Question 5
The following function unnecessarily uses two return statements to return boolean values. Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?


```python
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
```
Try to come up with two different solutions.


## My solution
```python
# First way
def is_color_valid(color):
  colors = ['blue', 'green']
  return color in colors

# Second way
def is_color_valid(color):
    return color == 'blue' or color == 'green' 
```