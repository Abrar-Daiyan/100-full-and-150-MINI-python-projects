# 1. **Temperature Converter** (Celsius ↔ Fahrenheit)  

print("Temperature Converter (Celsius ↔ Fahrenheit)")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "°C is equal to", fahrenheit, "°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(fahrenheit, "°F is equal to", celsius, "°C")
else:
    print("Invalid choice! Please enter 1 or 2.")
