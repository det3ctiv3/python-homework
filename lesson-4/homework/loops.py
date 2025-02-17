import random

#1. Return uncommon elements of lists. Order of elements does not matter.

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1,3,4,5]
not_in_list1 = (x for x in list1 if x not in list2) #checks if element in list1 does not exist in list2
not_in_list2 = (x for x in list2 if x not in list1) #same, but vice versa
uncommon_elements_list = list(not_in_list1) + list(not_in_list2) #adds two results to get unique elements from both lists
print(uncommon_elements_list)

#2. Print the square of each number which is less than n on a separate line.
n=5
for i in range(1, n): # iterates until reaches <5
    print(i**2)

#3. Task 3
txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'aeiouAEIOU'
output = ''
count = 0
for letter in range(len(txt)):
   count +=1
   output += txt[letter]

   if count %3 == 0 and txt[letter] not in vowels and letter != len(txt)-1:
       output += '_'
print(output)

#4. Number Guessing Game. Creating a simple number guessing game.
while True:
    random_number = random.randint(1, 100)  # Random number between 1 and 100
    count = 0  # Initialize count to track the number of tries

    while count < 10:  # Allow the user to guess up to 10 times
        user_number = int(input("Guess a number between 1 and 100: "))
        count += 1  # Increment the number of tries

        if user_number == random_number:
            print(f"You guessed the number in {count} tries!")
            break
        elif user_number < random_number:
            print("Too low!")
        else:
            print("Too high!")

    # If the user reaches 10 tries
    if count == 10:
        print("Sorry, you've exceeded 10 tries.")

    # Ask if the user wants to play again
    wants_to_play_again = input("Do you want to play again? (yes/no): ")
    if wants_to_play_again.lower() == "no":
        print("Thanks for playing!")
        break



#5. Password Checker Task: Create a simple password checker.
password = input("Please, set your password: ")
while True:
    if len(password) >=8:
        if any(x.isupper() for x in password):
            print("Password is strong!")
        else:
            print("Password must contain an uppercase letter.")
    else:
        print("Password is too short")
    break


#6.Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.
for num in range(1, 101):
    if num <= 1:
        continue
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)






