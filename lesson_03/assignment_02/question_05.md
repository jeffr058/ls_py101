# Question 5
Starting with the string:

```python
munsters_description = "The Munsters are creepy and spooky."
```

print the string with the case of all letters swapped:

```python
"tHE mUNSTERS ARE CREEPY AND SPOOKY."
```

That is, lowercase letters are converted to uppercase, and uppercase letters are converted to lowercase"

## My solution
```python
my_list = []
for char in munsters_description:
  if char == char.upper():
    my_list.append(char.lower())
  else:
    my_list.append(char.upper())
reverse_case_munsters = ''.join(my_list)
print(reverse_case_munsters)

# Second solution
swapcase_munsters = munsters_description.swapcase()
print(swapcase_munsters)
```