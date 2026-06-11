"""
Write a Python script that accepts a temperature in Celsius and converts it to both Fahrenheit and Kelvin.
Ensure the script prints the results in a clean, human-readable statement.
Sample Input: Celsius: 25
Expected Output: 25°C is equivalent to 77.0°F and 298.15K
"""

temperature_celcius = int(input("Enter temperature in celcius: "))

temperature_fahrenheit = (temperature_celcius * 1.8) + 32

temperature_kelvin = temperature_celcius + 273.15

print(f"{temperature_celcius}°C is equivalent to {temperature_fahrenheit}°F and {temperature_kelvin}K")