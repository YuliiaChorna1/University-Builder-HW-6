SELECT gp.name AS group_name, AVG(gd.grade) AS avg_grade, sb.name AS subject
FROM grades AS gd 
LEFT JOIN students AS st ON gd.student_id = st.id 
LEFT JOIN subjects AS sb ON gd.subject_id = sb.id
LEFT JOIN groups AS gp ON st.group_id = gp.id 
WHERE sb.name = :subject_name
GROUP BY gp.name;