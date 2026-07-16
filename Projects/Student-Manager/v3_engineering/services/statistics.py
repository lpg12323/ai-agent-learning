class StudentStatistics:
    def __init__(self, students):
        self.students = students

    def total_count(self):
        """返回学生总人数"""
        return len(self.students)

    def average_age(self):
        """返回平均年龄，空列表返回 0.0"""
        if not self.students:
            return 0.0
        total = sum(s.age for s in self.students)
        return total / len(self.students)

    def gender_ratio(self):
        """返回性别比例字典"""
        male = sum(1 for s in self.students if s.gender == "男")
        female = sum(1 for s in self.students if s.gender == "女")
        unknown = sum(1 for s in self.students if s.gender not in ("男", "女"))
        return {"男": male, "女": female, "未知": unknown}
