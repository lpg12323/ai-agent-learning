class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for s in  self.students:
            print(f"姓名：{s.name}, 年龄：{s.age}")

    def find_student(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None
    
    def delete_student(self, name):
        student = self.find_student(name)
        if student:
            self.students.remove(student)
            print(f"已删除：{student.name}")
        else:
            print("未找到该学生")
