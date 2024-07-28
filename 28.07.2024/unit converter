def unit_converter():
    def km_to_miles(km):
        return km * 0.621371

    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    while True:
        print("\nUnit Converter:")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            km = float(input("Enter kilometers: "))
            print(f"{km} km is {km_to_miles(km)} miles.")
        elif choice == '2':
            c = float(input("Enter Celsius: "))
            print(f"{c}°C is {celsius_to_fahrenheit(c)}°F.")
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")

unit_converter()
