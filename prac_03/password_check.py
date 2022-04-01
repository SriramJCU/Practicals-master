def main():
    password = get_password()
    length = len(password)
    while length <= 4:
        print("Error! Password is too short!")
        password = get_password()
        length = len(password)
    print(string_to_asterisks(length))


def get_password():
    password = input("Please enter your password: ")
    return password


def string_to_asterisks(length):
    return "*" * length

main()
