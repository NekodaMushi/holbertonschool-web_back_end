Resources
---------

**Read or watch**:

*   [MySQL cheatsheet](/rltoken/XCHG-pgtifYRSw8ILB6DEw "MySQL cheatsheet")
*   [MySQL Performance: How To Leverage MySQL Database Indexing](/rltoken/VXAPISdkpKg3YD3HmVQXlw "MySQL Performance: How To Leverage MySQL Database Indexing")
*   [Stored Procedure](/rltoken/C37E-NvP8KxpI5Ds5w1oAQ "Stored Procedure")
*   [Triggers](/rltoken/0xFZu5AK0imLk70dxxcODA "Triggers")
*   [Views](/rltoken/Q8butAms3BthfCFhXuQSPA "Views")
*   [Functions and Operators](/rltoken/0ezATipRSpz1K8MixrD2Rg "Functions and Operators")
*   [Trigger Syntax and Examples](/rltoken/rc8oho9n7LAjtffC584tgA "Trigger Syntax and Examples")
*   [CREATE TABLE Statement](/rltoken/F1SUJgWz-4YNNYLPkL9tPw "CREATE TABLE Statement")
*   [CREATE PROCEDURE and CREATE FUNCTION Statements](/rltoken/XhYdXik2tTMK2k81WxulpA "CREATE PROCEDURE and CREATE FUNCTION Statements")
*   [CREATE INDEX Statement](/rltoken/K90KZ3z4gL5mPpHROlEOcg "CREATE INDEX Statement")
*   [CREATE VIEW Statement](/rltoken/VJESVxV2V7jGqrR-50903A "CREATE VIEW Statement")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/j63kEGfU7eLokEipk6jQCA "explain to anyone"), **without the help of Google**:

### General

*   How to create tables with constraints
*   How to optimize queries by adding indexes
*   What is and how to implement stored procedures and functions in MySQL
*   What is and how to implement views in MySQL
*   What is and how to implement triggers in MySQL

Requirements
------------

### General

*   All your files will be executed on Ubuntu 18.04 LTS using `MySQL 5.7` (version 5.7.30)
*   All your files should end with a new line
*   All your SQL queries should have a comment just before (i.e. syntax above)
*   All your files should start by a comment describing the task
*   All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   The length of your files will be tested using `wc`

More Info
---------

### Comments for your SQL file:

    $ cat my_script.sql
    -- 3 first students in the Batch ID=3
    -- because Batch 3 is the best!
    SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
    $
    

### Use “container-on-demand” to run MySQL

*   Ask for container `Ubuntu 18.04 - Python 3.7`
*   Connect via SSH
*   Or via the WebTerminal
*   In the container, you should start MySQL before playing with it:

    $ service mysql start
     * MySQL Community Server 5.7.30 is started
    $
    $ cat 0-list_databases.sql | mysql -uroot -p my_database
    Enter password: 
    Database
    information_schema
    mysql
    performance_schema
    sys
    $
    

**In the container, credentials are `root/root`**

### How to import a SQL dump

    $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
    Enter password: 
    $ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
    Enter password: 
    $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
    Enter password: 
    id  name
    1   Drama
    2   Mystery
    3   Adventure
    4   Fantasy
    5   Comedy
    6   Crime
    7   Suspense
    8   Thriller
    $
