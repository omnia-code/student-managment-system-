#----------studen management system-------------#

Students = []

print("Welcome to Student Management System")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter the name of the student: ") 
        student_id = int(input("Enter the ID of the student: "))
        student_grade = input("Enter the grade of the student: ")
        Students.append((student_name, student_id, student_grade))
        print("Student added successfully!")
    
    elif choice == "2":
        if Students:
           def view_students():
                for student_name, student_id, student_grade in Students:
                    print(f"{student_name}: {student_id} - Grade=> {student_grade}")
           view_students()
        else:
            print("No students recorded.")
    elif choice == "3":
      def search_student(name_or_id):
        found = False
        for student_name, student_id, student_grade in Students:
            if student_name == name_or_id or str(student_id) == name_or_id:
                print(f"Student found: {student_name}, ID: {student_id}, Grade: {student_grade}")
                found = True
                break
        if not found:
            print("Student not found.")
      search_student(input("Enter the name or ID of the student: "))
    elif choice == "4":
        update_name = input("Enter the name of the student or ID to update: ")
        for i, (student_name, student_id, student_grade) in enumerate(Students):
            if student_name == update_name or student_id == int(update_name):
                new_id = int(input("Enter the new ID for the student: "))
                new_grade = input("Enter the new grade for the student: ")
                Students[i] = (student_name, new_id, new_grade)
                print("Student updated successfully!")
                break
        else:
            print("Student not found.")
    elif choice == "5":
        delete_name = input("Enter the name of the student or ID to delete: ")
        for i, (student_name, student_id, student_grade) in enumerate(Students):
            if student_name == delete_name or str(student_id) == delete_name:
                del Students[i]
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")
    elif choice == "6":
        print("see you later!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")