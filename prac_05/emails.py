def main():
    NAME_TO_EMAIL = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email).title()
        choice = input(f"Is your name {name}? (Y/n) ").lower()
        if choice != "":
            if choice[0] == "n":
                name = input("Enter your name: ").title()
        NAME_TO_EMAIL[name] = email
        email = input('Email: ')

    for key, value in NAME_TO_EMAIL.items():
        print(key, f"({value})")

def get_name_from_email(email):
    email_split = email.split("@")
    raw_name = email_split[0].split(".")
    if len(raw_name) > 1:
        name = ' '.join([str(i) for i in raw_name])
    else:
        name = raw_name[0]
    return name


main()