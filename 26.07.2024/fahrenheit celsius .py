def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit = input()
print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C.")
