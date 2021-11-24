"""1. Ask name and write to new file"""
user_name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(user_name, file=out_file)
out_file.close()

"""2. Open file and read"""
in_file = open("name.txt", "r")
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

"""3. Open numbers.txt file and read"""
input_file = open("numbers", "r")
total_number = 0
for i in range(2):
    total_number += int(input_file.readline())
print("The result is", total_number)
input_file.close()

"""4. Print total of all lines"""
total = 0
number_file = open("numbers", "r")
number_list = number_file.readlines()
for number in number_list:
    total += int(number)
print(f"The total is {total}")
number_file.close()
