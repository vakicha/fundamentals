import statistics

number_of_rows = int(input())
all_grades = {}
filtered_grades = {}
for incoming_data in range(number_of_rows):
    name = input()
    grade = float(input())
    if name not in all_grades:
        all_grades[name] = []
    all_grades[name].append(grade)
for student, grade in all_grades.items():
    mid_val = statistics.median(all_grades[student])
    if mid_val >= 4.5:
        filtered_grades[student] = mid_val
for student, grade in filtered_grades.items():
    print(f"{student} -> {grade:.2f}")
