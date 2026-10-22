distance = float(input("Enter the distance to the obstacle in cm: "))

if distance < 0:
    print("Invalid distance!")
elif distance <= 10:
    print("STOP! Obstacle is too close.")
elif distance <= 30:
    print("WARNING! Obstacle nearby.")
else:
    print("SAFE. Distance is clear.")
