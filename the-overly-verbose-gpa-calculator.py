def put_in_classes():
    classes = int(input("How many classes are you in? "))
    print(f"You are in {classes} classes.")
    return classes
def enter_grades(num_classes):
    grades = []
    for i in range(num_classes):
        grade = float(input(f"Enter grade {i+1} (0.0 - 4.0): "))
        grades.append(grade)
    return grades
num_classes = put_in_classes()
if num_classes == 0:
    print("Cannot calculate GPA with zero classes.")
    exit()
grades = enter_grades(num_classes)
overall_gpa = sum(grades) / len(grades)
print(f"Calculating... beep boop... Your current GPA is: {overall_gpa:.2f}")
analyze = input("Analyze First semester (1) or Second semester (2)? Enter 1 or 2: ")
half = num_classes // 2
if analyze == "1":
    semester_grades = grades[:half]
    semester_name = "First semester"
else:
    semester_grades = grades[half:]
    semester_name = "Second semester"
if semester_grades:
    semester_gpa = sum(semester_grades) / len(semester_grades)
    print(f"\n{semester_name} GPA: {semester_gpa:.2f}")
    print(f"Overall GPA: {overall_gpa:.2f}")
    if semester_gpa > overall_gpa:
        print(f"Nice! Your {semester_name.lower()} GPA is higher than your overall. You're trending upward!\n")
    elif semester_gpa < overall_gpa:
        print(f"Uh-oh! Your {semester_name.lower()} GPA is lower than your overall. Time to step it up!\n")
    else:
        print(f"Steady as she goes! Your {semester_name.lower()} GPA matches your overall.\n")
else:
    print(f"\nSkipping {semester_name} analysis: No grades to compare in that section.")
while True:
    try:
        goal_gpa = float(input("What's your goal GPA? "))
        if 0.0 <= goal_gpa <= 4.0:
            break
        else:
            print("Goal GPA must be between 0.0 and 4.0.")
    except ValueError:
        print("Invalid input. Please enter a number.")
if overall_gpa >= goal_gpa:
    print(f"\nCongratulations! You already met your goal GPA of {goal_gpa:.2f}")
else:
    possible = []
    for i, grade in enumerate(grades):
        new_gpa = (sum(grades) - grade + 4.0) / len(grades)
        if new_gpa >= goal_gpa:
            possible.append((i+1, grade, new_gpa))
    if possible:
        print(f"\nGood news! You can reach your goal of {goal_gpa:.2f} by improving just ONE grade:")
        for item in possible:
            print(f"- If you raise your grade in class {item[0]} from {item[1]:.2f} to 4.0, your GPA would be {item[2]:.2f}")
