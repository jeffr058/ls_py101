# Question 10
In Python, every object has a unique identifier that can be accessed using the id() function. This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime. For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value. This is known as "interning".

Given the following code, predict the output:


```python
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
```

## My solution
```python
My prediction is that the comparison operator == will cause the second comparison to be True == id(c). If so, the output should be False. 

However, I think id(c) will return the same identifier as id(a) and id(b).

# I was unfamiliar with chain comparisons, so my initial prediction was incorrect. But I was familiar enough with the concept of interning to have gotten it right if I looked at the comparison operators accurately.
```