class Student():

    def __init__(self, id, firstname, lastname):
        self.id = str(id)
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.num_course = 0
        self.total_credit = 0
        self.advisor = None
        self.major = None
    
    def add_course(self, course):
        if course.course_id in self.courses or self.total_credit + course.credit > 25:
            return False
        self.courses.append(course.course_id)
        self.num_course += 1
        self.total_credit += course.credit
        return True

    def drop_course(self, course):
        if course.course_id not in self.courses:
            return False
        self.courses.remove(course.course_id)
        self.num_course -= 1
        self.total_credit -= course.credit
        return True
    
    def set_advisor(self, advisor):
        self.advisor = advisor
    
    def set_major(self, major):
        self.major = major
    
    def __str__(self):
        id = f'Student ID: {self.id}'
        name = f'Name: {self.firstname} {self.lastname}'
        major = "Major: " + str(self.major)
        advisor = "Advisor: " + str(self.advisor)
        courses = "Courses: " + " ".join(self.courses)
        return f"{id}\n{name}\n{major}\n{advisor}\n{courses}"
        

class Course():

    def __init__(self, title, course_id, credit):
        self.title = title
        self.course_id = str(course_id)
        self.credit = credit

class Teacher():

    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = str(id)

    def	__str__(self):
        return f"{self.firstname} {self.lastname} ({self.id})"

class Major():

    def __init__(self, id, name, faculty):
        self.id = str(id)
        self.name = name
        self.faculty = faculty
    
    def __str__(self):
        return f"{self.name} ({self.id})"

pati = Student("6710504034", "Patiphat", "Moungmaithong")
compro = Course("Computer Programming", "01402113", 3)
art = Course("Art Of Living", "1", 3)
thai = Course("Thai Commu", "123", 3)
pati.add_course(compro)
pati.add_course(art)
pati.add_course(thai)
print(pati, end="\n\n")
advisor = Teacher("Ajarn", "New", "E27")
pati.set_advisor(advisor)
major = Major("CPE38", "Computer Engineering", "Engineering")
pati.set_major(major)
print(pati, end="\n\n")
print(pati)