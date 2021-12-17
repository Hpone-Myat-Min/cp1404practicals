def main():

    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        name = get_name_from_email(user_email)
        user_choice = input(f"Is your name {name}? (Y/n)").lower()
        if user_choice == "" or user_choice == 'y':
            email_to_name[user_email] = name
        else:
            user_name = input("Name: ")
            email_to_name[user_email] = user_name
        user_email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} {email}")


def get_name_from_email(email):
    email_details = email.split('@')
    possible_name = email_details[0].title().split('.')
    return possible_name


main()
