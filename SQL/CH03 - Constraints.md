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
# Schema
We've seen the word schema before, let's talk about what it means. A database's [schema](https://www.ibm.com/think/topics/database-schema) describes how data is organized within it. 

Data types, table names, field names, constraints, & the relationship between all of those entities are part of a database's schema.

## There is no perfect schema
When designing a database schema, there typically isn't a "correct" solution. We do our best to choose a reasonable set of tables, fields, constraints, etc. that will accomplish our project's goals.

Like many things in programming, different schema designs come with different trade-offs.

## How to decide on a Sane schema
Let's use CashPal as an example. One important decision that needs to be made is which table will store a user's balance! As you can imagine, ensuring our data is accurate when dealing with money is _critical_. We want to be able to:
 * Keep track of a user's current balance
 * See the historical balance at any point in the past
 * See a log of which transactions changed the balance over time.

There are many ways to approach this problem, but let's start with the simplest schema that fulfills our project's needs.

### Assignment
We have decided to use a single `transactions` table. Create it
```sql
CREATE TABLE transactions(
  id INTEGER PRIMARY KEY,
  sender_id INTEGER,
  recipient_id INTEGER,
  memo TEXT NOT NULL,
  amount REAL NOT NULL,
  balance REAL NOT NULL
);
```
# Relational Databases
A relational database is a type of database that stores data so that it can be easily related to other data. For example, a `user` can have many `tweets`. There's a relationship between a `user` and their `tweet`.

In a relational database:

1. Data is typically represented in "tables."
2. Each table has "columns" or "fields" that hold attributes related to the record.
3. Each row or entry in the table is called a [record](https://en.wikipedia.org/wiki/Record_(computer_science)).
4. Typically, each record has a unique `Id` called the [primary key](https://en.wikipedia.org/wiki/Primary_key).

[!Relational Database Example]()
This database has 3 tables. `Students`, `Courses` & `StudentCourses`. The `StudentCourses` table manages the relationship between the `Studends` & `Courses` tables

## Example 1: Curly
 * Curly has an `id` of `2`
 * We can find Curly's courses by looking in the `StudentCourses` table for the records that match his `StudentId`.

## Example 2: Haskell Monads
* Has an `id` of `3`
* We can find all the students enrolled in the Haskell Monads course by checking the `CourseId` column in the `StudentCourses` table.
