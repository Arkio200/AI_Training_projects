def main():
    user_input = input("Scores: ")
    scores = [int(x) for x in user_input.split()]
    
    if not all(0 <= n <= 100 for n in scores):
        print("Please enter valid scores between 0 and 100.")
        return
    
    passing = sum(1 for n in scores if n >= 60)
    failing = len(scores) - passing
    
    print(f"Average: {sum(scores) / len(scores):.1f}")
    print(f"Highest: {max(scores)}")
    print(f"Lowest: {min(scores)}")
    print(f"Passing count: {passing}")
    print(f"Failing count: {failing}")

if __name__ == "__main__":
    main()