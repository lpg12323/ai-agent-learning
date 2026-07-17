class Student:
    def __init__(self, student_id, name, age, gender="", score=0.0):
        self.student_id = student_id  # 学号
        self.name = name
        try:
            self.age = int(age)
        except (ValueError, TypeError):
             raise ValueError(f"年龄必须是数字，收到：{age!r}")
        self.gender = gender
        try:
            self.score = float(score)
        except (ValueError, TypeError):
            raise ValueError(f"成绩必须是数字，收到：{score!r}")
        if not 0 <= self.score <= 100:
            raise ValueError(f"成绩必须在 0-100 之间，收到：{self.score}")
