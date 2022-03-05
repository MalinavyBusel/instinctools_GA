# 1: наследование,
#    полиморфизм
#    абстракция - скорее всего, класс EduInst будет использоваться
# просто как шаблон, а не как рабочая модель
# 2: полиморфизм - одна функция с разной реализацией для разных входных данных
# 3: полиморфизм(перегрузка) - один метод, но разная реализация для разных классов


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

    def get_students(self):
        return [val for val in self.students.values()]

    def get_students_names(self):
        return [key for key in self.students.keys()]

    def student_info(self, st_info: str):
        return self.students.get(st_info, 'No such student.')

    def add(self, other):
        try:
            students = self.get_students() + other.get_students()
            res = EduInst(students)
            return res
        except AttributeError:
            print('Educational institutions are of invalid types.')


class Gymnasium(EduInst):
    def __init__(self, students: list):
        super().__init__(students)
        self.type = 'Gymnasium'

    def add(self, other):
        if isinstance(other, Gymnasium):
            students = self.get_students() + other.get_students()
            res = Gymnasium(students)
            return res
        else:
            print('Argument is not the instance of Gymnasium.')


class School(EduInst):
    def __init__(self, students: list):
        super().__init__(students)
        self.type = 'School'

    def add(self, other):
        if isinstance(other, School):
            students = self.get_students() + other.get_students()
            res = School(students)
            return res
        else:
            print('Argument is not the instance of School.')


def add(edu_inst_1, edu_inst_2):
    cond_1 = [isinstance(edu_inst_1, School), isinstance(edu_inst_2, School)]
    cond_2 = [isinstance(edu_inst_1, Gymnasium), isinstance(edu_inst_2, Gymnasium)]
    if any([all(cond_1), all(cond_2)]):
        students = edu_inst_1.get_students() + edu_inst_2.get_students()
        res = School(students) if all(cond_1) else Gymnasium(students)
    else:
        res = 'Educational institutions are of invalid types.'
    return res


if __name__ == '__main__':
    my_inst = EduInst([Student('Ignat'), Student('Zakhar')])
    inst_2 = EduInst([Student('Misha')])
    inst_3 = my_inst.add(inst_2)
    print(inst_3.get_students_names())
