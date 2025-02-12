#1
username = input("Enter your username: ")
password = input("Enter your password: ")
if not username or not password:
    print("Empty")

#2
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
if first_num == second_num:
    print("True")

#3
rand_num1 = int(input("Enter a random number: "))
if rand_num1 > 0 and rand_num1 %2 ==0:
    print(True)

#4
rand_num2 = int(input("Enter a random number: "))
rand_num3 = int(input("Enter a random number: "))
rand_num4 = int(input("Enter a random number: "))
if rand_num2 != rand_num3 and rand_num2 != rand_num4 and rand_num3 != rand_num4:
    print("True")

#5
rand_str = input("Enter a random text: ")
rand_str2 = input("Enter a random text: ")
if len(rand_str) == len(rand_str2):
    print("True")

#6
rand_num5 = int(input("Enter a random number: "))
if rand_num5 %3 == 0 and rand_num5 %5 == 0:
    print("True")

#7
first_num = int(input("Enter a random number: "))
second_num = int(input("One more: "))
sum = first_num + second_num
if sum > 50.8:
    print("True")

#8
third_num = int(input("Enter a random number: "))
if 10 <= third_num <=20:
    print("True")





