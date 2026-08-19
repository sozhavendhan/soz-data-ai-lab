-- Snowflake example: create a stage and load data (illustrative)

-- This is illustrative SQL; adapt to your Snowflake environment and credentials.
CREATE OR REPLACE TABLE demo_users (id INT, name STRING, email STRING);

-- Assume a CSV file in an external stage or internal stage
-- COPY INTO demo_users FROM @my_stage/file.csv FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"');

SELECT * FROM demo_users;
