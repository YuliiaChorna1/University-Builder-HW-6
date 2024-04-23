from table import Table
from dataclasses import dataclass 


@dataclass
class Student:
    id: int
    name: str
    group_id: int

@dataclass
class Group:
    id: int
    name: int

@dataclass
class Teacher:
    id: int
    name: str

@dataclass
class Subject:
    id: int
    name: str
    teacher_id: int

@dataclass
class Grade:
    id: int
    student_id: int
    subject_id: int
    grade: int
    date: str


class StudentsTable(Table):
    def __init__(self):
        super().__init__("students",
            {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "name": "varchar(255) NOT NULL",
                "group_id": "integer NOT NULL"
            },
            [
                "FOREIGN KEY (group_id) REFERENCES groups(id)"
            ]
        )

    def create(self, student: Student) -> int | None:
        return super().create(student.__dict__)

    def get_all(self) -> list[Student] | None:
        result = []

        rows = super().get_all()

        for i in rows:
            result.append(Student(*i))

        return result

    def update(self, student: Student, **kwargs):
        super().update(student.__dict__, kwargs)


class GroupsTable(Table):
    def __init__(self):
        super().__init__("groups",
            {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "name": "integer NOT NULL",
            },
            []
        )

    def create(self, group: Group) -> int | None:
        return super().create(group.__dict__)

    def get_all(self) -> list[Group] | None:
        result = []

        rows = super().get_all()

        for i in rows:
            result.append(Group(*i))

        return result

    def update(self, group: Group, **kwargs):
        super().update(group.__dict__, kwargs)


class TeachersTable(Table):
    def __init__(self):
        super().__init__("teachers",
            {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "name": "varchar(255) NOT NULL",
            },
            []
        )

    def create(self, teacher: Teacher) -> int | None:
        return super().create(teacher.__dict__)

    def get_all(self) -> list[Teacher] | None:
        result = []

        rows = super().get_all()

        for i in rows:
            result.append(Teacher(*i))

        return result

    def update(self, teacher: Teacher, **kwargs):
        super().update(teacher.__dict__, kwargs)


class SubjectsTable(Table):
    def __init__(self):
        super().__init__("subjects",
            {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "name": "varchar(255) NOT NULL",
                "teacher_id": "integer NOT NULL"
            },
            [
                "FOREIGN KEY (teacher_id) REFERENCES teachers(id)"
            ]
        )

    def create(self, subject: Subject) -> int | None:
        return super().create(subject.__dict__)

    def get_all(self) -> list[Subject] | None:
        result = []

        rows = super().get_all()

        for i in rows:
            result.append(Subject(*i))

        return result

    def update(self, subject: Subject, **kwargs):
        super().update(subject.__dict__, kwargs)


class GradesTable(Table):
    def __init__(self):
        super().__init__("grades",
            {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "student_id": "integer NOT NULL",
                "subject_id": "integer NOT NULL",
                "grade": "integer NOT NULL",
                "date": "date NOT NULL",
            },
            [
                "FOREIGN KEY (student_id) REFERENCES students(id)", 
                "FOREIGN KEY (subject_id) REFERENCES subjects(id)"
            ]
        )

    def create(self, grade: Grade) -> int | None:
        return super().create(grade.__dict__)

    def get_all(self) -> list[Grade] | None:
        result = []

        rows = super().get_all()

        for i in rows:
            result.append(Grade(*i))

        return result

    def update(self, grade: Grade, **kwargs):
        super().update(grade.__dict__, kwargs)
