name = input("Enter student name: ")
marks = int(input("Enter marks (0–100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
