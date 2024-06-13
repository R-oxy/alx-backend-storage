```markdown
# 0x00. MySQL advanced

## Table of Contents
1. [Introduction](#introduction)
2. [Concepts](#concepts)
3. [Resources](#resources)
4. [Learning Objectives](#learning-objectives)
5. [Requirements](#requirements)
6. [Tasks](#tasks)

## Introduction
This project involves advanced usage of MySQL, a popular relational database management system. By the end of the project, you will have hands-on experience with creating tables, optimizing queries, implementing stored procedures, functions, views, and triggers.

## Concepts
For this project, the following concepts are essential:
- Advanced SQL

## Resources
- [MySQL cheatsheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.mysqltutorial.org/mysql-indexes.aspx)
- [Stored Procedure](https://dev.mysql.com/doc/refman/5.7/en/stored-routines.html)
- [Triggers](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives
By the end of this project, you should be able to explain:
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Requirements
- **General:**
  - All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
  - All your files should end with a new line.
  - All your SQL queries should have a comment just before (i.e., syntax above).
  - All your files should start with a comment describing the task.
  - All SQL keywords should be in uppercase (SELECT, WHERE, etc.).
  - A `README.md` file at the root of the project folder is mandatory.
  - The length of your files will be tested using `wc`.

## Tasks
### 0. We are all unique!
- **File:** `0-uniq_users.sql`
- **Description:** Create a table `users` with attributes `id`, `email`, and `name`. Ensure `email` is unique.

### 1. In and not out
- **File:** `1-country_users.sql`
- **Description:** Create a table `users` with attributes `id`, `email`, `name`, and `country` (an enumeration of countries).

### 2. Best band ever!
- **File:** `2-fans.sql`
- **Description:** Rank country origins of bands by the number of non-unique fans.

### 3. Old school band
- **File:** `3-glam_rock.sql`
- **Description:** List all bands with Glam rock as their main style, ranked by their longevity.

### 4. Buy buy buy
- **File:** `4-store.sql`
- **Description:** Create a trigger that decreases the quantity of an item after adding a new order.

### 5. Email validation to sent
- **File:** `5-valid_email.sql`
- **Description:** Create a trigger that resets the attribute `valid_email` only when the email has been changed.

### 6. Add bonus
- **File:** `6-bonus.sql`
- **Description:** Create a stored procedure `AddBonus` that adds a new correction for a student.

### 7. Average score
- **File:** `7-average_score.sql`
- **Description:** Create a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student.

### 8. Optimize simple search
- **File:** `8-index_my_names.sql`
- **Description:** Create an index `idx_name_first` on the table `names` and the first letter of `name`.

## More Info
### Comments for your SQL file:
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
### Use “container-on-demand” to run MySQL
- Request an Ubuntu 18.04 - Python 3.7 container.
- Connect via SSH or WebTerminal.
- Start MySQL in the container:
  ```sh
  $ service mysql start
  ```
- Import a SQL dump:
  ```sh
  $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
  $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
  $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
  ```