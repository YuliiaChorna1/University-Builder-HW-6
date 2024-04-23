SELECT DISTINCT st.name AS student_name, sb.name AS subject
FROM students AS st
LEFT JOIN grades AS gd ON gd.student_id = st.id
LEFT JOIN subjects AS sb ON gd.subject_id = sb.id
WHERE st.name = :student_name;
--GROUP BY sb.name;