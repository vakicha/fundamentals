data = input()
courses_students = {}
while data != "end":
    course_name, student = data.split(' : ')
    if course_name not in courses_students:
        courses_students[course_name] = []
    courses_students[course_name].append(student)
    data = input()
for each_course in courses_students:
    print(f"{each_course}: {len(courses_students[each_course])}")
    for stud in courses_students[each_course]:
        print(f"-- {stud}")
