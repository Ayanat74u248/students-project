students = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
def find_student(name):
    for student in students:
        if student.lower() == name.lower():
            print("Студент найден:", student)
            return

    print("Студент не найден")
    find_student("Charlie")  