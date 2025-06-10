# Question 3
What will the following code output?


```python
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
```
Try to answer without running the code.


## My solution
```python
The code will output "hello there" because assigning "goodbye!" to str2 reassigns the value for str2, not str1. str1 continues to point to the same object in memory.
```