students = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
def add_student(name):
    students.append(name)
    print("Студент добавлен:", name)

add_student("Grace")
def show_students():
    print("Список студентов:")
    for student in students:
        print(student)

show_students()
print("Всего студентов:", len(students))