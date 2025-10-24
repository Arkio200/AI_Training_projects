import string

def count_words(sentence):
    sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def main():
    user_input = input("Sentence: ")
    print(count_words(user_input))

if __name__ == "__main__":
    main()