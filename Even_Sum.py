def main():
    user_input = input("List of integers: ")
    string_list = user_input.split()
    integer_list = []
    for i in string_list:
        integer_list.append(int(i))
    even_integer_list = []
    for n in integer_list:
        if is_even(n):
            even_integer_list.append(n)
    print(f"{sum(even_integer_list)}")



def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()