# Question 4
What will the following code output?


```python
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
```
Try to answer without running the code.


## My solution
```python
I think print(my_list1) will output 

[{"first": 42}, {"second": "value2"}, 3, 4, 5]

because the copy method creates a shallow copy of my_list1 where the topmost level (the list object my_list2) is a different object but the inner levels refer to the same objects, so if the dictionary object is mutated by my_list2, the same mutated dictionary object will be referred to by my_list1.
```