# Question 9
Print a new version of the sentence given by advice that ends just before the word house. Don't worry about spaces or punctuation: remove everything starting from the beginning of house to the end of the sentence.

```python
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
```

## My solution
```python
advice_list = advice.split()
new_advice = ' '.join(advice_list[0:8])
print(new_advice)
```