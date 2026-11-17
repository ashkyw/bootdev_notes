# Null Values
In SQL, a cell with a `NULL` value indicates that the value is _missing_. A `NULL` value is _very_ different from a _zero_ value.

## Constraints
When creating a table, we can define whether or not a field _can or cannot_ be `NULL`, & that's a kind of `constraint`.

### Assignment
Write a `SELECT` query
```sql
SELECT 
  *
FROM 
  transactions;
```
# Constraints
A `constraint` is a rule we create on a database that _enforces_ some specific behavior. For example, setting a `NOT NULL` constraint on a column ensures that the column will not accept `NULL` values.

If we try to insert a `NULL` value into a column with the `NOT NULL` constraint, the insert will fail with an error message. Constraints are extremely useful when we need to _ensure_ that certain kinds of data exist within our database.

## Defining a NOT NULL constraint
The `NOT NULL` constraint can be added directly to the `CREATE TABLE` statement.
```sql
CREATE TABLE employees (
 id INTEGER PRIMARY KEY,
  -- The PRIMARY KEY constraint uniquely identifies each row in the table
 name TEXT UNIQUE,
  -- The UNIQUE constraint ensures that no two rows can have the same value in the 'name' column
 title TEXT NOT NULL
  -- The NOT NULL constraint ensures that the 'title' column cannot have NULL values
);
```
## SQLite Limitation
In other dialects of SQL you can `ADD CONSTRAINT` within an `ALTER TABLE` statement. SQLite does _not_ support this feature so when we create our tables we need to make sure we specify all the constraints we want! 
[List of SQL features SQLite does not implement](https://www.sqlite.org/omitted.html)

### Assignment
Create the `users` table with constraints
```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country_code TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);
```
# Primary Keys
A _key_ defines & protects relationships between tables. A [primary key](https://en.wikipedia.org/wiki/Primary_key) is special column that _uniquely_ identifies records within a table. Each table can have one, and **_only one_**, primary key.

## Primary Key is usually an ID
It's _very_ common to have a column named `id` on each table in a database, and that `id` is the primary key for that table. No two rows in that table can share an `id`.

A `PRIMARY KEY` constraint can be explicitly specified on a column to ensure uniqueness, rejecting any inserts where you attempt to create a duplicate ID.

### Assignment
Fix the `PRIMARY KEY` on the `id` column
```sql
INSERT INTO
  users (id, name, age, username, password, is_admin)
VALUES
  (1, 'Rudolf', 33, 'rudolf1234', 'thisisnotsecure', false);

INSERT INTO
  users (id, name, age, username, password, is_admin)
VALUES
  (2, 'Jerry', 25, 'jerrysmith', 'mypasswordis1234', true);
```
# Foreign Keys
Foreign keys define the relationships _between_ tables. Simply put, a `FOREIGN KEY` is a field in one table that references the `PRIMARY KEY` (or a `UNIQUE` column) of another table.

## Creating a foreign key in SQLite
Creating a `FOREIGN KEY` in SQLite happens at table creation! After we define the table fields & constraints we add a named `CONSTRAINT` where we define the `FOREIGN KEY` column & its `REFERENCES`.
```sql
CREATE TABLE departments (id INTEGER PRIMARY KEY, department_name TEXT NOT NULL);

CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  department_id INTEGER,
  CONSTRAINT fk_departments FOREIGN KEY (department_id) REFERENCES departments (id)
);
```
In the above example, an `employee` has a `department_id`. The `department_id` must be the same as the `id` field of a record from the `departments` table. `fk_departments` is the specified name of the constraint.

 1. `CONSTRAINT fk_departments`: create a constraint called `fk_departments`
 2. `FOREIGN KEY (department_id)`: make this constraint a foreign key assigned to the `department_id` field
 3. `REFERENCES departments (id)`: link the foreign field `id` from the `departments` table

Creating a foreign key without the `CONSTRAINT` keyword means the name of the constraint is auto-assigned.
### Assignment
Fix the data so no foreign keys are violated
```sql
File 1:
PRAGMA foreign_keys = ON;

CREATE table countries (code TEXT PRIMARY KEY, name TEXT);

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER,
  country_code TEXT NOT NULL,
  username TEXT,
  password TEXT,
  is_admin BOOLEAN,
  FOREIGN KEY (country_code) REFERENCES countries (code)
);

INSERT INTO
  countries (code, name)
VALUES
  ('US', 'United States of America');

INSERT INTO
  countries (code, name)
VALUES
  ('IN', 'India');

File 2:
INSERT INTO
  users (id, name, country_code)
VALUES
  (1, 'Jerry', 'US');

INSERT INTO
  users (id, name, country_code)
VALUES
  (2, 'Amit', 'IN');
```
