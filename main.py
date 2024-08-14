class TooManyStudentsException(Exception):
    """Виняток, який виникає при спробі додати більше 10 студентів до групи."""
    pass

class Група:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsException("Не можна додати більше 10 студентів до групи.")
        self.students.append(student)

    def __str__(self):
        return f"Група: {self.students}"

# Приклад використання класу Група та обробка винятку
try:
    група = Група()
    for i in range(11):
        група.add_student(f"Студент {i+1}")
except TooManyStudentsException as e:
    print(e)

print(група)
