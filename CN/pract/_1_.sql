-- TABLE
    -- create new table
        CREATE TABLE table_name (
            column1 datatype,
            column2 datatype,
            ...
        );
    -- alter table
        -- adding new column
            ALTER TABLE table_name
            ADD column_name datatype;
        -- Modifying a column's data type
            ALTER TABLE table_name
            MODIFY column_name new_datatype;
        -- Deleting a column
            ALTER TABLE table_name
            DROP COLUMN column_name;
    -- drop table
        DROP TABLE table_name;

-- VIEW
    -- creating view
        CREATE VIEW view_name AS
        SELECT column1, column2, ...
        FROM table_name
        WHERE condition;
    -- drop 
        DROP VIEW view_name;

-- index
    -- CREATE INDEX
        CREATE INDEX index_name
        ON table_name (column1, column2, ...);
    -- DROP INDEX
        DROP INDEX index_name;

-- SEQUENCE
    -- creating
        CREATE SEQUENCE sequence_name
        START WITH 1
        INCREMENT BY 1
        MAXVALUE 1000;
    -- using
        INSERT INTO table_name (id, name)
        VALUES (sequence_name.NEXTVAL, 'John Doe');

-- SYNONYM 
    -- Creating a Synonym
        CREATE SYNONYM synonym_name
        FOR object_name;

-- CONSTRAINTS
    -- CREATE UNIQUE CONSTRAINT
        ALTER TABLE table_name
        ADD CONSTRAINT constraint_name UNIQUE (column1, column2, ...);
    -- CREATE PRIMARY KEY CONSTRAINT
        ALTER TABLE table_name
        ADD CONSTRAINT constraint_name PRIMARY KEY (column_name);
    -- CREATE FOREIGN KEY CONSTRAINT
        ALTER TABLE table_name
        ADD CONSTRAINT constraint_name
        FOREIGN KEY (column_name)
        REFERENCES referenced_table(referenced_column);









