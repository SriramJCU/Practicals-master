def main():
    password = input("Please enter your password: ")
    length = len(password)
    while length <= 4:
        print("Error! Password is too short!")
        password = input("Please enter your password: ")
        length = len(password)
    print(string_to_asterisks(length))

def string_to_asterisks(length):
    return "*" * length

main()
