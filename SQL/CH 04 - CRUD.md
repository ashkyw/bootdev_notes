# CRUD
CRUD is an acronym that describes the four basic ways applications work with stored data: `CREATE`, `READ`, `UPDATE`, & `DELETE`. These four operations are the bread & butter of nearly every database & map directly to a lot of real-world application functionality.

  * `CREATE`: sign up a new user, post a comment
  * `READ`: load a user's profile, view a list of products
  * `UPDATE`: edit a comment, change your password
  * `DELETE`: remove a post, close an account

### Assignment
Determine what SQL command can be used for a `READ` operation.
```sql
SELECT *
FROM crud;
```
# Insert Statement
Tables are pretty useless without data in them. In SQL we can add records to a table using an `INSERT INTO` statement. When using an `INSERT` statement we must first specify the `table` we are inserting the record into, followed by the `fields` within that table we want to add `VALUES` to. Text values go in `,,` single quotes.
```sql
INSERT INTO
 employees (id, name, title)
VALUES
 (1, 'Allan','Engineer');
```
### Assignment
Insert new records into our table
```sql
INSERT INTO
  users(id, name, age, country_code, username, password, is_admin)
VALUES
  (1, 'David', 34, 'US', 'DavidDev', 'insertPractice', false),
  (2, 'Samantha', 29, 'BR', 'Sammy93', 'addingRecords!',  false);
```
# Auto Increment
Many dialects of SQL support an `AUTO INCREMENT` feature. When inserting records into a table with `AUTO INCREMENT` enabled, the database will assign the next value _automatically_. In SQLite, an integer `id` field that has the `PRIMARY KEY` constraint will auto-increment by default!
## IDs
Depending on how your database is set up, you may be using traditional `id`s or you may be using [UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier). SQL doesn't support auto-incrementing a `uuid`, so if your database is using them your server will have to handle the changing `uuid`s for each record.

## `AUTO INCREMENT` in SQLite
We are using traditional `id`s in our database, so we can take advantage of the auto-increment feature. Different dialects of SQL will implement this feature differently, but in SQLite any column that has the `INTEGER PRIMARY KEY` constraint will auto-increment! So we can omit the `id` field within the `INSERT` statement & allow the database to automatically add that field for us!

### Assignment
Modify the table to compensate for auto-incrementing
```sql
INSERT INTO
  users(name, age, country_code, username, password, is_admin)
VALUES
  ('Lance', 20, 'US', 'LanChr', 'bootdevisbest', false),
  ('Tiffany', 28, 'US', 'Tifferoon', 'autoincrement',  true);
```
# Manual Entry
Manually `INSERT`ing every single record in a database would be an _extremely_ time-consuming task! Working with raw SQL as we are now is _not_ super common when designing backend systems.

When working with SQL within a software system, like a backend web application, you'll typically have acccess to a programming language such as Go or Python. For example, a backend server written in Go can use string concatenation to dynamically create SQL statements, & that's how it's usually done!
```go
sqlQuery := fmt.Sprintf(`
INSERT INTO users(name, age, country_code)
VALUES ('%s', %v, '%s');
`, user.Name, user.Age, user.CountryCode)
```
## SQL Injection
The example above is an oversimplification of what _really_ happens when you access a database in Go, in essence, it's correct. String interpolation is how production systems access databases. That said, it must be done _carefully_ to not be a [security vulnerability](https://en.wikipedia.org/wiki/SQL_injection).
# Count
We can use a `SELECT` statement to get a _count_ of the records within a table. This can be very useful when we need to know _how many_ records there are, but we don't particularly care what's in them.
```sql
SELECT
 COUNT(*)
FROM
 employees;
```
### Assignment
```sql
SELECT
  COUNT(*)
FROM
  users;
```
