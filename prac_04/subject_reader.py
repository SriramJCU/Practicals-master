"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for subject_details in data:
        subject_code = subject_details[0]
        subject_lecturer = subject_details[1]
        number_of_students = subject_details[2]
        print("{} is taught by {:12} and has {:3} students".format(subject_code, subject_lecturer, number_of_students))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        data.append(line.split(","))
    input_file.close()
    return data

main()
