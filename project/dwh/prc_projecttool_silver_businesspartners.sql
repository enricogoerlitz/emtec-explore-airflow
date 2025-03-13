-- PROCEDURE: public.prc_projecttool_silver_businesspartners()

-- DROP PROCEDURE IF EXISTS public.prc_projecttool_silver_businesspartners();

CREATE OR REPLACE PROCEDURE public.prc_projecttool_silver_businesspartners()
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    -- Create the table if it doesn't exist
    CREATE TABLE IF NOT EXISTS silver_projecttool.businesspartners (
	    id INT,
		name VARCHAR(255)
    );

    -- Truncate the table to clear existing data
    TRUNCATE silver_projecttool.businesspartners;

    -- Insert transformed data into the silver_projecttool.users table
    INSERT INTO silver_projecttool.businesspartners
    SELECT
		id
		,name
    FROM bronze_projecttool.businesspartners;
    
END;
$BODY$;

ALTER PROCEDURE public.prc_projecttool_silver_businesspartners()
    OWNER TO postgres;
