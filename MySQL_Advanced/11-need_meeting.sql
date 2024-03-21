-- path 11-need_meeting.sql
-- Description: Create a view tthat lists all students that have a score under 80 (strict)
-- And no last_meeting or more than 1 month.
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
