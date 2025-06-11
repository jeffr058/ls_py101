# Question 6
What is the output of the following code?


```python
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)
```

## My solution
```python
I think the output of the code will be 34 as a result of subtracting 8 from the answer variable, which was initialized by being assigned 42 as its value. When answer is passed to the mess_with_it function, which is called when assigned to new_answer, answer inside the function is a local variable, meaning the function does not modify answer in the global scope.
```