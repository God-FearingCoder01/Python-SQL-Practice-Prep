student_list = []

def add_student(std_name, std_grade):
    new_student = {"name": std_name, "grade": std_grade}
    student_list.append(new_student)
    return student_list

def print_students(std_list):
    if not std_list: print("There are no students yet!") 
    else:
        for std in std_list : print(std)
    

def print_above_fifty(std_lst):
    above_50 = [std for std in std_lst if std['grade'] > 50]
    # above_50 = []
    # for std in std_lst:
    #     if std['grade'] > 50:
    #         above_50.append(std)
    print_students(above_50)


updated_student_list = []

user_response = input("Continue adding student data? (y/n): ")


while (user_response == 'y'):
    student_name = input("Student Name: ")
    try:
        student_grade = int(input("Student Grade: "))
    except Exception as e:
        print(f"Icaught an error! It is called: {type(e).__name__}")
        print(f"The message is: {e}") 
    updated_student_list = add_student(student_name, student_grade)
    user_response = input("Continue adding student data? (y/n): ")

else:
    print("\n******ALL STUDENTS******\n")
    print_students( updated_student_list)
    print("\n**********ABOVE 50**********\n")
    print_above_fifty(updated_student_list)