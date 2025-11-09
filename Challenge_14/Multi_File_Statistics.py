import sys
import csv
from io import StringIO

def main():

    user_input = input("Enter CSV file names: ").split(sep=", ")

    file_names = prompt_user(user_input)

    class_names = get_class_names(file_names)

    file_plus_dictionary = process_files(file_names)

    overall_grades = get_overall_grades(file_plus_dictionary)

    highest_score, lowest_score, highest_score_name, lowest_score_name = get_highest_lowest_name_plus_grade(overall_grades, file_plus_dictionary)[0], get_highest_lowest_name_plus_grade(overall_grades, file_plus_dictionary)[1], get_highest_lowest_name_plus_grade(overall_grades, file_plus_dictionary)[2], get_highest_lowest_name_plus_grade(overall_grades, file_plus_dictionary)[3]

    individual_class_grades = get_individual_class_grades(file_plus_dictionary)

    print("")

    for i in individual_class_grades:
        print(f"{class_names[0]} Average: {average(i)}")
        class_names.remove(class_names[0])

    print(f"Overall Average: {average(overall_grades)}")

    print(f"Highest Overall: {highest_score_name} ({highest_score})")
    print(f"Lowest Overall: {lowest_score_name} ({lowest_score})")


    print("")

    print("Letter grade counts:")
    print_letter_grade_counts(get_letter_grade(overall_grades))




def prompt_user(user_input) -> list:
    file_names = []
    for f in user_input:
        if not f.endswith(".csv"):
            print(f"{f} is not a CSV file. It will be skipped.")
        else:
            file_names.append(f)
    return file_names

def get_class_names(file_list) -> list:
    class_names = []
    for i in file_list:
        name = i.lstrip("grades_").rstrip(".csv")
        class_names.append(name)
    return class_names

def get_dict(f) -> dict:
    name_grade_dict = {}
    with open(f, newline="") as fi:
        print(f"Processing file: {f}")
        reader = csv.DictReader(fi)
        for row in reader:
            name = row["Name"]
            grade_str = row["Grade"]
            if not grade_str.isnumeric() or int(grade_str) > 100 or int(grade_str) < 0 :
                print(f"Invalid grade for {name}, skipped.")
                continue
            grade = int(grade_str)
            name_grade_dict[name] = grade
    return name_grade_dict

def process_files(file_list) -> list:
    file_plus_dictionary = []
    for i in file_list:
        try:
            dictionary = get_dict(i)
        except FileNotFoundError:
            print(f"{i} not found.")
            continue
        else:
            if not dictionary:
                print("No data found.")
                continue
            else:   
                file_plus_dictionary.append(dictionary)
    return file_plus_dictionary

def get_overall_grades(dictionary) -> list:
    overall_grades = []
    for i in dictionary:
        for key in i:
             overall_grades.append(int(i.get(key)))
    return overall_grades

def get_individual_class_grades(dictionary):
    individual_class_grades = []
    for i in dictionary:
        grades = []
        for key in i:
            grades.append(int(i.get(key)))
        individual_class_grades.append(grades)
    return individual_class_grades

def average(value_list):
    return f"{sum(value_list) / len(value_list):.1f}"

def get_letter_grade(value_list):
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

def get_highest_lowest_name_plus_grade(grade_list, dictionary):
    highest_score = max(grade_list)
    lowest_score = min(grade_list)
    highest_score_name = ""
    lowest_score_name = ""
    for item in dictionary:
        for key in item:
            if item.get(key) == highest_score:
                highest_score_name = key
            elif item.get(key) == lowest_score:
                lowest_score_name = key
    return highest_score, lowest_score, str(highest_score_name).strip("[']"), str(lowest_score_name).strip("[']")

def save_summary():
    buffer = StringIO()
    original_stdout = sys.stdout
    sys.stdout = buffer
    try:
        main()
    finally:
        sys.stdout = original_stdout
    with open("combined_summary.txt", "w") as f:
        f.write(buffer.getvalue())







if __name__ =="__main__":
    main()
    save_summary()