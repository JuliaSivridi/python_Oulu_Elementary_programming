try:
    distance = float(input("Input distance traveled (m): "))
    time = float(input("Input elapse time (s): "))
except ValueError:
    print("You need less donuts, and more number inputting.")
else:
    if time == 0:
        print("Can't divide by zero.")
    else:   
        speed = 3.6 * distance / time
        print(f"The speed of a car traveling {distance:.2f} meters in {time:.2f} seconds "
              f"is {speed:.2f} km/h.")
