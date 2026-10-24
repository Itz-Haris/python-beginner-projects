
def mm_to_cm(mm):
    return mm / 10

def mm_to_m(mm):
    return mm / 1000

def mm_to_km(mm):
    return mm / 1_000_000

print("=== Engineering Unit Converter ===")
print("Convert millimetres into other units.")

try:
    length = float(input("Enter length in millimetres: "))

    if length < 0:
        print("Error: Length cannot be negative.")
    else:
        print(f"Centimetres: {mm_to_cm(length)} cm")
        print(f"Metres: {mm_to_m(length)} m")
        print(f"Kilometres: {mm_to_km(length)} km")

except ValueError:
    print("Invalid input! Please enter a number.")
