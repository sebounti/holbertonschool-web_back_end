-- path 7-average_score.sql
-- Description: Create a view that lists all students that have a score under 80 (strict)
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN student_id INT
)
BEGIN
	DECLARE avg_score FLOAT;
	SET avg_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=student_id);
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END$$
DELIMITER ;
