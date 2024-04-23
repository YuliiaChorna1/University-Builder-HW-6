import random
from faker import Faker
from university import Student, Group, Teacher, Subject, Grade
from university import StudentsTable, GroupsTable, TeachersTable, SubjectsTable, GradesTable


class UniversityBuilder:
    def __init__(
            self, 
            students_table: StudentsTable, students_amount: int,
            groups_table: GroupsTable, groups_amount: int,
            teachers_table: TeachersTable, teachers_amount: int,
            subjects_table: SubjectsTable, subjects_amount: int,
            grades_table: GradesTable, grades_amount_per_student: int
    ) -> None:
        
        self.students_table = students_table
        self.students_amount = students_amount
        self.groups_table = groups_table
        self.groups_amount = groups_amount
        self.teachers_table = teachers_table
        self.teachers_amount = teachers_amount
        self.subjects_table = subjects_table
        self.subjects_amount = subjects_amount
        self.grades_table = grades_table
        self.grades_amount_per_student = grades_amount_per_student

        self.faker = Faker()
        self.subjects = [
            'Mathematics',
            'Algebra',
            'Geometry',
            'Science',
            'Geography',
            'History',
            'English',
            'Spanish',
            'German',
            'French',
            'Latin',
            'Greek',
            'Arabic',
            'Computer Science',
            'Art',
            'Economics',
            'Music',
            'Drama',
            'Physical Education']

    def generate_university(self):
        self._generate_groups()
        self._generate_teachers()
        self._generate_students()
        self._generate_subjects()
        self._generate_grades()

    def _generate_groups(self):
        for i in range(1, self.groups_amount + 1):
            self.groups_table.create(Group(id=i, name=random.randint(1, 20)))
           
    def _generate_students(self):       
        all_groups = self.groups_table.get_all()

        for i in range(1, self.students_amount + 1):
            group_id = random.choice(all_groups).id
            
            self.students_table.create(Student(id=i, name=self.faker.name(), group_id=group_id))
        
    def _generate_teachers(self):
        for i in range(1, self.teachers_amount + 1):
            self.teachers_table.create(Teacher(id=i, name=self.faker.name()))

    def _generate_subjects(self):
        all_teachers = self.teachers_table.get_all()

        for i in range(1, self.subjects_amount + 1):
            teacher_id = random.choice(all_teachers).id
            subject_name = random.choice(self.subjects)
            
            self.subjects_table.create(Subject(id=i, name=subject_name, teacher_id=teacher_id))

    def _generate_grades(self):
        all_students = self.students_table.get_all()
        all_subjects = self.subjects_table.get_all()

        id = 1

        for student in all_students:
            for _ in range(self.grades_amount_per_student):
                subject_id = random.choice(all_subjects).id
                grade = random.randint(1, 5)
                date = self.faker.date_this_year()
                
                self.grades_table.create(Grade(id=id, student_id=student.id, subject_id=subject_id, grade=grade, date=date))
                
                id += 1
