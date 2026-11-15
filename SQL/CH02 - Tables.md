# Creating a Table
To create a new table in a database, use the `CREATE TABLE` statement followed by the name of the table & the fields you want in the table.
```sql
CREATE TABLE employees (id INTEGER, name TEXT, age INTEGER,is_manager BOOLEAN, salary INTEGER);
```
Each field name is followed by its _datatype_.
### Assignment
Create the `people` table
```sql
CREATE TABLE people (
  id INTEGER,
  tag TEXT,
  name TEXT,
  age INTEGER,
  balance REAL,
  is_admin BOOLEAN
  );
```
# Create Table Practice
In most relational databases a single table isn't enough to hold all the data we need! We _usually_ create a table-per-entity. For example, a social media application might have the following tables:
  * `users`
  * `posts`
  * `comments`
  * `likes`
### Assignment
Create the `transactions` table
```sql
CREATE TABLE transactions (
  id INTEGER,
  recipient_id INTEGER,
  sender_id INTEGER,
  note TEXT,
  amount REAL
);
```
# Altering Tables
We often need to alter our databases schema without deleting it & re-creating it. Imagine if Twitter deleted its database each time it needed to add a feature, that would be a disaster!
Your account and all your tweets would be wiped out on a daily basis.

Instead, we can use the `ALTER TABLE` statement to make changes in place without deleting any data.

## Alter Table
With SQLite an `ALTER TABLE` statement allows you to:
  #### 1. Rename a Table or Column
  ```sql
  ALTER TABLE employess
  RENAME TO contractors;

  ALTER TABLE contractors
  RENAME COLUMN salary TO invoice;
  ```
  #### 2. Add or Drop a column.
  ```sql
  ALTER TABLE contractors
  ADD COLUMN job_title TEXT;

  ALTER TABLE contractors
  DROP COLUMN is_manager;
  ```

Unlike some SQL databases, SQLite dose not support performing multiple operations in a single `ALTER TABLE` statement. Each change must be made an a separate `ALTER TABLE` command.

### Assignment
Alter the `people` table.
```sql
ALTER TABLE people
RENAME TO users;

ALTER TABLE users
RENAME COLUMN tag TO username;

ALTER TABLE users
ADD COLUMN password TEXT;
```
# Intro to Migrations
A database [migration](https://en.wikipedia.org/wiki/Schema_migration)
[Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/writing-safe-migrations-1920x1080.mp4)
