"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data"


def main():
    subjects = get_data()
    print(subjects)
    display_subject_details(subjects)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []   # list of subjects
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(sub_info):
    """Display subject details in full sentence."""
    for subject in sub_info:
        print("{:6} is taught by {:^12} and has {:3d} students".format(subject[0], subject[1], subject[2]))


main()
