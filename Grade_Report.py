def main():
    student_count = int(input("Student count: "))
    student_plus_grade = make_dict(student_count)

    print("Student Grades:")
    display_student_plus_grade(student_plus_grade)

    print(f"Average grade: {average(value_list(student_plus_grade))}")
            
    print(f"Highest: {highest_and_lowest_name_identifier(value_list(student_plus_grade), student_plus_grade)[2]} ({highest_and_lowest_name_identifier(value_list(student_plus_grade), student_plus_grade)[0]})")
    
    print(f"Lowest: {highest_and_lowest_name_identifier(value_list(student_plus_grade), student_plus_grade)[3]} ({highest_and_lowest_name_identifier(value_list(student_plus_grade), student_plus_grade)[1]})")

def make_dict(s):
    student_plus_grade = []
    laps = 0
    while laps < s:
        name, grade = input("Name and grade: ").split()
        student_plus_grade.append({name: int(grade)})
        laps += 1
    return student_plus_grade

def display_student_plus_grade(dictionary):
    for pair in dictionary:
        for key in pair:
            letter_grade = ""
            if 90 <= pair.get(key) <= 100:
                letter_grade = "A"
            elif 80 <= pair.get(key) <= 89:
                letter_grade = "B"
            elif 70 <= pair.get(key) <= 79:
                letter_grade = "C"
            elif 60 <= pair.get(key) <= 69:
                letter_grade = "D"
            else:
                letter_grade = "F"
            print(f"{key}: {pair.get(key)} ({letter_grade})")

def value_list(dictionary):
    values = []
    for pair in dictionary:
        for key in pair:
            values.append(int(pair.get(key)))
    return values

def average(value_list):
    return f"{sum(value_list) / len(value_list):.1f}"

def highest_and_lowest_name_identifier(value_list, dictionary):
    highest_score = max(value_list)
    lowest_score = min(value_list)
    highest_score_name = []
    lowest_score_name = []
    for pair in dictionary:
        for key, value in pair.items():
            if int(value) == highest_score:
                highest_score_name.append(key)
            elif int(value) == lowest_score:
                lowest_score_name.append(key)
            else:
                continue
    return highest_score, lowest_score, str(highest_score_name).strip("[']"), str(lowest_score_name).strip("[']")

if __name__ == "__main__":
    main()

