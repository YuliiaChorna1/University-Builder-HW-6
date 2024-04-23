SELECT st.name AS student_name, gd.grade, gp.name AS group_name, sb.name AS subject
FROM grades AS gd
LEFT JOIN subjects AS sb ON gd.subject_id = sb.id
LEFT JOIN students AS st ON st.id = gd.student_id
LEFT JOIN groups AS gp ON st.group_id = gp.id
WHERE gp.name = :group_name AND sb.name = :subject_name;