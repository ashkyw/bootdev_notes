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
