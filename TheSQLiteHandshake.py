import sqlite3

db_connection = sqlite3.connect('school.db')

my_cursor = db_connection.cursor()

my_cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)')


def add_student(name, grade):

    my_cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))

    db_connection.commit()


def print_students():

    my_cursor.execute("SELECT * FROM students")

    rows = my_cursor.fetchall()

    for row in rows: print(row)


def print_above_fifty():

    my_cursor.execute("SELECT * FROM students WHERE grade > 50")
    my_rows = my_cursor.fetchall()

    for row in my_rows: print(row)


user_response = input("Enter another student? (y/n): ")


while user_response == 'y':

    student_name = input("Student Name: ")

    student_grade = input("Student Grade: ")

    add_student(student_name, student_grade)

    user_response = input("Enter another student? (y/n): ")


else:

    print("\n~~~~~~~~~~~~~~~~~~~ALL STUDENTS~~~~~~~~~~~~~~~~~~")
    print_students()

    print("\n~~~~~~~~~~~~~~~~~~~ABOVE 50~~~~~~~~~~~~~~~~~~~~~~~")

    print_above_fifty()