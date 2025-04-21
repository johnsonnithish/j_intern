SELECT
e.first_name AS "First Name",
e.last_name AS "Last Name",
e.date_of_birth AS "DOB",
e.date_of_joining AS "DOJ",
d.name AS "Department Name",
p.name AS "Project Name",
des.name AS "Designation",
CONCAT(m.first_name, ' ' , m.last_name) AS "Reporting Manager Name"
FROM emp_register e
LEFT JOIN dept_master d ON e.department_id=d.id
LEFT JOIN project_master p ON e.project_id=p.id
LEFT JOIN designation_master des ON e.designation_id=des.id
LEFT JOIN emp_register m ON e.reporting_to_id=m.id;
