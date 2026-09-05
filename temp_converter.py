class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
    @staticmethod
    def fahrenheit_to_kelvin(f):
        return (f - 32) * 5/9 + 273.15
    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15
    @staticmethod
    def kelvin_to_fahrenheit(k):
        return (k - 273.15) * 9/5 + 32

    @staticmethod
    def converter(temp, from_unit, to_unit):
        if from_unit.lower() in ['c', 'celcius']:
            celsius = temp
        elif from_unit.lower() in ['f', 'fahrenheit']:
            celsius = TemperatureConverter.fahrenheit_to_celsius(temp)
        elif from_unit.lower() in ['k', 'kelvin']:
            celsius = TemperatureConverter.kelvin_to_celsius(temp)
        else:
            raise ValueError(f"Invalid unit: {from_unit}. Supported units are 'C', 'F', 'K'.")


        if to_unit.lower() in ['c', 'celcius']:
            return celsius
        elif to_unit.lower() in ['f', 'fahrenheit']:
            return TemperatureConverter.celsius_to_fahrenheit(celsius)
        elif to_unit.lower() in ['k', 'kelvin']:
            return TemperatureConverter.celsius_to_kelvin(celsius)
        else:
            raise ValueError(f"Invalid unit: {to_unit}. Supported units are 'C', 'F', 'K'.")

def interactive_converter():
    print("=" * 40)
    print("      Temperature Converter")
    print("=" * 40)
    print("\nAvailable unites: C (Celsius), F (Fahrenheit), K (Kelvin)\n")

    while True:
        print("\n" + "-" * 40)
        from_unit = input("Enter the unit to convert from (C/F/K) or 'Q' to quit: ").upper()
        if from_unit == 'Q':
            print("Exiting the converter. Goodbye!")
            break
        if from_unit not in ['C', 'F', 'K']:
            print("Invalid unit. Please enter C, F, or K.")
            continue
        try:
            temp = float(input(f"Enter temerature in {from_unit}: "))
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue
        to_unit = input("To unit (C/F/K): ").upper()
        if to_unit not in ['C', 'F', 'K']:
            print("Invalid unit. Please enter C, F, or K.")
            continue
        try:
            result = TemperatureConverter.converter(temp, from_unit, to_unit)
            print(f"{temp} {from_unit} is equal to {result:.2f} {to_unit}.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    interactive_converter()
        
