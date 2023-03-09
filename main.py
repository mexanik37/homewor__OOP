student_list = []
lecturer_list = []


class Student:


    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()
        student_list.append(self)

    def rate_lect(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def grade_midl(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        return (self.average_rating)

    def __str__(self):
        courses_progress = ', '.join(self.courses_in_progress)
        finish_courses = ', '.join(self.finished_courses)
        text = (f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за домашнее задание: {self.grade_midl()}\n'
              f'Курсы в процессе обучения: {courses_progress}\n'
              f'Завершенные курсы: {finish_courses}')
        return text

    def lider_stud(self, other):
        if isinstance(other, Student):
            if self.grade_midl() == other.grade_midl():
                print("У выбранных студентов равный рейтинг")

            elif self.grade_midl() > other.grade_midl():
                print(f"Студент с лучшим рейтингом {self.name} {self.surname}")

            else:
                print(f"Студент с лучшим рейтингом {other.name} {other.surname}")

        else:
             print('Такое сравнение некорректно')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}
        lecturer_list.append(self)

    def grade_midl(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        return (self.average_rating)

    def __str__(self):
        courses_attach = ', '.join(self.courses_attached)
        text = (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.grade_midl()}\n'
                f'Курсы котортые читает: {courses_attach}\n')
        return text

    def lider_lect(self, other):
        if isinstance(other, Lecturer):
            if self.grade_midl() == other.grade_midl():
                print("У выбранных лекторов равный рейтинг")

            elif self.grade_midl() > other.grade_midl():
                print(f"Лектор с лучшим рейтингом {self.name} {self.surname}")

            else:
                print(f"Лектор с лучшим рейтингом {other.name} {other.surname}")

        else:
             print('Такое сравнение некорректно')

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_attach = ', '.join(self.courses_attached)
        text = (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Курсы котортые проверяет: {courses_attach}\n')
        return text

lecturer_1 = Lecturer('Лев', 'Толстой')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Асексндр', 'Дюма')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('О', 'Генри')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Майн', 'Рид')
reviewer_2.courses_attached += ['Python']

student_1 = Student('Николай', 'Васильев')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Артем', 'Веселов')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Савелий', 'Морозов')
student_3.courses_in_progress += ['Git']
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']




# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_3, 'Python', 9)
reviewer_1.rate_hw(student_3, 'Git', 10)

reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_1.rate_hw(student_3, 'Git', 9)
reviewer_1.rate_hw(student_3, 'Git', 8)


reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_3, 'Python', 8)
# Оценки лекторам п
student_1.rate_lect(lecturer_1, 'Python', 10)
student_1.rate_lect(lecturer_1, 'Python', 9)
student_1.rate_lect(lecturer_1, 'Git', 9)

student_1.rate_lect(lecturer_2, 'Python', 9)
student_1.rate_lect(lecturer_2, 'Python', 10)
student_1.rate_lect(lecturer_2, 'Python', 10)

student_2.rate_lect(lecturer_1, 'Python', 10)
student_2.rate_lect(lecturer_1, 'Python', 10)
student_2.rate_lect(lecturer_1, 'Git', 9)

student_2.rate_lect(lecturer_2, 'Git', 10)
student_2.rate_lect(lecturer_2, 'Python', 8)
student_2.rate_lect(lecturer_2, 'Python', 9)

student_3.rate_lect(lecturer_1, 'Git', 10)
student_3.rate_lect(lecturer_2, 'Python', 8)
student_3.rate_lect(lecturer_2, 'Python', 9)

def student_midl_rating(student_list, course_name):
    course_nam = course_name
    sum_all = 0
    count_all = 0
    for stud in student_list:
      for course_nam in stud.grades:
         for grade in stud.grades[course_nam]:
             sum_all += grade
             count_all += 1
    average_for_all = sum_all / count_all
    print(f"Средний рейтинг студентов по курсу {course_name} : {average_for_all}")
    return average_for_all

def lecturer_midl_rating(lecturer_list, course_name):
    course_nam = course_name
    sum_all = 0
    count_all = 1

    for lecter in lecturer_list:
      for course_nam in lecter.grades:
         for grade in lecter.grades[course_nam]:
             sum_all += grade
             count_all += 1
    average_for_all = sum_all / count_all
    print(f"Средний рейтинг леторов по курсу {course_name} : {average_for_all}")
    return average_for_all

print('Пример вывода данных студента')
print(str(student_1))
print()
print('Пример вывода данных лектора')
print()
print(str(lecturer_1))
print()
print('Пример вывода данных контролера')
print()
print(str(reviewer_1))

print()
print('Пример вывода лучшего студента из сравниваемых')
print()
print(student_1.lider_stud(student_2))

print()
print('Пример вывода лучшего лектора из сравниваемых')
print()
print(lecturer_1.lider_lect(lecturer_2))

print()
print('Пример вывода среднего рейтинга лекторов')
print()
lecturer_midl_rating(lecturer_list, 'Python')

print()
print('Пример вывода среднего рейтинга студентов')
print()
student_midl_rating(student_list, 'Python')