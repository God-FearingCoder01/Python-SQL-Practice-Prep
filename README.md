# Python-SQL-Practice-Prep

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/CustomTkinter-2596be?style=for-the-badge&logo=python&logoColor=white" alt="CustomTkinter">
</p>

A structured refresher on Python and SQLite3 fundamentals, designed to shake off the rust and build a foundation for creating an SQL Learning Tool for High School Computer Science learners.

## Overview

This repository contains three progressive warm-up exercises that transition from pure Python logic to database integration, culminating in a GUI foundation. These tasks directly inform the architecture of an interactive SQL practice tool for students.

## Prerequisites

- Python 3.x
- SQLite3 (comes bundled with Python)
- CustomTkinter (for task 3)

```bash
pip install customtkinter
```

# The Warm-up Trilogy

Three escalating challenges that build each other, moving from in-memory data structures to presistent storage then adding a graphical intergace.

## Task 1: Pure Python Logic

**Goal:** Demostrate proficiency with data structures and control flow without database complexity.

**The Task:** Build a student management system using a list of dictionaries.

**Requirements:**

- Function to add a student (name and grade)
- Function to display all students
- Function to filter and display students with grades above 50

**Key Concepts:**

- Functions and scope
- Lists and dictionary manipulation
- Conditionals and loops

This task matters because it isolates Python fundamentals before intrducing database complexity. If your logic breaks here, it'll break later-fix it fist!

## Task 2: The SQL Handshake

**Goal:** Re-establish connection to SQLite3 and understand basic CRUD operations.

**The Task:** Migrate the Task 1 logic to use a persistent `school.db` database file.

**Requirements:**

- Create a `students` table with appropriate schema
- Insert at least 3 rows of data programatically
- Execute a `SELECT` query and display results to console

**Critical commands to remember:**

```python
db_connection.commit() # Otherwise your data will just into 'limbo'
my_cursor.execute(<sql>)    # Your SQL interface
```

This task matters because it bridges the gap between temporary Python data structures and persistent SQL storage. Many beginners forget `commmit()` - you'll remember it now!

## Task 3: The GUI Skeleton

**Goal:** Prove that modern Python GUIs are approachable and powerful.

**The Task:** Create a responsive window with user and dynamic feedback.

**Requirements:**

- Entry box for user input
- Button that triggers an action
- Label that updates with the entered text
- Use CustomTkinter (not standard Tkinter)

**Why CustomTkinter?**

- Modern, clean appearance out of the box
- Class-based architecture encourages organized code
- Direct foundation for the SQL tool (SQL input box + run button)

This task matters because it is the exact interaction pattern my SQL Learning Tool will use - student types SQL --> click button --> sees results

# Project Structure

```
Python-SQL-Practice-Prep/
|-- ThePurePythonLogic.py   # List of dictionarie implemention
|-- TheSQLiteHandshake.py   # Database integration
|-- gui_skeleton.py         # CustomTkinter interface
|-- school.db               # Generated SQLite database (Task 2)
```

## Lessons Learned

1. **Defensive Programming (The Safety Net)**

- **Try/Exept Blocks:** I learnt how to prevent my application from craching when a user makes a mistake. By wrapping risky code (like `int(input())`) in a `try` block, I can catch errors like `ValueError` and provide helpful feedback instead of a crash.
- **Specific Error Catching:** I realized it's better to catch a specific error than a general one, so I don't accidetally hide bigger bugs in my code.

2. **Database Security (The Gold Standard)**

- **SQL Injection Prevention:** I learnt why **String Concatenation** (f-strings) is dangerous for database queries.
- **Parameterized Queries:** I implemented the `?` placeholder system. This sanitizes user input, ensuring that a student's practice query doesn't accidentally delete the entire database.

3. **Modern GUI Architecture**

- **CustomTkinter vs Standard Tkinter:** I moved from the older. "blocky" look of standard Tkinter to a modern, themed interface.
- **The Grid System:** I mastered the Graph Paper approach to layout -- using rows, columns and `sticky` properties to make sure the UI looks professional and stays organized when resized.
- **WIdget Control:** I learned how to get data from a `CTkTextbox` using specific coordinated ("1.0", "end-1c") and how to confugure labels and boxes to update the user user on the fly.

# Resources

- [SQLite3 Python Documentation](https://docs.python.org/3/library/sqlite3.html)
- [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/)
- [SQL Tutorial](https://www.w3schools.com/sql/)

# License

MIT - Use freely for personal learning or classroom instruction.
