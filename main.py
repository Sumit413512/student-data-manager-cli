from src.student_manager import *

def menu():
    while True:

        print("\n===== Student Data Manager =====")
        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Update Student")
        print("5 Delete Student")
        print("6 Export JSON")
        print("7 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            export_students_json()

        elif choice == "7":
            print("Goodbye")
            break

        else:
            print("Invalid choice")

menu()
