# Question 3
Starting with the string:

```python
famous_words = "seven years ago..."
```
Show two different ways to create a new string with "Four score and " prepended to the front of the string referenced by famous_words.

## My solution
### First way
```python
print("Four score and " + famous_words)
```

### Second way
```python
first_famous_words = "Four score and "
speech_intro = first_famous_words + famous_words
print(speech_intro)
```