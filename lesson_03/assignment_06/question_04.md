# Question 4
Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.

Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:

```python
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True
```

Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

Help Ben fix his code.

## My solution
I added an if statement that will return false if the list of numeric strings does not equal 4 elements.

```python
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    
    if len(dot_separated_words) != 4:
      return False

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False  # I didn't realize that break would cause the returned value to be True even if an invalid value was flagged

    return True

# Correction: my code for Alyssa's function was incomplete. I didn't look at the helpful code until after committing my first attempt at this exercise.
```