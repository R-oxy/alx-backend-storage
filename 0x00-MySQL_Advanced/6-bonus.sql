-- Creates a stored procedure AddBonus
-- that adds a new correction for a student.

DELIMITER //

CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;
    
    -- Check if the project exists; if not, create it
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    
    IF project_id IS NULL THEN
        -- Project does not exist, create it
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    
    -- Insert the correction with user_id, project_id, and score
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
    
END //

DELIMITER ;
