import csv
import sys
from io import StringIO

def main():
    try:
        name_grade_dict = get_dict()
    except FileNotFoundError:
        print("File not found.")
        sys.exit()
    else:
        if not name_grade_dict:
            print("No data found.")
            sys.exit()

    grade_list = get_grade_list(name_grade_dict)
    if not grade_list:
        print("No valid grades to process.")
        sys.exit()

    highest_score, lowest_score, highest_name, lowest_name = get_highest_lowest_name_plus_grade(grade_list, name_grade_dict)

    print(f"Average grade: {float(average(grade_list))}")
    print(f"Highest: {highest_name} ({highest_score})")
    print(f"Lowest: {lowest_name} ({lowest_score})")
    print("Letter grade counts:")
    print_letter_grade_counts(get_letter_grade(name_grade_dict))

def get_dict():
    name_grade_dict = {}
    with open("grades2.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Name"]
            grade_str = row["Grade"]
            if not grade_str.isnumeric():
                print(f"Invalid grade for {name}, skipped.")
                continue
            grade = int(grade_str)
            name_grade_dict[name] = grade
    return name_grade_dict

def average(value_list):
    return f"{sum(value_list) / len(value_list):.1f}"

def get_grade_list(dictionary):
    return list(dictionary.values())

def get_letter_grade(dictionary):
    letter_grade_list = []
    for grade in dictionary.values():
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

def get_highest_lowest_name_plus_grade(grade_list, dictionary):
    highest_score = max(grade_list)
    lowest_score = min(grade_list)
    highest_score_name = [k for k, v in dictionary.items() if v == highest_score]
    lowest_score_name = [k for k, v in dictionary.items() if v == lowest_score]
    return highest_score, lowest_score, str(highest_score_name).strip("[']"), str(lowest_score_name).strip("[']")

def print_letter_grade_counts(letter_grade_list):
    counts = {letter: 0 for letter in "ABCDF"}
    for letter in letter_grade_list:
        counts[letter] += 1
    for letter, count in counts.items():
        print(f"{letter}: {count}")

def save_summary():
    buffer = StringIO()
    original_stdout = sys.stdout
    sys.stdout = buffer
    try:
        main()
    finally:
        sys.stdout = original_stdout
    with open("summary.txt", "w") as f:
        f.write(buffer.getvalue())

if __name__ == "__main__":
    main()
    save_summary()
