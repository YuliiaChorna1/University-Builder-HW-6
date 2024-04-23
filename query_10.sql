SELECT st.name AS student_name, sb.name AS subject, t.name AS teacher
FROM subjects AS sb
LEFT JOIN grades AS gd ON gd.subject_id = sb.id 
LEFT JOIN students AS st ON gd.student_id = st.id 
LEFT JOIN teachers AS t ON t.id = sb.teacher_id
WHERE st.name = :student_name AND t.name = :teacher_name;