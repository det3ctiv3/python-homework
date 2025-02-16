#1. Count Occurrences: Given a list and an element, find how many times the element appears in the list.
count_occurences = [1,2,3,4,51,1,2,2,2,4,5,6,6,7]
print(count_occurences.count(2))
#2. Sum of Elements: Given a list of numbers, calculate the total of all the elements.
print(sum(count_occurences))
#3. Max Element: From a given list, determine the largest element.
print(max(count_occurences))
#4. Min Element: From a given list, determine the smallest element.
print(min(count_occurences))
#5. Check Element: Given a list and an element, check if the element is present in the list.
print(51 in count_occurences)
#6. First Element: Access the first element of a list, considering what to return if the list is empty.
if count_occurences:
    print(count_occurences[0])
else:
    print("List is empty")
#7. Last Element: Access the last element of a list, considering what to return if the list is empty.
if count_occurences:
    print(count_occurences[-1])
else:
    print("List is empty")
#8. Slice List: Create a new list that contains only the first three elements of the original list.
first_three = count_occurences[:3]
print(first_three)
#9. Reverse List: Create a new list that contains the elements of the original list in reverse order.
reversed_list = count_occurences[::-1]
print(reversed_list)
#10. Sort List: Create a new list that contains the elements of the original list in sorted order.
sorted_list = sorted(count_occurences)
print(sorted_list)
#11. Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.
duplicates_removed = list(set(count_occurences))
print(duplicates_removed)
#12. Insert Element: Given a list and an element, insert the element at a specified index.

element_to_insert = 10
count_occurences.insert(3, element_to_insert)
print(count_occurences)
#13. Index of Element: Given a list and an element, find the index of the first occurrence of the element.
print(count_occurences.index(3))
#14. Check for Empty List: Determine if a list is empty and return a boolean.
if count_occurences:
    print(True)
else:
    print(False)

#15. Count Even Numbers: Given a list of integers, count how many of them are even.
count_even = 0
for occurence_even in count_occurences:
    if occurence_even %2 ==0:
       count_even+=1
print(f"There are {count_even} even numbers in the list")

#16. Count odd Numbers: Given a list of integers, count how many of them are odd.
count_odd = 0
for occurence_odd in count_occurences:
    if occurence_odd %2 !=0:
        count_odd+=1
print(f"There are {count_odd} odd numbers in the list")

#17. Concatenate Lists: Given two lists, create a new list that combines both lists.
new_list = [77,435,342,2,9,3,123,2,2]
concatenated_list = count_occurences + new_list
print(concatenated_list)

#18. Find Sublist: Given a list and a sublist, check if the sublist exists within the list.
cars_models = ["BMW", "Audi", "Mercedes", "Volvo", "Bentley"]
sublist = ["BMW", "Audi"]
if str(sublist)[1:-1] in str(cars_models):
    print("Sublist found")
else:
    print("Sublist not found")

#19. Replace Element: Given a list, replace the first occurrence of a specified element with another element.
cars_models[0] = "Genesis"
print(cars_models)
#20. Find Second Largest: From a given list, find the second largest element.
print(sorted(count_occurences)[-2])
#21. Find Second Smallest: From a given list, find the second smallest element.
print(sorted(count_occurences)[1])
#22. Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.
even_list =[]
for count_even in count_occurences:
    if count_even %2 ==0:
        even_list.append(count_even)
print(even_list)
#23. Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.
odd_list =[]
for count_odd in count_occurences:
    if count_odd %2 !=0:
        odd_list.append(count_odd)
print(odd_list)

#24. List Length: Determine the number of elements in the list.
print(len(count_occurences))
#25. Create a Copy: Create a new list that is a copy of the original list.
copy_list = count_occurences.copy()
print(copy_list)
#26. Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
middle_element = len(count_occurences)//2
print(count_occurences[middle_element])
#27. Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.
random_list = [1,2,3,4,5,6,7,8,9,10]
sublist_to_search = [3,4,5]
print(max(sublist_to_search))
#28. Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.
print(min(sublist_to_search))
#29. Remove Element by Index: Given a list and an index, remove the element at that index if it exists.
random_list.pop(3)
print(random_list)
#30. Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.
if sorted(count_occurences) == count_occurences:
    print(True)
else:
    print(False)
#31. Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.
list_to_repeat = [1,2,3,4,5]
number_of_repeats = 4
repeated_list = []

for i in list_to_repeat:
    repeated_num = i * number_of_repeats  # Multiply each element
    repeated_list.extend([i] * number_of_repeats)  # Store in the new list

print(repeated_list)

#32. Merge and Sort: Given two lists, create a new sorted list that merges both lists.
merge_list_first = [1,2,3,4,5]
merge_list_second = [6,7,8,9,10]
merge_list = sorted(merge_list_first + merge_list_second)
print(merge_list)


#33. Find All Indices: Given a list and an element, find all the indices of that element in the list.
index_list = [1,2,3,4,5,6,7,8,9,10]
indices = []
for i in range(len(index_list)):
    if index_list[i] == 5:
        indices.append(i)
print(indices)
#34. Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
rotated_list = [1,2,3,4,5,6,7,8,9,10]
rotated_list = rotated_list[1:] + rotated_list[:1]
print(rotated_list)
#35. Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).
range_list = list(range(1,11))
print(range_list)
#36. Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.
list_of_numbers = [1,2,-3,4,5,-6,7,8,-9,10]
list_of_positive_numbers = []
for element in list_of_numbers:
    if element >0:
        list_of_positive_numbers.append(element)
print(sum(list_of_positive_numbers))
#37. Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.
list_of_negative_numbers = []
for neg_element in list_of_numbers:
    if neg_element < 0:
        list_of_negative_numbers.append(neg_element)
print(sum(list_of_negative_numbers))

#38. Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
palindrome_list = [1,2,3,4,5,4,3,2,1]
if palindrome_list == palindrome_list[::-1]:
    print("List is a palindrome")
else:
    print("List is not a palindrome")

#39. Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
nested_list=[[1,2,3,4,5], [6,7,8,9,10]]
print(nested_list)
#40. Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.
list_unique_elements = [1,2,3,3,3,4,5,6,7,8,9,10]
unique_list =[]
for q in list_unique_elements:
    already_in_list = False
    for qwerty in unique_list:
        if q == qwerty:
            already_in_list = True
    if not already_in_list:
        unique_list.append(q)
print(unique_list)








