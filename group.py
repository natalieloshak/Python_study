from student import Student


class Group:
    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        for s in self.group:
            if s.record_book == student.record_book:
                print(f"Student with record book {student.record_book} already exists.")
                return
        self.group.append(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group Number: {self.number}\n{all_students}"
