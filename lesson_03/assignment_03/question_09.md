# Question 9
We have most of the Munster family in our ages dictionary:


```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
```

Add entries for Marilyn and Spot to the dictionary:


```python
additional_ages = {'Marilyn': 22, 'Spot': 237}
```

## My solution
```python
# manually
ages['Marilyn'] = 22
ages['Spot'] = 237

# update method
ages.update(additional_ages)
```