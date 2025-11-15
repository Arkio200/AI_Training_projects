import sys
import json
from contextlib import redirect_stdout
from statistics import mode, median
import numpy as np
import matplotlib.pyplot as plt

def main() -> None:
    user_input = input("JSON file names: ").split(sep=", ")
    file_names = get_file_names(user_input)

    print("")

    validated_data = data_validation(file_names)

    overall_grades = get_overall_grades(validated_data)

    individual_class_grades = get_individual_class_grades(validated_data)

    highest_score, lowest_score, highest_name, lowest_name = get_highest_lowest_name_plus_grade(overall_grades, validated_data)

    letter_grades = get_letter_grades(overall_grades)

    print_divider("Class Statistics")
    for c in individual_class_grades:
        c_average = get_average(individual_class_grades.get(c))
        c_median = median(individual_class_grades.get(c))
        c_mode = mode(individual_class_grades.get(c))
        c_range = get_range(individual_class_grades.get(c))
        print(f"{c} Average: {c_average}")
        print(f"{c} Median: {c_median}")
        print(f"{c} Mode: {c_mode}")
        print(f"{c} Range: {c_range}")
        print("")

    print_divider("Overall Statistics")
    print(f"Overall Average: {get_average(overall_grades)}")
    print(f"Overall Median: {median(overall_grades)}")
    print(f"Overall Mode: {mode(overall_grades)}")
    print(f"Overall Range: {get_range(overall_grades)}")
    print_divider()

    print(f"Highest Overall: {highest_name} ({highest_score})")
    print(f"Lowest Overall: {lowest_name} ({lowest_score})")

    print_divider()

    print("Letter grade counts:")
    print_letter_grade_counts(letter_grades)

    summary_data = {"ClassStatistics": {},
                    "OverallStatistics": {"Average": get_average(overall_grades), "Mediane": median(overall_grades),
                                           "Mode": mode(overall_grades), "Range": get_range(overall_grades)},
                    "Highest Overall": f"{highest_name} ({highest_score})",
                    "Lowest Overall": f"{lowest_name} ({lowest_score})",
                    "Letter Grade Counts": {letter: get_letter_grades(overall_grades).count(letter) for letter in "ABCDF"}
                    }
    dictionary_list = []
    for c in individual_class_grades:
        dictionary = {c : {"Average": c_average, "Median": c_median, "Mode": c_mode, "Range": c_range}}
        dictionary_list.append(dictionary)
    summary_data.update({"ClassStatistics": dictionary_list})

    generate_bar_chart(individual_class_grades)
    save_json_prompt(summary_data)



def print_divider(label=None):
    if label:
        print(f"\n{'-' * 10} {label.upper()} {'-' * 10}")
    else:
        print("-" * 40)

def get_file_names(user_input) -> list:
    file_names = []
    for i in user_input:
        if not i.endswith(".json"):
            print("File is not a JSON file. It will be skipped.")
            continue
        else:
            file_names.append(i)
    return file_names

def data_validation(file_names) -> dict:
    class_student_grade_dict = {}
    for name in file_names:
        print(f"processing file: {name}")
        try:
            with open (name, "r") as f:
                d = json.load(f)
                class_name = d["Class"]
                student_grade_list = []
                for student in d["Students"]:
                    student_name = student["Name"]
                    student_grade = student["Grade"]
                    if not student_grade:
                        print(f"{student_name} doesn't have a grade. They will be skipped.")
                        continue
                    elif not student["Grade"] in range(0, 100) or not isinstance(student_grade, int):
                        print(f"Invalid data for {student_name}. They will be skipped")
                        continue
                    else:
                        student_grade_list.append(student)
                        class_student_grade_dict.update({class_name: student_grade_list})
        except FileNotFoundError:
            print(f"File not found.")
            continue
    return class_student_grade_dict

def get_overall_grades(data) -> list:
    grades = []
    for c in data:
        for student in data.get(c):
            grade = student.get("Grade")
            grades.append(grade)
    return grades

def get_individual_class_grades(data) -> dict:
    class_plus_grades = {}
    for c in data:
        grades = []
        for student in data.get(c):
            grade = student.get("Grade")
            grades.append(grade)
        class_plus_grades.update({c: grades})
    return class_plus_grades

def get_average(int_list) -> float:
    return f"{sum(int_list) / len(int_list):.1f}"

def get_range(int_list) -> int:
    highest_grade = max(int_list)
    lowest_grade = min(int_list)
    return highest_grade - lowest_grade

def get_highest_lowest_name_plus_grade(grade_list, data):
    highest_score = max(grade_list)
    lowest_score = min(grade_list)
    highest_score_name = ""
    lowest_score_name = ""
    for c in data:
        for student in data.get(c):
            grade = student["Grade"]
            name = student["Name"]
            if grade == highest_score:
                highest_score_name = name
            elif grade == lowest_score:
                lowest_score_name = name
    return highest_score, lowest_score, str(highest_score_name).strip("[']"), str(lowest_score_name).strip("[']")

def get_letter_grades(value_list):
    letter_grade_list = []
    for grade in value_list:
        if 90 <= grade <= 100:
            letter_grade = "A"
        elif 80 <= grade <= 89:
            letter_grade = "B"
        elif 70 <= grade <= 79:
            letter_grade = "C"
        elif 60 <= grade <= 69:
            letter_grade = "D"
        else:
            letter_grade = "F"
        letter_grade_list.append(letter_grade)
    return letter_grade_list

def print_letter_grade_counts(letter_grade_list):
    counts = {letter: 0 for letter in "ABCDF"}
    for letter in letter_grade_list:
        counts[letter] += 1
    for letter, count in counts.items():
        print(f"{letter}: {count}")

def save_summary():
    with open("json_summary.txt", "w") as f:
        with redirect_stdout(f):
            main()
        
def save_json_prompt(data):
    while True:
        yes_no_question = input("Would you like to save data to another JSON file?(y/n) ").lower()
        if yes_no_question == "y":
            while True:
                json_file_name = input("New file name (or 'n' to cancel the operation): ")
                if json_file_name.endswith(".json"):
                    with open (json_file_name, "w") as f:
                        json.dump(data, f, indent=2)
                    print(f"Data was saved to {json_file_name}")
                    break
                elif json_file_name.lower().strip() == "n":
                    break
                else:
                    print("File name must end with '.json'.")
                    continue
            break
        elif yes_no_question == "n":
            print("Data wasn't saved to a JSON file")
        break

def generate_bar_chart(individual_class_grades):
    class_names = []
    average_grades = []
    class_array = np.array(class_names)
    grades_array = np.array(average_grades)
    for c in individual_class_grades:
        class_names.append(c)
        avr = get_average(individual_class_grades.get(c))
        average_grades.append(avr)
    plt.bar(class_array, grades_array, )
    plt.title("Class Average Grades")
    plt.xlabel("Classes")
    plt.ylabel("Grades")
    plt.savefig("Class_average.png", dpi=300, bbox_inches="tight")
    plt.show()
    
if __name__ == "__main__":
    main()

    print("")

    print("Re-enter the file names to save output or use Ctrl C to exit.")
    try:
        save_summary()
        print("The output was saved.")
    except KeyboardInterrupt:
        print("The output wasn't saved.")
        sys.exit()