class StudentStatistics:
    def __init__(self, students):
        self.students = list(students)

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

    def average_score(self):
        """返回平均成绩，空列表返回 0.0"""
        if not self.students:
            return 0.0
        total = sum(s.score for s in self.students)
        return total / len(self.students)

    def top_students(self):
        """返回成绩最高的所有学生列表，空列表返回 []"""
        if not self.students:
            return []
        max_score = max(s.score for s in self.students)
        return [s for s in self.students if s.score == max_score]

    def bottom_students(self):
        """返回成绩最低的所有学生列表，空列表返回 []"""
        if not self.students:
            return []
        min_score = min(s.score for s in self.students)
        return [s for s in self.students if s.score == min_score]

    def export_json(self):
        """返回统计信息的字典，不写文件"""
        tops = self.top_students()
        bottoms = self.bottom_students()
        return {
            "total_count": self.total_count(),
            "average_age": round(self.average_age(), 2),
            "average_score": round(self.average_score(), 2),
            "gender_ratio": self.gender_ratio(),
            "top_students": [
                {"student_id": s.student_id, "name": s.name, "score": s.score}
                for s in tops
            ],
            "bottom_students": [
                {"student_id": s.student_id, "name": s.name, "score": s.score}
                for s in bottoms
            ]
        }

    def print_report(self):
        """返回格式化的统计报告字符串，不直接 print"""
        tops = self.top_students()
        bottoms = self.bottom_students()
        ratio = self.gender_ratio()
        lines = [
            "=" * 30,
            "学生统计报告",
            "=" * 30,
            f"总人数：{self.total_count()}",
            f"平均年龄：{self.average_age():.1f}",
            f"平均成绩：{self.average_score():.1f}",
            f"性别比例：男={ratio['男']}, 女={ratio['女']}, 未知={ratio['未知']}",
        ]
        # 最高分（支持并列）
        if not tops:
            lines.append("最高分：无学生")
        elif len(tops) == 1:
            lines.append(f"最高分：{tops[0].name}（{tops[0].score}分）")
        else:
            lines.append(f"最高分（{len(tops)}人）：")
            for s in tops:
                lines.append(f"  {s.name}（{s.score}分）")
        # 最低分（支持并列）
        if not bottoms:
            lines.append("最低分：无学生")
        elif len(bottoms) == 1:
            lines.append(f"最低分：{bottoms[0].name}（{bottoms[0].score}分）")
        else:
            lines.append(f"最低分（{len(bottoms)}人）：")
            for s in bottoms:
                lines.append(f"  {s.name}（{s.score}分）")
        lines.append("=" * 30)
        return "\n".join(lines)
