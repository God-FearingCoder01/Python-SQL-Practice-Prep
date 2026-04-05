student_list = []

def add_student(std_name, std_grade):

    new_student = {"name": std_name, "grade": std_grade}

    student_list.append(new_student)
    return student_list

def print_students(std_list):
    for std in std_list:
        print(std)

def print_above_fifty(std_lst):

    above_50_students = []
    for std in std_lst:

        if std['grade'] > 50:

            above_50_students.append(std)

    print_students(above_50_students)


updated_student_list = []

print("Continue adding student data? (y/n): ")
user_response = input()


while (user_response == 'y'):

    student_name = input("Student Name: ")

    student_grade = int(input("Student Grade: "))

    updated_student_list = add_student(student_name, student_grade)
    print("Continue adding student data? (y/n): ")
    user_response = input()

else:
    print("\n******ALL STUDENTS******\n")
    print_students( updated_student_list)
    print("\n**********ABOVE 50**********\n")
    print_above_fifty(updated_student_list)