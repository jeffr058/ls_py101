# Question 3
Given the following similar sets of code, what will each code snippet print?


A)
```python
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

B)
```python
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

C)
```python
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

## My solution
(A)
These will print: 

one is: ["one"]
two is: ["two"]
three is: ["three"]

because inside the function body, each of these variables are being assigned something, making them shadow the global variables of the same names, therefore separate and contained inside the function.

(B)
These will print:

one is: ["one"]
two is: ["two"]
three is: ["three"]

because inside the function body, each of these variables are being assigned something, making them shadow the global variables of the same names, therefore separate and contained inside the function.

(C)
These will print:

one is: ["two"]
two is: ["three"]
three is: ["one"]

because in the function body, the global variables passed as arguments are having their element at index position 0 reassigned. The string object within each list is a reference to the same object in memory for the global and local list variables.

```python

```