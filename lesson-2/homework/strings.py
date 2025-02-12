#1
# birth_year = int(input("Enter birth year: "))
# print(f"You are {2025-birth_year} years old.")
#2
txt = 'LMaasleitbtui'

# 1. Take a string input from the user
user_input = input("Enter a string: ")

# 2. Print the length of the string
print("Length of the string:", len(user_input))

#3
print("Uppercase:", user_input.upper())
print("Lowercase:", user_input.lower())

#4
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#5
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in user_input if char in vowels)
consonant_count = sum(1 for char in user_input if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

#6
sub_string = input("Enter a substring to check: ")
print("Substring found!" if sub_string in user_input else "Substring not found.")

#7
sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
print("Modified sentence:", sentence.replace(word_to_replace, new_word))

#8
print("First character:", user_input[0], "Last character:", user_input[-1])

#9
print("Reversed string:", user_input[::-1])

#10
print("Word count:", len(sentence.split()))

#11
print("Contains digits?", any(char.isdigit() for char in user_input))

#12
words = input("Enter words separated by spaces: ").split()
separator = input("Enter a separator: ")
print("Joined string:", separator.join(words))

#13
print("String without spaces:", user_input.replace(" ", ""))

#14
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Strings are equal!" if str1 == str2 else "Strings are not equal.")

#15
acronym_sentence = input("Enter a sentence for acronym: ")
acronym = "".join(word[0].upper() for word in acronym_sentence.split())
print("Acronym:", acronym)

#16
char_to_remove = input("Enter character to remove: ")
print("String without character:", user_input.replace(char_to_remove, ""))

#17
symbol = input("Enter a symbol to replace vowels: ")
replaced_vowels = ''.join(symbol if char in vowels else char for char in user_input)
print("Modified string:", replaced_vowels)

#18
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")
print("Starts and ends correctly!" if user_input.startswith(start_word) and user_input.endswith(
    end_word) else "Does not match criteria.")
