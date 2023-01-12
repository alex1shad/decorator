from loggers.logger_1 import logger as log_1
from loggers.logger_2 import logger as log_2


class Student:
    dict_marks = {}

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.course_in_progress = []
        self.finished_course = []
        self.grades = {}

    @log_1
    @log_2('log_student.log')
    def add_course(self, course_name):
        self.course_in_progress.append(course_name)
        self.dict_marks[course_name] = []

    @log_1
    @log_2('log_student.log')
    def end_course(self, course_name):
        if course_name in self.course_in_progress:
            self.finished_course.append(course_name)
            self.course_in_progress.remove(course_name)
        else:
            print(f'Название курса введено некорректно\n'
                  f'{"_"*40}')

    @log_1
    @log_2('log_student.log')
    def add_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.attached_course and\
                0 < int(grade) < 11:
            if course in lecturer.grades.keys():
                lecturer.grades[course] += [grade]
                lecturer.dict_marks[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
                lecturer.dict_marks[course] += [grade]
        else:
            print(f'Данные введены некорректно\n{"_"*40}\n')

    @log_1
    @log_2('log_student.log')
    def _grade_medium_all(self):
        total_list = []
        for mark in self.grades.values():
            for digit in mark:
                total_list.append(digit)
        return round(sum(map(int, total_list))/len(total_list), 1)

    @log_1
    @log_2('log_student.log')
    def __str__(self):
        res = f'Сведения о студенте:\n' \
              f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self._grade_medium_all()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.course_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_course)}\n' \
              f'{"_" * 40}\n'
        return res

    @log_1
    @log_2('log_student.log')
    def __lt__(self, student):
        if isinstance(student, Student):
            res_1 = self._grade_medium_all()
            res_2 = student._grade_medium_all()
            if res_1 > res_2:
                print(f'{self.name} {self.surname} лучше чем '
                      f'{student.name} {student.surname}\n'
                      f'{"_"*40}\n')
            else:
                print(f'{student.name} {student.surname} лучше чем '
                      f'{self.name} {self.surname}\n'
                      f'{"_"*40}\n')
        else:
            print(f'Сведения о студенте введены некорректно\n'
                  f'{"_"*40}\n')


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.attached_course = []


class Lecturer(Mentor):

    dict_marks = {}

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    @log_1
    @log_2('log_student.log')
    def add_course(self, course_name):
        self.attached_course.append(course_name)
        self.dict_marks[course_name] = []

    @log_1
    @log_2('log_student.log')
    def _grade_medium_all(self):
        total_list = []
        for mark in self.grades.values():
            for digit in mark:
                total_list.append(digit)
        return round(sum(map(int, total_list))/len(total_list), 1)

    @log_1
    @log_2('log_student.log')
    def __str__(self):
        res = f'Сведения о лекторе:\n' \
              f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self._grade_medium_all()}\n' \
              f'{"_"*40}\n'
        return res

    @log_1
    @log_2('log_student.log')
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            res_1 = self._grade_medium_all()
            res_2 = lecturer._grade_medium_all()
            if res_1 > res_2:
                print(f'{self.name} {self.surname} лучше чем '
                      f'{lecturer.name} {lecturer.surname}\n{"_"*40}\n')
            else:
                print(f'{lecturer.name} {lecturer.surname} лучше чем '
                      f'{self.name} {self.surname}\n{"_"*40}\n')
        else:
            print(f'Сведения о лекторе введены некорректно\n'
                  f'{"_"*40}\n')


class Reviewer(Mentor):

    @log_1
    @log_2('log_student.log')
    def add_course(self, course_name):
        self.attached_course.append(course_name)

    @log_2('log_student.log')
    @log_1
    def add_grade(self, student, course, grade):
        if isinstance(student, Student) and course in student.course_in_progress and \
                0 < int(grade) < 11:
            if course in student.grades.keys():
                student.grades[course] += [grade]
                student.dict_marks[course] += [grade]
            else:
                student.grades[course] = [grade]
                student.dict_marks[course] += [grade]
        else:
            print(f'Данные введены некорректно\n{"_"*40}\n')

    @log_1
    @log_2('log_student.log')
    def __str__(self):
        res = f'Сведения о проверяющем:\n' \
              f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'{"_"*40}\n'
        return res


student_001 = Student('Ivan', 'Ivanov', 'male')
student_002 = Student('Sergey', 'Sergeev', 'male')
student_003 = Student('Anna', 'Annina', 'female')
lecturer_1 = Lecturer('Maria', 'Teacher')
lecturer_2 = Lecturer('Fedor', 'Professor')
reviewer_1 = Reviewer('Svetlana', 'Checker')
reviewer_2 = Reviewer('Gennadi', 'Inspector')

student_001.add_course('Python')
student_001.add_course('Java')
student_001.add_course('HTML')
student_001.end_course('HTML')
student_002.add_course('Python')
student_002.add_course('Java')
student_002.add_course('HTML')
student_002.end_course('Java')
student_003.add_course('Python')
student_003.add_course('Java')
student_003.add_course('HTML')
student_003.end_course('Python')

lecturer_1.add_course('Python')
lecturer_2.add_course('Java')
lecturer_2.add_course('HTML')
reviewer_1.add_course('Python')
reviewer_1.add_course('Java')
reviewer_2.add_course('Java')
reviewer_2.add_course('HTML')

student_001.add_grade(lecturer_1, 'Python', '10')
student_002.add_grade(lecturer_1, 'Python', '9')
student_001.add_grade(lecturer_2, 'Java', '7')
student_001.add_grade(lecturer_2, 'Java', '8')
student_003.add_grade(lecturer_2, 'HTML', '9')
student_003.add_grade(lecturer_2, 'HTML', '10')

reviewer_1.add_grade(student_001, 'Python', '9')
reviewer_1.add_grade(student_001, 'Python', '10')
reviewer_1.add_grade(student_001, 'Java', '8')
reviewer_1.add_grade(student_002, 'Python', '10')
reviewer_1.add_grade(student_002, 'Python', '9')
reviewer_1.add_grade(student_002, 'HTML', '8')

reviewer_2.add_grade(student_002, 'Python', '9')
reviewer_2.add_grade(student_002, 'Python', '10')
reviewer_2.add_grade(student_002, 'HTML', '9')
reviewer_2.add_grade(student_003, 'Java', '8')
reviewer_2.add_grade(student_003, 'HTML', '8')


@log_1
@log_2('log_student.log')
def grade_medium_student(course_name):
    if course_name in Student.dict_marks.keys():
        res = sum(map(int, Student.dict_marks[course_name])) / \
              len(Student.dict_marks[course_name])
        print(f'Средняя оценка по курсу {course_name} среди студентов: '
              f'{round(res, 1)}\n{"_"*40}\n')
    else:
        print(f'Данные введены некорректно\n{"_"*40}\n')


grade_medium_student('HTML')


@log_1
@log_2('log_student.log')
def grade_medium_lecturer(course_name):
    if course_name in Lecturer.dict_marks.keys():
        res = sum(map(int, Lecturer.dict_marks[course_name])) / \
              len(Lecturer.dict_marks[course_name])
        print(f'Средняя оценка по курсу {course_name} среди лекторов: '
              f'{round(res, 1)}\n{"_"*40}\n')
    else:
        print(f'Данные введены некорректно\n{"_"*40}\n')


grade_medium_lecturer('Java')

print(student_001)
print(lecturer_1)
print(reviewer_1)
student_001 > student_002
