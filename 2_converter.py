def length():
    print("Select unit of length from the options below using the abreviations")
    print("Inch (in or \")")
    print("Foot (ft or ')")
    print("Yard (yd)")
    print("Mile (mi)")
    unit = input("Input source unit: ")
    value = float(input("Input value to convert: "))
    if unit == "in" or unit == "\"":
        si_value = value * 2.54
        print(f"{value:.2f}\" is {si_value:.2f} cm")
    elif unit == "ft" or unit == "'":
        si_value = value * 39.48
        print(f"{value:.2f}' is {si_value:.2f} cm")
    elif unit == "yd":
        si_value = value * 0.9144
        print(f"{value:.2f} yd is {si_value:.2f} m")
    elif unit == "mi":
        si_value = value * 1.609344
        print(f"{value:.2f} mi is {si_value:.2f} km")
    else:
        print("The selected unit is not supported")

def mass():
    print("Select unit of mass from the options below using the abreviations")
    print("Ounce (oz)")
    print("Pound (lb)")
    unit = input("Input source unit: ")
    value = float(input("Input value to convert: "))
    if unit == "oz":
        si_value = value * 28.349523125
        print(f"{value:.2f} oz is {si_value:.2f} g")
    elif unit == "lb":
        si_value = value * 0.45359237
        print(f"{value:.2f} lb is {si_value:.2f} kg")
    else:
        print("The selected unit is not supported")

def volume():
    print("Select unit of mass from the options below using the abbreviations")
    print("Cup (cp)")
    print("Pint (pt)")
    print("Quart (qt)")
    print("Gallon (gal)")
    unit = input("Input source unit: ")
    value = float(input("Input value to convert: "))
    if unit == "cp":
        si_value = value * 2.365882365
        print(f"{value:.2f} cp is {si_value:.2f} dl")
    elif unit == "pt":
        si_value = value * 4.73176473
        print(f"{value:.2f} pt is {si_value:.2f} dl")
    elif unit == "qt":
        si_value = value * 0,94635295
        print(f"{value:.2f} qt is {si_value:.2f} l")
    elif unit == "gal":
        si_value = value * 3.785411784
        print(f"{value:.2f} gal is {si_value:.2f} l")
    else:
        print("The selected unit is not supported")

def temperature():
    print("Temperature conversion from Fahrenheit to Celsius.")
    fahrenheit = float(input("Input temperature: "))
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"{fahrenheit:.2f} °F is {celsius:.2f} °C")

print("This program converts US customary units to SI units")
print("Available features:")
print("(L)ength")
print("(M)ass")
print("(V)olume")
print("(T)emperature")
print()
choice = input("Make your choice: ").strip().lower()
if choice == "l" or choice == "length":
    length()
elif choice == "m" or choice == "mass":
    mass()
elif choice == "v" or choice == "volume":
    volume()
elif choice == "t" or choice == "temperature":
    temperature()
else:
    print("The selected feature is not available")
