def get_student_grades(count):
    grades = {}
    for _ in range(count):
        name, grade = input("Name and grade: ").split()
        grades[name] = int(grade)
    return grades

def display_student_grades(grades):
    for name, grade in grades.items():
        print(f"{name}: {grade}")

def get_stats(grades):
    avg = sum(grades.values()) / len(grades)
    highest_name = max(grades, key=grades.get)
    lowest_name = min(grades, key=grades.get)
    return avg, highest_name, lowest_name

def main():
    student_count = int(input("Student count: "))
    grades = get_student_grades(student_count)
    
    print("Student Grades:")
    display_student_grades(grades)
    
    avg, hi, lo = get_stats(grades)
    print(f"Average grade: {avg:.1f}")
    print(f"Highest: {hi} ({grades[hi]})")
    print(f"Lowest: {lo} ({grades[lo]})")

if __name__ == "__main__":
    main()
