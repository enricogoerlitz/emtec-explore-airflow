-- PROCEDURE: public.prc_projecttool_silver_projects()

-- DROP PROCEDURE IF EXISTS public.prc_projecttool_silver_projects();

CREATE OR REPLACE PROCEDURE public.prc_projecttool_silver_projects(
	)
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    -- Create the table if it doesn't exist
    CREATE TABLE IF NOT EXISTS silver_projecttool.projects (
	    id INT,
	    projectname VARCHAR(255),
	    description TEXT,
	    businesspartner_id INT,
	    hourly_rate DECIMAL(8, 2)
    );

    -- Truncate the table to clear existing data
    TRUNCATE silver_projecttool.projects;

    -- Insert transformed data into the silver_projecttool.users table
    INSERT INTO silver_projecttool.projects
    SELECT
		id
		,projectname
		,description
		,businesspartner_id
		,hourly_rate
    FROM bronze_projecttool.projects;
    
END;
$BODY$;

ALTER PROCEDURE public.prc_projecttool_silver_projects()
    OWNER TO postgres;
