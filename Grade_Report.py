def get_letter_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

def main():
    student_count = int(input("Student count: "))
    grades = {}
    
    for _ in range(student_count):
        name, grade = input("Name and grade: ").split()
        grades[name] = int(grade)

    print("Student Grades:")
    for name, grade in grades.items():
        print(f"{name}: {grade} ({get_letter_grade(grade)})")

    avg = sum(grades.values()) / len(grades)
    highest = max(grades, key=grades.get)
    lowest = min(grades, key=grades.get)

    print(f"Average grade: {avg:.1f}")
    print(f"Highest: {highest} ({grades[highest]})")
    print(f"Lowest: {lowest} ({grades[lowest]})")

if __name__ == "__main__":
    main()
