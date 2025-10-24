def main():
    user_input = input("Enter list of integers: ")
    numbers = [int(x) for x in user_input.split()]
    print(f"Sum: {sum(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.1f}")

if __name__ == "__main__":
    main()