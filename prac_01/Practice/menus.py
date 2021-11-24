MENU = """(H)ello
(G)oodbye
(Q)uit"""
user_name = input("Enter name: ")
print(MENU)
choice = input(">>> ").title()
while choice != 'Q':
    if choice == 'H':
        print("Hello", user_name)
    elif choice == 'G':
        print("Goodbye", user_name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").title()
print("Finished.")
