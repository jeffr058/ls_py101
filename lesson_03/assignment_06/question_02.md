# Question 2
What does the last line in the following code output?


```python
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
```
Try to answer without running the code or looking at the solution.


## My solution
The code starts with a variable dictionary initialized with a dictionary that has one key/value pair, with the key a string 'first' and the value a list [1]. That is followed by a variable num_list initialized with the dictionary variable that is followed by the key 'first' in square brackets, or dictionary['first'], meaning the value of key 'first', which is [1], is being assigned to this new num_list variable, making num_list a list with one element [1]. Then, the append method appends the value 2 to num_list. The first print call, print(num_list), will output [1, 2].

I think the last line, print(dictionary) will print {'first': [1, 2]} because the in-place modification to num_list by the append method mutates the same list object in memory that the list dictionary value references.