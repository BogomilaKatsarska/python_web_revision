'''
1:06
1. Data storage vs Data management
- a DB is an organized collection of related information
- the user doesn't have direct access to the stored data
- access to data is usually provided by DBMS
- the table is the main building block of any DB

2.PostgreSQL - ORDBMS /object-relational DB management system/
#TODO: check docker
-> employee -> query tool

3. PgAdmin/management tool/ - we use it to access PostgreSQL

4. Data Types in SQL:
- CHARACTER / CHAR [(M)] - fixed length, char without the length specifier (m) is the same as CHAR(1)
- CHARACTER VARYING / VARCHAR [(N)] - variable-length with limit, varchar without (n) can store a string with unlimited length
- TEXT - stores strings of any length
- SMALLINT, INT, BIGINT
- DECIMAL, NUMERIC
- REAL, DOUBLE PRECISION
- SMALLSERIAL, SERIAL, BIGSERIAL
- UNIQUE
- NULL / NOT NULL
- DEFAULT
- PRIMARY KEY

5. Table Relations
- Denormalized (adding additional column) vs Normalized (creating a new table with relations)
- One-to-many
- Many-to-many (using mapping/conjunction table - with 2 FKs)
- One-to-one

6. ON DELETE:
- RESTRICT - restrict deleting the record
- CASCADE - automatically delete rows referencing a deleted record
- SET NULL - set null to the referenced fk columns

7. Basic SQL Commands:
- CREATE TABLE
- INSERT INTO
- SELECT * FROM
- WHERE first_name LIKE 'D%'

- UPDATE - SET - WHERE

- ALTER TABLE employees
  ADD COLUMN salary DECIMAL;
  DROP COLUMN ...

- TRUNCATE TABLE employees; --> delete all the entries in a table

- ORDER BY
'''


'''
CREATE TABLE public.employees
(
    name character varying(30) NOT NULL,
    id serial NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.employees
    OWNER to postgres;
    
UPDATE employees
SET salary = salary * 1.1
WHERE job_title = 'Cashier';

INSERT INTO employees(first_name, last_name)
VALUES ('Doncho', 'Minkov')

CREATE TABLE department
(dep_id SERIAL UNIQUE NOT NULL,
dep_name VARCHAR(100) UNIQUE NOT NULL,
dep_location VARCHAR(100) DEFAULT 'Sofia'
);

CREATE TABLE categories
(id serial PRIMARY KEY ,
name VARCHAR (20) NOT NULL,
);


SELECT *
from products
RIGHT JOIN categories
    ON products.category_it = categories.id
'''