-- # Write your MySQL query statement below
SELECT s.student_id, s.student_name, su.subject_name, COUNT(e.subject_name) attended_exams 
FROM Students s 
CROSS JOIN Subjects su 
LEFT JOIN Examinations e ON (s.student_id = e.student_id AND su.subject_name = e.subject_name)
-- GROUP BY e.student_id, e.subject_name
GROUP BY su.subject_name, s.student_id
ORDER BY s.student_id, su.subject_name