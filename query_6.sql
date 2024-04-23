SELECT gp.name AS group_name, st.name AS studet_name
FROM students AS st
RIGHT JOIN groups AS gp ON st.group_id = gp.id 
WHERE gp.name = :group_name;