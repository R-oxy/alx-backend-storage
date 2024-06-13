-- Creates a stored procedure ComputeAverageScoreForUser
-- that computes and stores the average score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;
    DECLARE avg_score FLOAT;
    
    -- Calculate total score and total number of projects
    SELECT SUM(score), COUNT(*)
    INTO total_score, total_projects
    FROM corrections
    WHERE user_id = user_id;
    
    -- Compute average score
    IF total_projects > 0 THEN
        SET avg_score = total_score / total_projects;
    ELSE
        SET avg_score = 0; -- default average score if no projects
    END IF;
    
    -- Update average_score for the user
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
    
END //

DELIMITER ;
