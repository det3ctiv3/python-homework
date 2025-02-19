def convert_cel_to_far(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def convert_far_to_cel(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


while True:
    try:
        # Fahrenheit to Celsius Conversion
        fahrenheit = float(input("Enter temperature in Fahrenheit (or type 'exit' to quit): "))
        if fahrenheit < -459.67:
            print("Temperature cannot be below absolute zero (-459.67°F). Try again.")
            continue

        celsius = convert_far_to_cel(fahrenheit)
        print(f"{fahrenheit}°F == {round(celsius, 2)}°C")

        # Celsius to Fahrenheit Conversion
        celsius = float(input("Enter temperature in Celsius (or type 'exit' to quit): "))
        if celsius < -273.15:
            print("Temperature cannot be below absolute zero (-273.15°C). Try again.")
            continue

        fahrenheit = convert_cel_to_far(celsius)
        print(f"{celsius}°C == {round(fahrenheit, 2)}°F")

    except ValueError:
        print("Invalid input. Please enter a valid number or type 'exit' to quit.")
        break
