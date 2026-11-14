# SQL
[SQL](https://en.wikipedia.org/wiki/SQL) (**S**tructured **Q**uery **L**anguage) is the language we use to talk to databases. PostgreSQL, MySQL, SQLite, & most other databases that store data in tables _all_ speak it.
### Assignment
Change "people" to "users" in the query:
```sql
SELECT
  *
FROM
  users;
```

# Select Single Column
Databases are made up of [tables]() which are made up of [columns]() (AKA "fields"). It's _just_ like an Excel Spreadsheet.

Each Row in a table is a single record. For example, here are three rows from our CashPal `users` table:

| id | name | age | balance | is_admin |
|--|--|--|--|--|
| 1 | John Smith | 28 | 450 | 1 |
| 2 | Darren Walker | 27 | 200 | 1 |
| 3 | Jane Morris | 33 | 496.24 | 0 |

In the last lesson we used the `*` wildcard to get _all_ the columns. To select only a _single_ column, swap out the `*` for the name of the specific column:
```sql
SELECT
 name
FROM
 users;
```

### Assignment
Update the query to only select the `age` column from the `users` table
```sql
SELECT
 age
FROM
 users;
```

# Select Multiple Columns
As you can guess, if you can select _all_ columns with a `*`, and you can select a single column by name, then you can also selecto multiple columns by name.
For example, if we had a `monsters` table that stores their attributes, we might write:
```sql
select
 health,
 damage,
 defense
from
 monsters;
```
>[!WARNING]
> All SQL statemnts must end with a semicolon `;`.

### Assignment
Update the query to select the 
 * `age`
 * `name`
 * `balance`
columns in order
```sql
SELECT
  age,
  name,
  balance
FROM
  users;
```

# What is SQL?
[Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/What-Is-SQL-V2-1920x1080.mp4)

The primary language used to manage and interact with [relational databases](https://cloud.google.com/learn/what-is-a-relational-database). SQL can perform operations like **Creating, Updating, Reading, Deleting** (CRUD) records within a database.

Generally speaking, SQL is _extremely powerful_ and _programmable_. While spreadsheets are great for simple _manual_ data manipulation, SQL is designed for **automated** & **scalable** data operations. It can handle large datasets, complex queries, and integrate easily with general purpose programming languages like Python, TypeScript, and Go.

# Which Databases Use SQL?
SQL is just a query language. It is typically used to interact with a specific database technology. For example:
 * SQLite
 * PostgreSQL
 * MySQL

Although many different databases use the SQL _language_, most of them will have their own _dialect_. It's _critical_ to understand that _not_ all databases are created equal. Just because one SQL-compatible database does things a certain way, doesn't mean every SQL-compatible database will follow those exact same patterns.

## SQLite
In this training we'll be using SQLite. It is great for embedded projects, web browsers, and toy projects. It's lightweight, but has limited functionality compared to the likes of PostgreSQL or MySQL, two of the more common production SQL technologies.

Unique SQLite functionality will be highlighted in these notes.

### Assignment
One way that SQLite is different is that is stores Boolean values as integers.
 * `0` = `false`
 * `1` = `true`
Write a query selecting all the `id`s, `name`s & `is_admin` flags from the `users` table
```sql
SELECT
  id,
  name,
  is_admin
FROM
  users;
```

# Comparing SQL Databases
SQLite vs PostgreSQL
SQLite is a serverless database management sysetm (DBMS) that has the ability to run within applications, whereas PostgreSQL uses a client-server model & requires a server to be installed and listening on a network, similar to an HTTP server.

[Full comparison here](https://db-engines.com/en/system/PostgreSQL%3BSQLite).

### Assignment
SQLite does _not_ enforce type-checking. Notice that within the `CREATE TABLE` statement, `name` is defined as a `TEXT` field.
Change the second `name` to `1`:
```sql
CREATE TABLE users (id INTEGER, name TEXT, age INTEGER);

INSERT into
  users (id, name, age)
values
  (1, 'John Doe', 21);

INSERT into
  users (id, name, age)
values
  (2, 1, 33);

SELECT
  *
FROM
  users;
```
#NoSQL vs. SQL
When talking about SQL databases, we also have to mention the elephant in the room: [NoSQL](https://en.wikipedia.org/wiki/NoSQL).

Put simply, a NoSQL database is a database that does _not_ use SQL. Each NoSQL database system typically has its own way of writing and executing queries. For example, MongoDB uses MQL (MongoDB Query Language), and ElasticSearch simply has a JSON API.

While most relational databases are fairly similar, NoSQL databases tend to be unique & are used for more niche purpose. Some of the main differences between SQL & NoSQL databases are:

  1. NoSQL databases are usually non-relational; SQL databases are usually [relationl](https://cloud.google.com/learn/what-is-a-relational-database).
  2. SQL databases usually have a defined schema; NoSQL databases usually have a dynamic schema.
  3. SQL databases are table-based; NoSQL databases have a variety of different storage methods, such as document, key-value, graph, wide column, & more.

[Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/sql-vs-no-sql-s-1920x1080.mp4)

## NoSQL databases
 * [Document Database](https://en.wikipedia.org/wiki/Document-oriented_database)
 * [Key-Value Store](https://en.wikipedia.org/wiki/Key%E2%80%93value_database)
 * [Wide-Column](https://en.wikipedia.org/wiki/Wide-column_store)
 * [Graph](https://en.wikipedia.org/wiki/Graph_database)

## SQL databases
 * [MongoDB](https://en.wikipedia.org/wiki/MongoDB)
 * [Cassandra](https://en.wikipedia.org/wiki/Apache_Cassandra)
 * [CouchDB](https://en.wikipedia.org/wiki/Apache_CouchDB)
 * [ElasticSearch](https://www.elastic.co/)
