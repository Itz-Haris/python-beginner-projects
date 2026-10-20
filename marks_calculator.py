
print("=== Student Marks Calculator ===")

name = input("Enter your name: ")

subjects = ["EM3", "SMRA", "SMM", "C Programming"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter your {subject} marks (out of 100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
average = total / len(subjects)

print("\n--- Your Results ---")
print("Student:", name)
print(f"Total Marks: {total:.2f} / 400")
print(f"Average: {average:.2f}%")

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
