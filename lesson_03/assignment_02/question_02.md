# Question 2
How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or False depending on whether the string ends with an exclamation mark.

```python
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
```

## My solution
```python
def ends_in_exclamation(string):
  if string[-1] == '!':
    return True
  else:
    return False
    
print(ends_in_exclamation(str1))
print(ends_in_exclamation(str2))
```