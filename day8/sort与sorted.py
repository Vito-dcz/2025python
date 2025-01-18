my_list = "This is my list".split()
print(my_list)

# 转小写
def change_lower(str_name: str):
    return str_name.lower()

# 对字符串列表进行排序（不区分大小写）
print(sorted(my_list, key=change_lower))

# 对字符串列表进行原地排序（不区分大小写）
my_list.sort(key=change_lower)
print(my_list)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # 用于返回元组
    def __repr__(self):
        return repr((self.name, self.age, self.grade))

# 创建一个 Student 实例
student_instance = Student("John", 23, 4)
print(student_instance)
print('-' * 100)

# 创建 Student 对象列表
student_objects = [
    Student('vito', 24, 410),
    Student('lihua', 24, 400),
    Student('xiaomi', 24, 390),
]

# 按成绩排序
print(sorted(student_objects, key=lambda s: s.grade))

from operator import itemgetter, attrgetter
print('使用operator系列')
print(sorted(student_objects, key=attrgetter('grade')))
print(sorted(student_objects, key=attrgetter('grade'), reverse=True))
#print(sorted(student_objects,key=itemgetter(0)))，
# 这是错误的，因为itemgetter不适用于对象列表
