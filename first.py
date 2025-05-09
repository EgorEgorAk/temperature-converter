while True:
    t = input("Enter: 'C' - Celsius, 'F' - Fahrenheit, 'K' - Kelvin, 'Q' - quit: ").lower()
    if t == 'q':
        print("Exiting the program.")
        break
    try:
        temperature = float(input("Enter the temperature value: "))

        if t == "c":
            print(f'\nTemperature in Fahrenheit = {(temperature * 9/5) + 32:.2f} F')
            print(f'Temperature in Kelvin = {temperature + 273.15:.2f} K\n')
        elif t == "f":
            print(f'\nTemperature in Celsius = {((temperature - 32) * 5/9):.2f} C')
            print(f'Temperature in Kelvin = {(((temperature - 32) * 5/9) + 273.15):.2f} K\n')
        elif t == "k":
            print(f'\nTemperature in Celsius = {(temperature - 273.15):.2f} C')
            print(f'Temperature in Fahrenheit = {(((temperature - 273.15) * 9/5) + 32):.2f} F\n')
        else:
            print("Invalid input! Please enter only 'C', 'F', 'K', or 'Q'.\n")

    except ValueError:
        print("Error: please enter a valid numeric temperature.\n")