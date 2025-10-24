def main():
    dictionaries = []
    while True:
        user_input = input("Student and score: ")
        if len(user_input.split()) == 2 and user_input.lower != "stop":
            name, score = user_input.split()
            dictionaries.append({"name": name, "score": score})
            continue
        elif user_input.lower == "stop":
            break
        break
    scores = []
    for dictionary in dictionaries:
        scores.append(int(dictionary.get("score")))
    max_score = max(scores)
    min_score = min(scores)
    print(f"Average: {sum(scores) / len(scores):.1f}")
    print(f"Highest: {max(dictionaries).get("name")} ({max_score})")
    print(f"Lowest: {min(dictionaries).get("name")} ({min_score})")



#    values = []
#    print(f"Average: {sum(values) / len(values):.1f}")
#    print(f"Highest: {dictionary[name]} ({max(values)})")
#    print(f"Lowest: {dictionary[name]} ({min(values)})")

if __name__ == "__main__":
    main()
    

        
