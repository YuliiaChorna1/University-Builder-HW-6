SELECT t.name AS teacher_name, sb.name AS subjects
FROM teachers AS t
LEFT JOIN subjects AS sb ON sb.teacher_id = t.id
WHERE t.name = :teacher_name;
