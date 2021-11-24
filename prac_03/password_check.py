MIN_PASSWORD_LENGTH = 7


def main():
    """Check password."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get valid password."""
    password = input("Enter password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Password must be at least", MIN_PASSWORD_LENGTH)
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print as many asterisks as password length"""
    print("*" * len(password))


main()
