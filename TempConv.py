def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return value

    # Convert input to Celsius first
    if from_unit == "F":
        value = (value - 32) * 5 / 9
    elif from_unit == "K":
        value = value - 273.15
    elif from_unit != "C":
        raise ValueError("Invalid from_unit. Use C, F, or K.")

    # Convert from Celsius to target unit
    if to_unit == "F":
        return (value * 9 / 5) + 32
    elif to_unit == "K":
        return value + 273.15
    elif to_unit == "C":
        return value
    else:
        raise ValueError("Invalid to_unit. Use C, F, or K.")

def main():
    print("🔥 Temperature Converter 🔥")
    print("Convert between Celsius (C), Fahrenheit (F), and Kelvin (K)")

    try:
        value = float(input("Enter temperature value: "))
        from_unit = input("Convert from (C/F/K): ")
        to_unit = input("Convert to (C/F/K): ")

        result = convert_temperature(value, from_unit, to_unit)
        print(f"\n✅ {value}°{from_unit.upper()} = {result:.2f}°{to_unit.upper()}")
    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
