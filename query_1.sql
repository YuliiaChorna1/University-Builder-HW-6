SELECT st.name AS student_name, AVG(gd.grade) AS avg_grade
FROM students AS st
INNER JOIN grades AS gd ON st.id = gd.student_id
GROUP BY st.id
ORDER BY avg_grade DESC
LIMIT 5;
