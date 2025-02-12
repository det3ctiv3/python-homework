
#1
float_number = float(input("Enter a float number: "))
print(round(float_number))

#2
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))
if first_number > second_number and first_number > third_number:
    print(f"The largest number is {first_number}.")
elif second_number > first_number and second_number > third_number:
    print(f"The largest number is {second_number}.")
else:
    print(f"The largest number is {third_number}.")

#3
a4 = float(input("Input km: "))
print(a4 * 1000, "Meters and ", a4 * 1000000, "centimetres")

#4
rand_num = int(input("Input a random number: "))
rand_num2 = int(input("Input a random number: "))
print(divmod(rand_num, rand_num2))

#5
celsius = float(input("Input celsius: "))
farenheit = (celsius *9/5) + 32
print(farenheit)

#6
random_number = int(input("Input a random number: "))
print(random_number%10)

#7
random_number_7 = int(input("Input a random number: "))
if (random_number_7%2 == 0):
    print("Even")
else:
    print("Odd")


