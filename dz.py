class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        pes = f'Имя: {self.name}\nФамилия: {self.surname}'
        return pes


class Lekturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.lec = []
        self.grades = {}

    def __str__(self):
        ses = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}'
        return ses

    def average_grades_lec(lektor_list, lec_list):
        lektor_list = []
        lec_list = []

    def aw_grades_LEC(self):

        #Средняя оценка 1 лектора по курсу

        grades_list = sum(self.grades.values(), start=[])
        return round(sum(grades_list) / len(grades_list), 2)

    def __lt__(self, other):

        #Сравнение Лекторов по оценкам

        if not isinstance(other, Lekturer):
            print('Ошибка')
            return
        return self.aw_grades_LEC() < other.aw_grades_LEC()


lekturer_list = []
lekturer_list.append(Lekturer('Pierce', 'Brosnan'))  # добавление в список преподаваемых курсов [0]
lekturer_list.append(Lekturer('Thony', 'Kark'))  # [1]

lekturer_list[0].lec += ['Python', 'Git']
lekturer_list[1].lec += ['Python', 'Git']


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        #Выставление оценок студентам

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


mentors_list = []
mentors_list.append(Reviewer('Some', 'Buddy'))  # [0]
mentors_list.append(Reviewer('Every', 'One'))  # [1]

mentors_list[0].courses_attached += ['Python', 'Git']
mentors_list[1].courses_attached += ['Python', 'Git']


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредння оценка за домашнее задание: {self.grades}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def aw_grades(self):

        #Средняя оценка 1 студента по курсу

        grades_list = sum(self.grades.values(), start=[])
        return round(sum(grades_list) / len(grades_list), 2)

    def __lt__(self, other):

        #Сравнение студентов по оценкам

        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.aw_grades() < other.aw_grades()

    def rate_L_M(self, lektor, lec, grade):

        #Выставление оценок лекторам

        if isinstance(lektor, Lekturer) and lec in lektor.lec:
            if lec in lektor.grades:
                lektor.grades[lec] += [grade]
            else:
                lektor.grades[lec] = [grade]
        else:
            return 'Ошибка'


# Добавляем список студентов
student_list = []
student_list.append(Student('Pol', 'Kakasha', 'female'))  # [0]
student_list.append(Student('Ruoy', 'Eman', 'male'))  # [1]
student_list.append(Student('Pol', 'Cosinsky', 'male'))  # [2]
student_list.append(Student('Lola', 'Kolola', 'female'))  # [3]

# Добавляем студентам курсы
student_list[0].courses_in_progress += ['Python']
student_list[0].finished_courses += ['Git']
student_list[1].courses_in_progress += ['Python']
student_list[2].courses_in_progress += ['Git']
student_list[2].finished_courses += ['Python']
student_list[3].courses_in_progress += ['Python']
student_list[3].finished_courses += ['Git']

# выставление оценок студентам
mentors_list[0].rate_hw(student_list[0], 'Python', 10)
mentors_list[1].rate_hw(student_list[0], 'Python', 8)
mentors_list[0].rate_hw(student_list[0], 'Python', 8)
mentors_list[0].rate_hw(student_list[0], 'Python', 10)
mentors_list[0].rate_hw(student_list[1], 'Python', 8)
mentors_list[1].rate_hw(student_list[1], 'Python', 7)
mentors_list[0].rate_hw(student_list[1], 'Python', 5)
mentors_list[0].rate_hw(student_list[2], 'Python', 7)
mentors_list[1].rate_hw(student_list[2], 'Git', 7)
mentors_list[1].rate_hw(student_list[2], 'Git', 10)

# выставление оценок лекторам
student_list[0].rate_L_M(lekturer_list[0], 'Python', 2)
student_list[0].rate_L_M(lekturer_list[0], 'Python', 5)
student_list[0].rate_L_M(lekturer_list[1], 'Python', 6)
student_list[0].rate_L_M(lekturer_list[1], 'Python', 10)
student_list[1].rate_L_M(lekturer_list[0], 'Git', 9)
student_list[1].rate_L_M(lekturer_list[0], 'Git', 9)
student_list[1].rate_L_M(lekturer_list[1], 'Git', 10)


def total(student_list, course):

    #Средняя оценка всех студентов по определенному курсу

    all_grades = []
    for student in student_list:
        for key, value in student.grades.items():
            if key == course:
                all_grades.extend(value)
    return sum(all_grades) / len(all_grades)


def total(lekturer_list, course):

    #Средняя оценка всех Лекторов по определенному курсу

    all_grades = []
    for lektor in student_list:
        for key, value in lektor.grades.items():
            if key == course:
                all_grades.extend(value)
    return sum(all_grades) / len(all_grades)


print(student_list[0].grades)
print(student_list[1].grades)
print(student_list[2].grades)
print(student_list[2])
print(mentors_list[0])
print(mentors_list[1])
print(lekturer_list[0])
print(total(student_list, 'Git'))
print(total(lekturer_list, 'Git'))
print(Lekturer.aw_grades_LEC(lekturer_list[0]))
print(Student.aw_grades(student_list[0]))
print(student_list[0] > student_list[1])
print(lekturer_list[0] > lekturer_list[1])