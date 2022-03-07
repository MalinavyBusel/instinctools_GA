# 1: наследование,
#    инкапсуляция - данные и их методы объединены в одном классе
#    абстракция - скорее всего, класс EduInst будет использоваться
# просто как шаблон, а не как рабочая модель
# 2: полиморфизм - одна функция с разной реализацией для разных входных данных
# 3: инкапсуляция - Для операций с данными класса используются только методы
# этого же класса


class Student:
    def __init__(self, name: str, grade: int = 5):
        self.name = name
        self.grade = grade

    def __str__(self):
        return self.name


class EduInst:
    def __init__(self, students: list):
        self.students = {st.name: st for st in students if isinstance(st, Student)}

    def add_students(self, students: list):
        st_dict = {st.name: st for st in students if isinstance(st, Student)}
        self.students.update(st_dict)
        return None

    def get_students(self):
        return [val for val in self.students.values()]

    def get_students_names(self):
        return [key for key in self.students.keys()]

    def student_info(self, st_info: str):
        return self.students.get(st_info, 'No such student.')

    def __add__(self, other: 'EduInst'):
        students = self.get_students() + other.get_students()
        res = EduInst(students)
        return res


class Gymnasium(EduInst):
    def __init__(self, students: list):
        super().__init__(students)
        self.type = 'Gymnasium'

    def __add__(self, other: 'Gymnasium'):
        condition = type(self) == type(other)
        if condition:
            students = self.get_students() + other.get_students()
            res = Gymnasium(students)
            return res
        else:
            print('Arguments are of different classes.')
            return None


class School(EduInst):
    def __init__(self, students: list):
        super().__init__(students)
        self.type = 'School'

    def __add__(self, other: 'School'):
        condition = type(self) == type(other)
        if condition:
            students = self.get_students() + other.get_students()
            res = Gymnasium(students)
            return res
        else:
            print('Arguments are of different classes.')
            return None


if __name__ == '__main__':
    my_inst = EduInst([Student('Ignat'), Student('Zakhar')])
    inst_2 = EduInst([Student('Misha')])
    inst_3 = my_inst + inst_2
    print(inst_3.get_students_names())
