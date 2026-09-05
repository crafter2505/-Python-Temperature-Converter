**🌡️ Python Temperature Converter**
A clean, object-oriented Python temperature converter supporting Celsius, Fahrenheit, and Kelvin conversions. Built with best practices for both interactive use and module import.

**✨ Features**
Complete conversions between Celsius, Fahrenheit, and Kelvin

Object-oriented design with static methods

Interactive mode with input validation

Error handling for invalid inputs

Can be imported as a library

No external dependencies

🚀 Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/temperature-converter.git
```

# Navigate to directory
```bash
cd temperature-converter
```

# Run the converter
```python
python temperature_converter.py
```

💻 Usage

**Interactive Mode**

Run the script directly to use the interactive converter:

```bash
python temperature_converter.py
```
As a Module
```python
from temperature_converter import TemperatureConverter
```
# Convert using individual methods
```python
print(TemperatureConverter.celsius_to_fahrenheit(100))    # 212.0
print(TemperatureConverter.fahrenheit_to_celsius(32))     # 0.0
print(TemperatureConverter.celsius_to_kelvin(0))          # 273.15
```

# Universal converter
```pyhton
print(TemperatureConverter.convert(25, 'C', 'F'))         # 77.0
print(TemperatureConverter.convert(300, 'K', 'C'))        # 26.85
print(TemperatureConverter.convert(98.6, 'F', 'K'))       # 310.15
```
**📊 Supported Conversions**

From	To	Method

Celsius	Fahrenheit	celsius_to_fahrenheit()

Celsius	Kelvin	celsius_to_kelvin()

Fahrenheit	Celsius	fahrenheit_to_celsius()

Fahrenheit	Kelvin	fahrenheit_to_kelvin()

Kelvin	Celsius	kelvin_to_celsius()

Kelvin	Fahrenheit	kelvin_to_fahrenheit()

Any	Any	convert(temp, from_unit, to_unit)

**📐 Conversion Formulas**

C→ F: (C × 9/5) + 32

C → K: C + 273.15

F → C: (F - 32) × 5/9

F → K: (F - 32) × 5/9 + 273.15

K → C: K - 273.15

K → F: (K - 273.15) × 9/5 + 32

**🧪 Testing**
```python
# Quick test with known values
assert round(TemperatureConverter.celsius_to_fahrenheit(100), 2) == 212.0
assert round(TemperatureConverter.fahrenheit_to_celsius(32), 2) == 0.0
assert round(TemperatureConverter.celsius_to_kelvin(0), 2) == 273.15
print("All tests passed! ✅")
```
📁 Project Structure
```text
temperature-converter/
├── temperature_converter.py   # Main converter class
├── README.md                  # Documentation
└── LICENSE                    # MIT License
```
**🔧 Requirements**
Python 3.6 or higher

**📝 License**

MIT License - feel free to use in your own projects!

**⭐ Show Your Support**
If you found this helpful, please give it a star ⭐ on GitHub!
