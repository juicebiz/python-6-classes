class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and (0 < grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        average = 0
        for value in self.grades.values():
            average += sum(value) / len(value)
        return(round(average,2))

    def compare(self, other):
        average_grades_self = self._average_grade()
        average_grades_other = other._average_grade()
        if average_grades_self > average_grades_other:
            return 'Первый cтудент лучше'
        elif average_grades_self == average_grades_other:
            return 'Студенты равны'
        else:
            return 'Второй студент лучше'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self._average_grade()}\n' \
               f'Курсы в прохождении: {" ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {" ".join(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        average = 0
        for value in self.grades.values():
            average += sum(value) / len(value)
        return(round(average,2))

    def compare(self, other):
        average_grades_self = self._average_grade()
        average_grades_other = other._average_grade()
        if average_grades_self > average_grades_other:
            return 'Первый лектор лучше'
        elif average_grades_self == average_grades_other:
            return 'Лекторы равны'
        else:
            return 'Второй лектор лучше'

    def __str__(self):
        return super().__str__() + f'\nСредняя оценка за лекции: {self._average_grade()}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def calc_average_grades_students_course(students, course):
    average = 0
    for student in students:
        for key, value in student.grades.items():
            if(key == course):
                average += sum(value) / len(value)

    return (round(average/len(students), 2))

def calc_average_grades_lectors_course(lectors, course):
    average = 0
    for lector in lectors:
        for key, value in lector.grades.items():
            if(key == course):
                average += sum(value) / len(value)

    return (round(average/len(lectors), 2))

# Students
first_student = Student('First', 'Student', 'M')
first_student.courses_in_progress += ['Python']

second_student = Student('Second', 'Student', 'F')
second_student.courses_in_progress += ['Python']

first_reviewer = Reviewer('First', 'Reviewer')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Second', 'Reviewer')
second_reviewer.courses_attached += ['Python']

first_reviewer.rate_hw(first_student, 'Python', 3)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 10)

first_reviewer.rate_hw(second_student, 'Python', 2)
first_reviewer.rate_hw(second_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Python', 5)

print(first_student);
print(second_student)
print(first_student.compare(second_student))
print(calc_average_grades_students_course([first_student, second_student], 'Python'))

print(first_reviewer)
print(second_reviewer)

first_lecturer = Lecturer('First', 'Lecturer')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Second', 'Lecturer')
second_lecturer.courses_attached += ['Python']

first_student.rate_lw(first_lecturer, 'Python', 5)
first_student.rate_lw(first_lecturer, 'Python', 10)
first_student.rate_lw(first_lecturer, 'Python', 7)

first_student.rate_lw(second_lecturer, 'Python', 2)
first_student.rate_lw(second_lecturer, 'Python', 3)
first_student.rate_lw(second_lecturer, 'Python', 4)

print(first_lecturer)
print(second_lecturer)

print(first_lecturer.compare(second_lecturer))

print(calc_average_grades_lectors_course([first_lecturer, second_lecturer], 'Python'))
