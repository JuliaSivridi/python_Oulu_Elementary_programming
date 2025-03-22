UNITS = {
    "in": (2.54, "cm"),
    "\"": (2.54, "cm"),
    "ft": (30.48, "cm"),
    "'": (30.48, "cm"),
    "yd": (0.9144, "m"),
    "mi": (1.609344, "km"),
    "oz": (28.349523125, "g"),
    "lb": (0.45359237, "kg"),
    "cp": (2.365882365, "dl"),
    "pt": (4.73176473, "dl"),
    "qt": (0.946352946, "l"),
    "gal": (3.785411784, "l")    
}

def convert_to_si(measurement):
    value = measurement["value"]
    unit = measurement["unit"]
    try:
        # first item in the tuple is the factor
        si_value = value * UNITS[unit][0]
    except KeyError:
        measurement["invalid"] = True
    else:
        # second item in the tuple is the new unit
        measurement["unit"] = UNITS[unit][1]
        measurement["value"] = si_value

def read_measurements():
    print("Input measured values and units separated with spaces. Leave empty to quit.")
    measurements = []
    while True:
        value_unit = input("Input measurement: ").strip()
        if not value_unit:
            return measurements
        try:
            value, unit = value_unit.split(" ")
            value = float(value)
        except ValueError:
            print("Enter measurements in the specified format")
        else:
            measurements.append({
                "unit": unit,
                "value": value
            })

def print_measurements(measurements):
    for measurement in measurements:
        if measurement.get("invalid"):
            print("Invalid measurement {value:.3f} {unit}".format(**measurement))
        else:
            print("{value:.3f} {unit}".format(**measurement))
        
def main():
    measurements = read_measurements()
    for measurement in measurements:
        convert_to_si(measurement)
    print_measurements(measurements)
    
try:
    main()
except KeyboardInterrupt:
    print("Measurement processing interrupted")
