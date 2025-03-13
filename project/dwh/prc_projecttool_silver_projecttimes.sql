CREATE OR REPLACE PROCEDURE public.prc_projecttool_silver_projecttimes()
LANGUAGE plpgsql
AS
$$
BEGIN
    -- Create the table if it doesn't exist
    CREATE TABLE IF NOT EXISTS silver_projecttool.projecttimes (
	    id INT,
		user_id INT,
		project_id INT,
		hours FLOAT,
		comment TEXT
    );

    -- Truncate the table to clear existing data
    TRUNCATE silver_projecttool.projecttimes;

    -- Insert transformed data into the silver_projecttool.users table
    INSERT INTO silver_projecttool.projecttimes
    SELECT
		id
		,user_id
		,project_id
		,hours
		,comment
		
    FROM bronze_projecttool.projecttimes;
    
END;
$$;