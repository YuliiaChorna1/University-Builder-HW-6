
**University Data Generator**

This script generates a fake university database populated with students, groups, teachers, subjects, and grades.

**Requirements:**

* Python 3
* Faker library ([https://pypi.org/project/Faker/](https://pypi.org/project/Faker/))
* sqlite3 library (usually included in Python by default)

**Usage:**

1. Clone or download the repository.
2. Install the required libraries:

```bash
pip install faker
```

3. Run the script:

```bash
python main.py
```

This will create a database file named "University.sqlite" in the current directory.

**How it Works:**

* The script first defines several classes to represent the different entities in the university database (Student, Group, Teacher, Subject, Grade).
* It then creates a connection to a SQLite database file.
* The script uses the `Table` class to create tables in the database for each of the entities.
* The `UniversityBuilder` class is used to generate random data for the students, groups, teachers, subjects, and grades.
* The generated data is then inserted into the database tables using the `create` method of the respective table classes.

**Database Schema:**

The database schema consists of the following tables:

* **students:**
    * id (INTEGER PRIMARY KEY AUTOINCREMENT)
    * name (varchar(255) NOT NULL)
    * group_id (integer NOT NULL) - Foreign key referencing the groups table
* **groups:**
    * id (INTEGER PRIMARY KEY AUTOINCREMENT)
    * name (integer NOT NULL)
* **teachers:**
    * id (INTEGER PRIMARY KEY AUTOINCREMENT)
    * name (varchar(255) NOT NULL)
* **subjects:**
    * id (INTEGER PRIMARY KEY AUTOINCREMENT)
    * name (varchar(255) NOT NULL)
    * teacher_id (integer NOT NULL) - Foreign key referencing the teachers table
* **grades:**
    * id (INTEGER PRIMARY KEY AUTOINCREMENT)
    * student_id (integer NOT NULL) - Foreign key referencing the students table
    * subject_id (integer NOT NULL) - Foreign key referencing the subjects table
    * grade (integer NOT NULL)
    * date (date NOT NULL)

**Customization:**

* You can modify the script to change the number of students, groups, teachers, subjects, and grades that are generated.
* You can also modify the script to generate different types of data for the entities. For example, you could add a field to the students table to store their email addresses.

**License:**

This script is in the public domain. You are free to use, modify, and distribute it as you wish.

**How to execute queries**

The commented-out code block in main.py demonstrates how to execute SQL queries from external `.sql` files with parameters. This functionality is not currently active in the main script, but it provides a way to extend the script's capabilities for more complex database operations.

The code snippet shows how to:

1. Open an `.sql` file (here named "query_2.sql") and read its contents.
2. Create a cursor object to interact with the database connection.
3. Execute the SQL query from the file, passing any necessary parameters (in this case, the parameter `"Latin"`).
4. Retrieve the results of the query using `cur.fetchall()`.
5. Log the results using the `logging.info` function.
6. Close the cursor object.

To enable this functionality, you would need to uncomment the code block and modify the file path and query name as needed.
