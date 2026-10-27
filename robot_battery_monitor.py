def check_battery(level):
    if level == 0:
        return "BATTERY EMPTY - Robot cannot operate."
    elif level < 30:
        return "LOW BATTERY - Please charge the robot."
    elif level < 80:
        return "Battery moderate - Charging recommended."
    else:
        return "Battery healthy - Robot ready."


print("=== Robot Battery Monitor ===")

try:
    battery = int(input("Enter battery level (0-100): "))

    if battery < 0 or battery > 100:
        print("Invalid input! Enter a value from 0 to 100.")
    else:
        print(check_battery(battery))

except ValueError:
    print("Invalid input! Please enter a whole number.")
