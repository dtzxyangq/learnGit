#!/usr/bin/env python3

class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1
        #self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    print(Student.count)
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

# bart = Student('Bart', 'male')
# print(bart.name, bart.get_gender())
# bart.set_gender('female')
# print(bart.name, bart.get_gender())

# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

