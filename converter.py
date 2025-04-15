def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "C":
        if to_unit == "F":
            return celsius_to_fahrenheit(value)
        elif to_unit == "K":
            return celsius_to_kelvin(value)
    elif from_unit == "F":
        if to_unit == "C":
            return fahrenheit_to_celsius(value)
        elif to_unit == "K":
            return fahrenheit_to_kelvin(value)
    elif from_unit == "K":
        if to_unit == "C":
            return kelvin_to_celsius(value)
        elif to_unit == "F":
            return kelvin_to_fahrenheit(value)

def main():
    print("Temperature Converter")
    print("Available units: C (Celsius), F (Fahrenheit), K (Kelvin)")
    
    try:
        value = float(input("Enter the temperature value: "))
        from_unit = input("Convert from (C/F/K): ").upper()
        to_unit = input("Convert to (C/F/K): ").upper()

        if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
            print("Invalid unit entered.")
            return
        
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value}°{from_unit} is {result:.2f}°{to_unit}")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
