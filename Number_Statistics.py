def main():
    user_input = input("Enter list of integers: ")
    numbers = [int(x) for x in user_input.split()]
    count = 0
    for _ in numbers:
        count += 1
    print(f"Count: {count}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.1f}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")

if __name__ == "__main__":
    main()