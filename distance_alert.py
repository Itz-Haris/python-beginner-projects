distance = float(input("Enter the distance to the obstacle in cm: "))

if distance < 0:
    print("Invalid distance!")
    
elif distance <= 10:
    print("CRITICAL! Obstacle is too close.")
    print("Action: STOP immediately.")

elif distance <= 30:
    print("WARNING! Obstacle nearby.")
    print("Action: Reduce speed.")

else:
    print("SAFE. Distance is clear.")
    print("Action: Continue moving.")
