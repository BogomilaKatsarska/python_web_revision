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
'''

'''
CREATE TABLE public.employee
(
    name character varying(30) NOT NULL,
    id serial NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.employee
    OWNER to postgres;
    '''