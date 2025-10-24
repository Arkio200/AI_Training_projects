def main():
    user_input = int(input("Enter an integer: "))
    print(check(user_input))

def check(n):
    if n % 2 == 0:
        return("Even")
    else:
        return("Odd")

if __name__ == "__main__":
    main()
