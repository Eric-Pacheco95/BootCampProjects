-- Query 1
SELECT e.emp_no, e.first_name, e.last_name, e.gender, s.salary
FROM employees e, salaries s
WHERE e.emp_no = s.emp_no;
-- Query 2
SELECT employees.emp_no, employees.birth_date, employees.first_name, employees.last_name, employees.gender, employees.hire_date
FROM employees
WHERE employees.hire_date LIKE '1986%';
-- Query 3
SELECT de.dept_no, d.dept_name, de.emp_no, e.first_name, e.last_name, de.to_date
FROM dept_emp de, departments d, employees e
WHERE de.dept_no = d.dept_no 
AND de.emp_no = e.emp_no;
-- Query 4
SELECT e.emp_no,e.first_name,e.last_name,d.dept_name
FROM employees e,departments d,dept_emp de
WHERE e.emp_no = de.emp_no AND de.dept_no = d.dept_no
ORDER BY e.emp_no;
-- Query 5
SELECT employees.emp_no, employees.birth_date, employees.first_name, employees.last_name
FROM employees
WHERE employees.first_name = 'Hercules' 
AND employees.last_name LIKE 'B%';
-- Query 6
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e, departments d, dept_emp de
WHERE e.emp_no = de.emp_no 
AND d.dept_name = 'Sales';
-- Query 7
SELECT departments.dept_name,employees.emp_no,employees.last_name,employees.first_name
FROM employees
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no
WHERE departments.dept_name = 'Sales' 
OR departments.dept_name = 'Development';
-- Query 8
SELECT employees.last_name, COUNT(employees.last_name) AS "Count"
FROM employees
GROUP BY employees.last_name
ORDER BY (count(employees.last_name)) DESC;