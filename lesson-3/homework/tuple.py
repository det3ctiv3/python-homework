#1. Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
sample_tuple = (1, 2, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 8, 9, 10)
print(sample_tuple.count(4))
#2. Max Element: From a given tuple, determine the largest element.
print(max(sample_tuple))
#3. Min Element: From a given tuple, determine the smallest element.
print(min(sample_tuple))
#4. Check Element: Given a tuple and an element, check if the element is present in the tuple.
specified_num = 11
print(True if specified_num in sample_tuple else False)
#5. First Element: Access the first element of a tuple, considering what to return if the tuple is empty.
if sample_tuple:
    print(sample_tuple[0])
#6. Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
if sample_tuple:
    print(sample_tuple[-1])
#7. Tuple Length: Determine the number of elements in the tuple.
print(len(sample_tuple))
#8. Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
print(sample_tuple[:3])
#9. Concatenate Tuples: Given two tuples, create a new tuple that combines both.
first_tuple = (1, 2, 3)
seocnd_tuple = (4, 5, 6)
print(first_tuple + seocnd_tuple)
#10. Check if Tuple is Empty: Determine if a tuple has any elements.
print(bool(sample_tuple))
#11. Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
indexed_tuple = (1,2,3,4,5,5,5,5,6,7,8,9,10)
print(indexed_tuple.index(4))
#12. Find Second Largest: From a given tuple, find the second largest element.
sorted_tuple = sorted(sample_tuple)
print(sorted_tuple[-2])
#13. Find Second Smallest: From a given tuple, find the second smallest element.
print(sorted_tuple[1])
#14. Create a Single Element Tuple: Create a tuple that contains a single specified element.
single_element = (1)
print(single_element)
#15. Convert List to Tuple: Given a list, create a tuple containing the same elements.
list_to_tuple = [1,2,3,4,5]
print(tuple(list_to_tuple))
#16. Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
if sorted_tuple == sorted(sorted_tuple):
    print(True)
else:
    print(False)
#17. Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
tuple_to_search = (1,2,3,4,5,6,7,8,9,10)
subtuple_to_search = (3,4,5)
print(max(subtuple_to_search))

#18. Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.

print(min(subtuple_to_search))

#19. Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
element_to_remove = 7
element_to_remove_tuple = (1,2,3,4,5,6,7,8,9,10)
element_to_remove_list = list(element_to_remove_tuple)
if element_to_remove in element_to_remove_list:
    element_to_remove_list.remove(element_to_remove)
print(tuple(element_to_remove_list))

#20. Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
nested_tuple = ((1,2,3), (4,5,6), (7,8,9))
#21. Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
tuple_to_repeat = (1,2,3,4,5)
number_of_repeats = 4
repeated_tuple = ()
for i in tuple_to_repeat:
    repeated_tuple += (i,) * number_of_repeats
print(repeated_tuple)
#22. Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
range_tuple = tuple(range(1,11))
print(range_tuple)
#23. Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
reversed_tuple = tuple(reversed(range_tuple))
print(reversed_tuple)
#24. Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
palindrome_tuple = (1,2,3,4,5,4,3,2,1)
if palindrome_tuple == palindrome_tuple[::-1]:
    print("Tuple is a palindrome")
else:
    print("Tuple is not a palindrome")
#25. Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
sample_tuple = (1, 2, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10)
unique_list = []
for item in sample_tuple:
    if item not in unique_list:
        unique_list.append(item)

new_tuple = tuple(unique_list)
print(new_tuple)
