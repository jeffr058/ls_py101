# Question 2
Alan wrote the following function, which was intended to return all of the factors of number:


```python
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
```
Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.

Bonus Question: What is the purpose of number % divisor == 0 in that code?


## My solution
He can have a separate if statement block that decrements by 1 toward 0 when the divisor is positive and increments by 1 toward 0 when the divisor is negative.

```python
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        if divisor > 0:
            divisor -= 1
        elif divisor < 0:
            divisor += 1
    return result
```

Bonus: The purpose of number % divisor == 0 is to capture the divisor as a factor if dividing number by the divisor results in a remainder of 0, because the divisor is a factor of number.