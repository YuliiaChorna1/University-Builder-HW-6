SELECT t.name AS teacher, sb.name AS subject, AVG(gd.grade) AS avg_grade
FROM subjects AS sb 
LEFT JOIN teachers AS t ON sb.teacher_id = t.id 
LEFT JOIN grades AS gd ON gd.subject_id = sb.id
WHERE t.name = :teacher_name
GROUP BY sb.name;