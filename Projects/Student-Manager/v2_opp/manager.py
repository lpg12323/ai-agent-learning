import json
from student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        # 检查学号是否为空
        if not student.student_id:
            raise ValueError("学号不能为空")
        # 检查学号是否重复
        if self._is_id_exists(student.student_id):
            raise ValueError(f"学号 {student.student_id} 已存在")
        self.students.append(student)

    def _is_id_exists(self, student_id):
        """检查学号是否已存在"""
        for s in self.students:
            if s.student_id == student_id:
                return True
        return False

    def find_by_id(self, student_id):
        """按学号查找学生，返回 Student 对象或 None"""
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def show_students(self):
        for s in  self.students:
            print(f"学号：{s.student_id}, 姓名：{s.name}, 年龄：{s.age}")

    def find_student(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def find_by_name(self, name):
        """按姓名查找学生，返回所有匹配的学生列表"""
        result = []
        for s in self.students:
            if s.name == name:
                result.append(s)
        return result

    def delete_student(self, student):
        """删除指定学生对象，成功返回 True，失败返回 False"""
        try:
            self.students.remove(student)
            return True
        except ValueError:
            return False

    def update_student(self, student, field, new_value):
        """修改学生信息，field 为 'name' 或 'age'，学号不允许修改"""
        if field == "name":
            student.name = new_value
        elif field == "age":
            age = int(new_value)
            if not 0 <= age <= 150:
                raise ValueError("年龄必须在 0-150 之间")
            student.age = age
        else:
            raise ValueError("不支持的修改字段")

    def save_to_file(self, filepath):
        """将学生数据保存到 JSON 文件"""
        data = {"students": [{"student_id": s.student_id, "name": s.name, "age": s.age}
                             for s in self.students]}
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_from_file(self, filepath):
        """从 JSON 文件加载学生数据，文件不存在或格式损坏则清空列表"""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.students = [Student(s["student_id"], s["name"], s["age"])
                             for s in data["students"]]
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []
