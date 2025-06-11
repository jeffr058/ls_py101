# Question 7
One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

```python
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"
```
After writing this function, he typed the following code:
```python
mess_with_demographics(munsters)
```
Before Grandpa could stop him, Spot hit the Enter key with his tail. Did the family's data get ransacked? Why or why not?

## My solution

The family's data did not get ransacked because within the loop block in the mess_with_demographics function, the the syntax for accessing the values for the keys "age" and "gender" is incorrect.

```python
# Correction: I was familiar with the concept of in-place modification of the mutable object (dictionary) but I incorrectly thought there was an error in how the values were being accessed. I didn't realize the values contained dictionaries themselves.

# The data does get ransacked because the munsters dictionary is mutable, so when it is passed to the function, the loop block modifies the same objects in memory of the nested dictionaries in each value that the global munsters variable points to.
```