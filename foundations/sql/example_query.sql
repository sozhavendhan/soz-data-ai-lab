-- Example SQL queries for learning

-- Simple example: create a table and insert sample data (syntax may vary by database)
CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(200)
);

INSERT INTO users (id, name, email) VALUES
(1, 'Alice', 'alice@example.com'),
(2, 'Bob', 'bob@example.com');

SELECT * FROM users;
