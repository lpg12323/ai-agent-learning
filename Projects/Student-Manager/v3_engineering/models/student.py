class Student:
    def __init__(self, student_id, name, age, gender="", score=0.0):
        self.student_id = student_id  # 学号
        self.name = name
        self.age = self._validate_age(age)
        self.gender = gender
        self.score = self._validate_score(score)

    @staticmethod
    def _validate_age(value):
        """校验年龄：转为 int，范围 0-150，返回校验后的值"""
        try:
            age = int(value)
        except (ValueError, TypeError):
            raise ValueError(f"年龄必须是数字，收到：{value!r}")
        if not 0 <= age <= 150:
            raise ValueError(f"年龄必须在 0-150 之间，收到：{age}")
        return age

    @staticmethod
    def _validate_score(value):
        """校验成绩：转为 float，范围 0-100，返回校验后的值"""
        try:
            score = float(value)
        except (ValueError, TypeError):
            raise ValueError(f"成绩必须是数字，收到：{value!r}")
        if not 0 <= score <= 100:
            raise ValueError(f"成绩必须在 0-100 之间，收到：{score}")
        return score
