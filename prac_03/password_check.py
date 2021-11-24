MIN_PASSWORD_LENGTH = 7


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Password must be at least", MIN_PASSWORD_LENGTH)
        password = input("Enter password: ")
    return password


main()
