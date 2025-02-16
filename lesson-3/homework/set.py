import random
#1. Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
first_set = {1, 2, 3, 4, 5}
second_set = {6, 6, 7, 8, 9, 10}
union_set = first_set.union(second_set)
print(union_set)

#2. Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.
intersection_set = first_set.intersection(second_set)
print(intersection_set)

#3. Difference of Sets: Given two sets, create a new set with elements from the first set that are not in the second.
difference_set = first_set.difference(second_set)
print(difference_set)
#4. Check Subset: Given two sets, check if one set is a subset of the other.
if_subset = first_set.issubset(second_set)
print(if_subset)
#5. Check Element: Given a set and an element, check if the element exists in the set.
element_if_exists = 6 in first_set
print(element_if_exists)
#6. Set Length: Determine the number of unique elements in a set.
unique_elements = len(first_set)
print(unique_elements)
#7. Convert List to Set: Given a list, create a new set that contains only the unique elements from that list.
list_to_set = [1,2,3,4,5,6,7,8,9,0]
set_from_list = set(list_to_set)
print(set_from_list)
#8. Remove Element: Given a set and an element, remove the element if it exists.
set_from_list = {1, 2, 3, 4, 5}  # Example set

try:
    set_from_list.remove(11)
except KeyError:
    print("Element not found in the set")

#9. Clear Set: Create a new empty set from an existing set.
clear_set = set_from_list.copy()
clear_set.clear()
print(clear_set)

#10. Check if Set is Empty: Determine if a set has any elements.
sample_set = {1, 2, 3}
is_empty = len(sample_set) == 0
print(is_empty)
#11. Symmetric Difference: Given two sets, create a new set that contains elements that are in either set but not in both.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
sym_diff = set1 ^ set2
print(sym_diff)
#12. Add Element: Given a set and an element, add the element to the set if it is not already present.
element = 7
if element not in sample_set:
    sample_set.add(element)
print(sample_set)

#13. Pop Element: Given a set, remove and return an arbitrary element from the set.

popped_element = sample_set.pop()
print(popped_element)

#14. Find Maximum: From a given set of numbers, find the maximum element.
print(max(sample_set))
#15. Find Minimum: From a given set of numbers, find the minimum element.
print(min(sample_set))

#16. Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.
even_set = {num for num in sample_set if num % 2 == 0}
print(even_set)

#17. Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.
odd_set = odd_set = {num for num in sample_set if num % 2 != 0}
print(odd_set)

#18. Create a Set of a Range: Create a set of numbers in a specified range (e.g., from 1 to 10).
range_set = set(range(1, 11))
print(range_set)

#19. Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged_set = set(list1 + list2)
print(merged_set)
#20. Check Disjoint Sets: Given two sets, check if they have no elements in common.
set3 = {1, 2, 3}
set4 = {4, 5, 6}
are_disjoint = set3.isdisjoint(set4)
print(are_disjoint)

#21. Remove Duplicates from a List: Given a list, create a set from it to remove duplicates, then convert back to a list.
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(dup_list))
print(unique_list)

#22. Count Unique Elements: Given a list, determine the count of unique elements using a set.
unique_count = len(set(dup_list))
print(unique_count)
#23. Generate Random Set: Create a set with a specified number of random integers within a certain range.
random_set = {random.randint(1, 100) for _ in range(5)}
print(random_set)

