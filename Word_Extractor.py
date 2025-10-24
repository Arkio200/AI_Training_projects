import string

def main():
    user_input = input("Sentence: ").lower()
    no_punctuation = remove_punctuation(user_input).split()
    word_set = set()
    for word in no_punctuation:
        word_set.add(word)
    print(sorted(word_set))

def remove_punctuation(s):
    no_punctuation = s.translate(str.maketrans('', '', string.punctuation))
    return no_punctuation


if __name__ == "__main__":
    main()