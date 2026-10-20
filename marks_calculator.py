print("=== Student Marks Calculator ===")

name = input("Enter your name: ")

em3 = float(input("Enter your EM3 marks (out of 100): "))
smra = float(input("Enter your SMRA marks (out of 100): "))
smm = float(input("Enter your SMM marks (out of 100): "))
cprogramming = float(input("Enter your C Programming marks (out of 100): "))

total = em3 + smra + smm + cprogramming
average = total / 4

print("\n--- Your Results ---")
print("Student:", name)
print("Total Marks:", total, "/ 400")
print(f"Average: {average:.2f}%")

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
