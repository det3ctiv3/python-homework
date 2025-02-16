# 1. Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
sample_dict = {"a": 1, "b": 2, "c": 3}
key_to_find = "d"
value = sample_dict.get(key_to_find, "Key not found")
print(value)

# 2. Check Key: Given a dictionary and a key, check if the key is present in the dictionary.
key_exists = "b" in sample_dict
print(key_exists)

# 3. Count Keys: Determine the number of keys in the dictionary.
num_keys = len(sample_dict)
print(num_keys)

# 4. Get All Keys: Create a list that contains all the keys in the dictionary.
keys_list = list(sample_dict.keys())
print(keys_list)

# 5. Get All Values: Create a list that contains all the values in the dictionary.
values_list = list(sample_dict.values())
print(values_list)

# 6. Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# 7. Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
key_to_remove = "b"
sample_dict.pop(key_to_remove, None)
print(sample_dict)

# 8. Clear Dictionary: Create a new empty dictionary.
empty_dict = {}
print(empty_dict)

# 9. Check if Dictionary is Empty: Determine if a dictionary has any elements.
is_dict_empty = not bool(sample_dict)
print(is_dict_empty)

# 10. Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.
key_to_find = "a"
pair = (key_to_find, sample_dict[key_to_find]) if key_to_find in sample_dict else "Key not found"
print(pair)

# 11. Update Value: Given a dictionary, update the value for a specified key.
sample_dict["a"] = 100
print(sample_dict)

# 12. Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.
value_to_count = 3
count_occurrences = list(sample_dict.values()).count(value_to_count)
print(count_occurrences)

# 13. Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
inverted_dict = {v: k for k, v in sample_dict.items()}
print(inverted_dict)

# 14. Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value.
value_to_search = 100
keys_with_value = [k for k, v in sample_dict.items() if v == value_to_search]
print(keys_with_value)

# 15. Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.
keys = ["x", "y", "z"]
values = [10, 20, 30]
dict_from_lists = dict(zip(keys, values))
print(dict_from_lists)

# 16. Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.
nested_dict = {"a": 1, "b": {"c": 3}, "d": 4}
has_nested = any(isinstance(v, dict) for v in nested_dict.values())
print(has_nested)

# 17. Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
nested_value = nested_dict.get("b", {}).get("c", "Not found")
print(nested_value)

# 18. Create Default Dictionary: Create a dictionary that provides a default value for missing keys.
from collections import defaultdict
default_dict = defaultdict(lambda: "Default Value")
default_dict["a"] = 5
print(default_dict["b"])

# 19. Count Unique Values: Given a dictionary, determine the number of unique values it contains.
unique_values_count = len(set(sample_dict.values()))
print(unique_values_count)

# 20. Sort Dictionary by Key: Create a new dictionary sorted by keys.
sorted_by_key = dict(sorted(sample_dict.items()))
print(sorted_by_key)

# 21. Sort Dictionary by Value: Create a new dictionary sorted by values.
sorted_by_value = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print(sorted_by_value)

# 22. Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
filtered_dict = {k: v for k, v in sample_dict.items() if v > 50}
print(filtered_dict)

# 23. Check for Common Keys: Given two dictionaries, check if they have any keys in common.
dict3 = {"x": 10, "y": 20, "z": 30}
dict4 = {"y": 25, "z": 35, "w": 45}
common_keys = set(dict3.keys()) & set(dict4.keys())
print(common_keys)

# 24. Create Dictionary from Tuple: Given a tuple of key-value pairs, create a dictionary from it.
tuple_of_pairs = (("a", 1), ("b", 2), ("c", 3))
dict_from_tuple = dict(tuple_of_pairs)
print(dict_from_tuple)

# 25. Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
first_pair = next(iter(sample_dict.items()), "Dictionary is empty")
print(first_pair)
