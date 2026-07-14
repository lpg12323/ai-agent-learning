from student import Student
from manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("="*30)
        print("学生管理系统")
        print("1.添加学生")
        print("2.查看学生")
        print("3.查找学生")
        print("4.删除学生")
        print("5.退出")
        print("="*30)

        choice = input("请输入操作编号：")

        if choice == "1":
            name = input("请输入学生姓名：")
            age = input("请输入学生年龄：")
            student = Student(name, age)
            manager.add_student(student)
            print("添加成功！")
        
        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            name = input ("请输入要查找的学生姓名：")
            result = manager.find_student(name)
            if result:
                print(f"找到：{result.name}, {result.age}")
            else:
                print("未找到")

        elif choice == "4":
            name = input("请输入要删除学生的姓名：")
            manager.delete_student(name)

        elif choice == "5":
            print("退出程序")
            break

        else:
            print("输入错误，请重新选择")

if __name__ == "__main__":
    main()
