def factor(n):
    n_counter = 0
    while n_counter <n:
        n_counter += 1
        if n % n_counter == 0 and n>0:
            print(f"{n_counter} is a factor of {n}")

try:
    n = int(input("Enter a positive number: "))
    factor(n)
except ValueError or NameError:
    print("Invalid input. Please enter a valid number.")