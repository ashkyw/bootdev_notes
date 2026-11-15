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
A database [migration](https://en.wikipedia.org/wiki/Schema_migration) is a change of the structure of a relational database. You can think of it like a commit in Git, but for your database schema. Every migration records how the structure of your data evolves over time.

For example, when we previously used an `ALTER TABLE` statement to add a new column, we were performing a **migration**.

Migrations are essential for adapting your database to changing requirements, fixing mistakes, and rolling out new features. In a team setting, migrations ensure everyone applies the same changes in the same order.

**_Good_** migrations are small, incremental and ideally _reversible_ changes to a database. As you can imagine, when working with large databases making changes can be scary! We have to be careful when writing database migrations so that we don't break any systems that depend on the old database schema.

[Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/writing-safe-migrations-1920x1080.mp4)

## Example of a Bad Migration
Let's say CashPal backend runs this SQL regularly:
```sql
SELECT
  *
FROM
  people;
```
If we rename from `people` to `users` in a migration but _forget to update the code_ this query will break because the `people` table no longer exists.

## A safer approach
Roll out schema & application changes in backward-compatible phases. Keep the old schema available until no running code depends on it.

# Up Migration
To manage migrations, we use a simple system based on **up** & **down** directions.
  * The **up** migration applies changes to move your schema forward
  * The **down** migration rolls these changes back to the previous state.

This allows devs to safely move between versions of the schema during development & production rollouts.
### Assignment
Write an `up` migration query:
```sql
ALTER TABLE transactions
ADD COLUMN was_successful BOOLEAN;

ALTER TABLE transactions
ADD COLUMN transaction_type TEXT;
```

# Down Migration
When migrations end up causing issues in production we need to roll back the changes safely using a **down** migration.

#### Why Down Migrations Matter.
Down migrations allow us to:
  * **Undo Changes** introduced by an up migration
  * Quickly recover from bugs or compatibility issues in production.
  * Keep our schema consistent across environments (local, staging, & production)

A well-written down migration should completely reverse the changes made in the up migration. In our case, that means the two columns we just added.

For example, to remove a column you can use the `DROP COLUMN` command:
```sql
ALTER TABLE users
DROP COLUMN email;
```
[Video]([https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/writing-safe-migrations-1920x1080.mp4](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Up-Vs-Down-Migrations-1920x1080.mp4))

### Assignment
Write a `down` migration query:
```sql
ALTER TABLE transactions
DROP COLUMN was_successful;

ALTER TABLE transactions
DROP COLUMN transaction_type;
```
# Migration Review
Let's look at a more realistic migration that reflects a common evolution.

The `projects` table is being renamed to `initiatives` to better reflect how teams plan and track long-term work.

We also want to _record when each initiative officially launched_.

Up Migration:
```sql
ALTER TABLE projects
RENAME TO initiatives;

ALTER TABLE initiatives
ADD COLUMN launched_at TIMESTAMP;
```
Down Migration
```sql
ALTER TABLE initiatives
DROP COLUMN launched_at;

ALTER TABLE initiatives
RENAME to projects;
```
This pair of migrations is **reversible** & **safe**. If something breaks, we can undo it.

#### Real World Migration Tools
In real-world projects, we don't run raw SQL migrations. We use tools that help:
  * Track which migrations have been applied
  * Organize migrations in files
  * Apply & roll back safely

#### Popular Tools
| Tool | Language | Notes |
|------|----------|-------|
|Goose|Go|Native Go Tool|
|Flyway|Java, Etc.|Simple file-based|
|Liquibase|Java|More config-heavy|
|Alembic|Python|For SQLAlchemy|

#### Example Workflow with a Tool
1. Write migration files
    * `001_add_columns_to_transactions.up.sql`
    * `001_add_columns_to_transactions.down.sql`

2. Apply them using the CLI.
  ```
  migrate up
  ```
3. Your tool logs which migrations ran, and prevents duplicate migrations.

#### Version control for your schema
Migration files are committed like code. They travel with your project, so your teammates and [CI Systems](https://en.wikipedia.org/wiki/Continuous_integration) always apply the same schema changes in the right order.
