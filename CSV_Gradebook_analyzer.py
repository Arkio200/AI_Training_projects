import csv
import sys
from Grade_Report import average

def main():
    name_grade_dict = get_dict()
    grade_list = get_grade_list(name_grade_dict)
    highest_score = get_highest_lowest_name_plus_grade(grade_list, name_grade_dict)[0]
    lowest_score = get_highest_lowest_name_plus_grade(grade_list, name_grade_dict)[1]
    highest_name = get_highest_lowest_name_plus_grade(grade_list, name_grade_dict)[2]
    lowest_name = get_highest_lowest_name_plus_grade(grade_list, name_grade_dict)[3]
    print(f"Average grade: {average(grade_list)}")

    print(f"Highest: {highest_name} ({highest_score})")

    print(f"Lowest: {lowest_name} ({lowest_score})")

    print("Letter grade counts:")
    print_letter_grade_counts(get_letter_grade(name_grade_dict))
    return



def get_dict():
    name_grade_dict = {}
    with open ("grades.csv") as f:
        reader = csv.DictReader(f, fieldnames=("Name", "Grade"))
        for row in reader:
            name = row["Name"]
            grade = row["Grade"]
            if name == "Name" and grade == "Grade":
                continue
            else:
                name_grade_dict.update({name: grade})
    return(name_grade_dict)

def get_grade_list(dictionary):
    value_list = []
    for key in dictionary:
        value_list.append(int(dictionary.get(key)))
    return value_list

def get_letter_grade(dictionary):
    letter_grade_list = []
    for key in dictionary:
        grade = int(dictionary.get(key))
        letter_grade = ""
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
    highest_score_name = []
    lowest_score_name = []
    for key, value in dictionary.items():
        if int(value) == highest_score:
            highest_score_name.append(key)
        elif int(value) == lowest_score:
            lowest_score_name.append(key)
        else:
            continue
    return highest_score, lowest_score, str(highest_score_name).strip("[']"), str(lowest_score_name).strip("[']")

def print_letter_grade_counts(letter_grade_list):
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for letter_grade in letter_grade_list:
        if letter_grade in counts:
            counts[letter_grade] += 1
    for pair in counts:
        print(f"{pair}: {counts.get(pair)}")

def save_summary():
    with open ("summary.txt", "w") as f:
        o = sys.stdout
        sys.stdout = f
        main()


if __name__ == "__main__":
    main()

save_summary()