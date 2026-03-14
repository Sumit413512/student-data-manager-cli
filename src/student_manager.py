from src.file_handler import read_students, write_students, export_to_json


def add_student():
    students = read_students()

    id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    student = {
        "id": id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    write_students(students)

    print("Student added successfully")
def view_students():
    students = read_students()

    if not students:
        print("No studnets found")
        return
    for student in students:
        print(
            student["id"],
            student["name"],
            student["age"],
            student["course"]

        )
def serach_student():
    students = read_students()
    student_id = input("Enter student ID to search :")


    for student in students:
        if student["id"] ==student_id:
            print("student found:")
            print(student)
            return
                    

    print('student not found')

def update_student():
    students = read_students()
    student_id = input("Enter ID to update :")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("New name:")
            student["age"] = input("New age:")
            student["course"] = input("New course:")


            write_students(students)

            print("Student updated")
            return
        
    print("student not found")

def delete_student():
    students = read_students()
    student_id = input(" Enter ID to delete: ")

    updated_students = [
        student for student in students 
        if student["id"] != student_id
    ]


    write_students(updated_students)


    print("student deleted")


def export_students_json():
    students = read_students()
    export_to_json(students)
                   
        
        