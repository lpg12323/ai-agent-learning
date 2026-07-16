import json
from models.student import Student


class JsonStorage:
    @staticmethod
    def save(filepath, students):
        """将学生列表序列化为 JSON 并保存到文件"""
        data = {"students": [{"student_id": s.student_id, "name": s.name, "age": s.age}
                             for s in students]}
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load(filepath):
        """从 JSON 文件读取并反序列化为 Student 对象列表"""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Student(s["student_id"], s["name"], s["age"])
                    for s in data["students"]]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
