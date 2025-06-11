# Question 3
Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.

She wrote two implementations of the code for adding elements to the buffer:


```python
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer
```
What is the key difference between these implementations?


## My solution
```python
The first implementation adds new_element through the append method, mutating the list buffer by adding new_element as a single object.

The second implementation adds new_element as a new element to the list buffer through list concatenation. This creates a new list that is assigned to the existing variable buffer. If new_element has nested elements, those elements are added to the top level of the new list that is created.
```