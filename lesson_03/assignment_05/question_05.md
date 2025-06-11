# Question 5
What do you think the following code will output?

```python
nan_value = float("nan")

print(nan_value == float("nan"))
```
Bonus Question

How can you reliably test if a value is nan?

## My solution
```python
I think the code will output True, because nan_value is assigned "nan" passed to the float function, which results in the value of nan.

Bonus:
Use math.isnan().
```