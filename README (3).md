# Assignment 7 – PostgreSQL CRUD Operations with Python

A Python script demonstrating basic **Create, Read, Update, and Delete (CRUD)** operations on a PostgreSQL database using the `psycopg2` library.

---

## Prerequisites

- Python 3.x
- PostgreSQL server running locally
- `psycopg2` library

Install the dependency:

```bash
pip install psycopg2
```

---

## Database Configuration

The script connects to a local PostgreSQL instance with the following default settings:

| Parameter | Value      |
|-----------|------------|
| Database  | `postgres` |
| User      | `postgres` |
| Host      | `localhost`|
| Port      | `5433`     |

> ⚠️ **Security Note:** The database password is currently hardcoded in the script. Before sharing or deploying this code, move credentials to environment variables or a config file.

---

## Table Schema

The script operates on a `students` table with the following structure:

| Column | Type         | Description              |
|--------|--------------|--------------------------|
| Name   | `TEXT`       | Student's full name      |
| URN    | `VARCHAR`    | University Roll Number   |
| Age    | `INT`        | Student's age            |

---

## Functions

### `create_table()`
Creates the `students` table in the database.

```python
create_table()
```

### `insert_records()`
Inserts a hardcoded sample record into the `students` table.

```python
insert_records()
# Inserts: ('John Doe', 200, 20)
```

### `extract_records()`
Fetches and prints the first record from the `students` table.

```python
extract_records()
# Prints: Name, URN, Age of the first row
```

### `user_input()`
Prompts the user to enter a student's Name, URN, and Age, then inserts the record using a parameterized query (safe against SQL injection).

```python
user_input()
# Prompts: Enter the name, Enter the URN, Enter the age
```

### `delete_records()`
Truncates (clears all rows from) and then drops the `students` table entirely.

```python
delete_records()
```

---

## Usage

Run the script directly. All five functions execute sequentially:

```bash
python assignment_7.py
```

**Execution order:**
1. `create_table()` — creates the table
2. `insert_records()` — adds a sample record
3. `extract_records()` — reads and displays a record
4. `user_input()` — accepts and inserts user-provided data
5. `delete_records()` — drops the table

---

## Notes

- Each function opens and closes its own database connection independently.
- The `user_input()` function uses parameterized queries (`%s`) to prevent SQL injection.
- `delete_records()` permanently removes the `students` table — re-running the script will recreate it via `create_table()`.
