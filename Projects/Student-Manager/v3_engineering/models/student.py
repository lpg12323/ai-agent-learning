class Student:
    def __init__(self, student_id, name, age, gender=""):
        self.student_id = student_id  # 学号
        self.name = name
        try :
            self.age = int(age)
        except (ValueError, TypeError):
             raise ValueError(f"年龄必须是数字，收到：{age!r}")
        self.gender = gender 
