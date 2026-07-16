from models.student import Student
from services.manager import StudentManager
from services.statistics import StudentStatistics

def main():
    manager = StudentManager()
    manager.load_from_file("data/students.json")

    while True:
        print("="*30)
        print("学生管理系统")
        print("1.添加学生")
        print("2.查看学生")
        print("3.查找学生")
        print("4.删除学生")
        print("5.按学号查询")
        print("6.修改学生")
        print("7.退出")
        print("8.统计信息")
        print("="*30)

        choice = input("请输入操作编号：")

        if choice == "1":
            # 添加学生，包含学号输入和空值校验
            student_id = input("请输入学号：")
            while not student_id:
                print("学号不能为空，请重新输入")
                student_id = input("请输入学号：")
            name = input("请输入学生姓名：")
            age = input("请输入学生年龄：")
            
            try:
                student = Student(student_id, name, age)
                manager.add_student(student)
                print("添加成功！")
            except ValueError as e:
                print(f"添加失败：{e}")

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            # 按姓名查询，返回所有匹配学生
            name = input ("请输入要查找的学生姓名：")
            results = manager.find_by_name(name)
            if results:
                for s in results:
                    print(f"学号={s.student_id}, 姓名={s.name}, 年龄={s.age}")
            else:
                print("未找到")

        elif choice == "4":
            # 按姓名查找并删除学生
            name = input("请输入要删除学生的姓名：")
            candidates = manager.find_by_name(name)
            if not candidates:
                print("未找到该姓名的学生")
            elif len(candidates) == 1:
                s = candidates[0]
                print(f"学号={s.student_id}, 姓名={s.name}, 年龄={s.age}")
                confirm = input("确认删除？(y/n)：")
                if confirm.lower() == "y":
                    if manager.delete_student(s):
                        print("删除成功")
                    else:
                        print("删除失败")
            else:
                print("找到多个同名学生：")
                for i, s in enumerate(candidates, 1):
                    print(f"{i}. 学号={s.student_id}, 姓名={s.name}, 年龄={s.age}")
                try:
                    idx = int(input("请输入要删除的学生编号："))
                    if 1 <= idx <= len(candidates):
                        confirm = input("确认删除？(y/n)：")
                        if confirm.lower() == "y":
                            if manager.delete_student(candidates[idx - 1]):
                                print("删除成功")
                            else:
                                print("删除失败")
                    else:
                        print("编号超出范围")
                except ValueError:
                    print("输入无效，请输入数字编号")

        elif choice == "5":
            # 按学号查询学生
            student_id = input("请输入要查询的学号：")
            result = manager.find_by_id(student_id)
            if result:
                print(f"找到：学号={result.student_id}, 姓名={result.name}, 年龄={result.age}")
            else:
                print("未找到该学号的学生")

        elif choice == "6":
            # 修改学生信息
            print("1.按学号修改")
            print("2.按姓名修改")
            sub_choice = input("请选择修改方式：")

            # 定位学生
            target = None
            if sub_choice == "1":
                student_id = input("请输入学号：")
                target = manager.find_by_id(student_id)
                if not target:
                    print("未找到该学号的学生")
                    continue
            elif sub_choice == "2":
                name = input("请输入姓名：")
                candidates = manager.find_by_name(name)
                if not candidates:
                    print("未找到该姓名的学生")
                    continue
                elif len(candidates) == 1:
                    target = candidates[0]
                else:
                    print("找到多个同名学生：")
                    for i, s in enumerate(candidates, 1):
                        print(f"{i}. 学号={s.student_id}, 姓名={s.name}, 年龄={s.age}")
                    try:
                        idx = int(input("请输入要修改的学生编号："))
                        if 1 <= idx <= len(candidates):
                            target = candidates[idx - 1]
                        else:
                            print("编号超出范围")
                            continue
                    except ValueError:
                        print("输入无效，请输入数字编号")
                        continue
            else:
                print("输入错误")
                continue

            # 修改学生信息
            print(f"当前信息：学号={target.student_id}, 姓名={target.name}, 年龄={target.age}")
            field_choice = input("修改姓名(1)还是年龄(2)？")
            try:
                if field_choice == "1":
                    new_name = input("请输入新姓名：")
                    manager.update_student(target, "name", new_name)
                    print("修改成功")
                elif field_choice == "2":
                    new_age = input("请输入新年龄：")
                    manager.update_student(target, "age", new_age)
                    print("修改成功")
                else:
                    print("输入错误")
            except ValueError as e:
                print(f"修改失败：{e}")

        elif choice == "7":
            # 退出前确认保存数据
            should_exit = False
            while True:
                save_choice = input("是否保存数据？(y/n)：")
                if save_choice.lower() == "y":
                    manager.save_to_file("data/students.json")
                    print("保存成功")
                    should_exit = True
                    break
                elif save_choice.lower() == "n":
                    confirm = input("⚠️ 数据未保存，确定退出？(y/n)：")
                    if confirm.lower() == "y":
                        should_exit = True
                        break
                    else:
                        break
                else:
                    print("输入错误")
            if should_exit:
                break

        elif choice == "8":
            # 统计信息
            students = manager.get_all_students()
            stats = StudentStatistics(students)
            total = stats.total_count()
            avg_age = stats.average_age()
            ratio = stats.gender_ratio()
            print(f"总人数：{total}")
            print(f"平均年龄：{avg_age:.1f}")
            print(f"性别比例：男={ratio['男']}, 女={ratio['女']}, 未知={ratio['未知']}")

        else:
            print("输入错误，请重新选择")

if __name__ == "__main__":
    main()
