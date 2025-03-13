CREATE OR REPLACE PROCEDURE public.prc_projecttool_silver_users()
LANGUAGE plpgsql
AS
$$
BEGIN
    -- Create the table if it doesn't exist
    CREATE TABLE IF NOT EXISTS silver_projecttool.users (
        id INT,
        name TEXT
    );

    -- Truncate the table to clear existing data
    TRUNCATE silver_projecttool.users;

    -- Insert transformed data into the silver_projecttool.users table
    INSERT INTO silver_projecttool.users (id, name)
    SELECT
        id,
        CONCAT(
            SPLIT_PART(REPLACE(name, ', ', ','), ',', 1),
            ', ',
            SPLIT_PART(REPLACE(name, ', ', ','), ',', 2)
        ) AS name
    FROM bronze_projecttool.users;
    
END;
$$;

CALL public.prc_projecttool_silver_users();