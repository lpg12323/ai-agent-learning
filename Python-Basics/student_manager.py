students = [{"name":"Tom", "age":20}, {"name":"Alice", "age":18}]

def add_student():
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    students.append({"name":name, "age":age})

def delete_student():
    name = input("请输入要删除的学生姓名：")
    for s in students:
         if s["name"] == name:
            students.remove(s)
            print(f"已删除学生：{name}")
            break
    else:
        print("未找到该学生")

def view_student():
        if len(students) == 0:
            print("暂无学生")
        else:
            print("学生列表:")
            for s in students:
                print(f"姓名：{s['name']}, 年龄：{s['age']}")

def modify_student_age():
    name = input("请输入要修改年龄的学生姓名：")
    for s in students:
        if s["name"] == name:
            new_age = int(input("请输入修改后的年龄："))
            s["age"] = new_age
            print(f"{name}的年龄已经修改为{new_age}")
    else:
        print("未找到该学生")

def search_student_by_name():
    name = input("请输入要查找学生的姓名：")
    for s in students:
        if s["name"] == name:
            print(f"姓名：{s['name']}, 年龄：{s['age']}")
    else:
        print("未找到该学生")

while True:
    print("="*30)
    print("学生管理系统")
    print("1.添加学生")
    print("2.删除学生")
    print("3.查看学生")
    print("4.修改学生年龄")
    print("5.按姓名查找学生")
    print("6.退出")
    print("="*30)
    choice = input("请输入操作编号：")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    
    elif choice == "3":
        view_student()

    elif choice == "4":
        modify_student_age()
    
    elif choice == "5":
        search_student_by_name()

    else:
        print("退出程序")
        break

