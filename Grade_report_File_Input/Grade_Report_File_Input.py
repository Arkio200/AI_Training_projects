from Grade_Report import value_list, highest_and_lowest_name_identifier, average

def main():
    student_list = []
    with open ("grades.txt") as f:
        for line in f:
            student_list.append(line.removesuffix("\n"))

    student_count = 0
    for i in student_list:
        print(i)
        student_count += 1

    print("")

    student_plus_grade = make_dict(student_count, student_list)

    student_grades = value_list(student_plus_grade)
    print(f"Average grade: {average(student_grades)}")

    highest_score, highest_score_name = highest_and_lowest_name_identifier(student_grades, student_plus_grade)[0], highest_and_lowest_name_identifier(student_grades, student_plus_grade)[2]
    lowest_score, lowest_score_name = highest_and_lowest_name_identifier(student_grades, student_plus_grade)[1], highest_and_lowest_name_identifier(student_grades, student_plus_grade)[3]

    print(f"Highest: {highest_score_name} ({highest_score})")
    print(f"Lowest: {lowest_score_name} ({lowest_score})")

    print("Letter grade counts")
    print_letter_grade_count(student_list)

def make_dict(student_list):
    student_plus_grade = []
    for line in student_list:
        name, grade, _ = line.split()
        student_plus_grade.append({name.removesuffix(":"): int(grade)})
    return student_plus_grade

def print_letter_grade_count(student_list):
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for line in student_list:
        *_, letter = line.split()
        letter = letter.strip("()")
        if letter in counts:
            counts[letter] += 1

    for grade, count in counts.items():
        print(f"{grade}: {count}")




if __name__ == "__main__":
    main()