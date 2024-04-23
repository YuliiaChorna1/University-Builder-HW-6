import sqlite3
import logging
from table import Table
from fake_uni_builder import UniversityBuilder
from university import StudentsTable, GroupsTable, TeachersTable, SubjectsTable, GradesTable


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
formatter = logging.Formatter(
    'line_num: %(lineno)s > %(message)s'
)

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


def main():
    with sqlite3.connect("University.sqlite") as conn:
        Table.conn = conn

        students_table = StudentsTable()
        groups_table = GroupsTable()
        teachers_table = TeachersTable()
        subjects_table = SubjectsTable()
        grades_table = GradesTable()
        
        my_uni = UniversityBuilder(
            students_table, 50, 
            groups_table, 3, 
            teachers_table, 5,
            subjects_table, 8,
            grades_table, 20
            )
        my_uni.generate_university()
        
        logging.debug(teachers_table.get_all())
        logging.debug(groups_table.get_all())
        logging.debug(subjects_table.get_all())
        logging.debug(grades_table.get_all())

        # Приклад коду для виконання запитів з .sql файлів з параметрами:

        # with open("query_2.sql", "r") as script:
        #     sql = script.read()

        # cur = conn.cursor()
        # cur.execute(sql, ("Latin",))

        # logging.info(cur.fetchall())
        # cur.close()

if __name__ == "__main__":
    main()
