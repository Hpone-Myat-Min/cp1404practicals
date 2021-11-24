CHOICES = """  
  i. Show the even numbers from x to y
 ii. Show the odd numbers from x to y
iii. Show the squares from x to y
 iv. Exit the program
 """


def main():
    print(CHOICES)
    user_choice = input("Which option would you like to choose: i, ii, iii, iv? ").lower()
    while user_choice != "iv":
        while user_choice != 'i' and user_choice != 'ii' and user_choice != "iii":
            print("Invalid Choice")
            print(CHOICES)
            user_choice = input("Which option would you like to choose: i, ii, iii, iv? ").lower()
        min_value = int(input("Enter the value of x: "))
        max_value = int(input("Enter the value of y: "))
        if user_choice == 'i':
            show_even(min_value, max_value)
        elif user_choice == "ii":
            show_odd(min_value, max_value)
        elif user_choice == "iii":
            show_square(min_value, max_value)
        print(CHOICES)
        user_choice = input("Which option would you like to choose: i, ii, iii, iv? ").lower()
    print("Have a nice day! ")


def show_even(x, y):
    if x % 2 == 1:
        for i in range(x + 1, y+1, 2):
            print(i, end=" ")
        print()
    else:
        for i in range(x, y + 1, 2):
            print(i, end=" ")
        print()
    return ()


def show_odd(x, y):
    if x % 2 == 1:
        for i in range(x, y+1, 2):
            print(i, end=" ")
        print()
    else:
        for i in range(x + 1, y + 1, 2):
            print(i, end=" ")
        print()
    return ()


def show_square(x, y):
    for i in range(x, y + 1):
        print(i ** 2, end=" ")
    print()


main()
