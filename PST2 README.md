# MSMS - Music School Management System (PST2)

## Overview:
Welcome to **Music School Management System**! This is an application built in Python to manage data of student and teacher at a music school. This app allows receptionists to register new students, enroll them in their preferred instruments, manage teacher records and perform searches.

This README focuses on **PST2**, which adds persistent data storage and refactors the program structure for better data management, upgrading PST1. 

---

## PST 2 - The Persistence Upgrade

### Purpose
PST2 address the biggest drawback of PST1 - **data loss on exit** - which loads and saves all data from a single structured JSON file ('msms.json')

It further enhances the code structure by integrating all data into one global dictionary('app_data') and ensuring that changes are saved immediately as soon as they occur. 

---

### KEY FEATURES OF EACH FRAGMENT
1. **The Core Persistence Engine**
- 'load_data(path)': Loads 'app_data' from 'msms.json' at startup - if there is no file, an empty structure is created.
- 'save_data(path): Saves 'app_data' back to 'msms.json' in a clean, readable JSON format. 

2. **Refactored and Expanded CRUD Operations**
- Students, teachers, courses and attendance are stored centrally, making data storage secure and consistent. 
- Prevents duplicate ID's and ensures input validation.

3. **Implementing New Receptionist Features**
- Record lesson attendance for students
- Print student ID cards as '.txt' files.

4. **Refactored Main Loop**
- Loads data at the start of the program.
- Runs an interactive menu until the user exits.
- Saves data automatically after every change.

---

### How PST2 Works
flowchart TD
A[Start Program] --> B[load_data()]
    B --> C[Display Main Menu]
    C --> D[User Selects Option]
    D -->|CRUD or Check-in| E[Update app_data]
    E --> F[save_data()]
    F --> C
    D -->|Exit| G[Save & Quit]

---

# RUNNING PST2

## Requirements 
- Python 3.8+
'pst2_main.py' and supporting modules in the same directory

## Steps
# Open terminal in the MSMS-project directory
python pst2_main.py

---

### TESTING PST2
1. **Start Fresh**
- Delete or rename msms.json before running the program to begin with no stored data. 

2. **Add Data**
- Add at least one student, teacher and course using the menu.

3. **Check for Persistence**
- Exit and restart the program
- Confirm that your data is still available

4. **Handle Error**
- Try adding duplicate IDs
- Attempt to enrol a non-existent student.

5. **Print Student Card**
- Use the "print student card" feature and verify that a '.txt' file is created. 

---

### DESIGN CHOICES - Why we did it this way.
- **Changes are saved immediately** - Prevents accidental data loss. 
- **Global Data Dictionary (app_data)**: Centralizes all data in one place so it can be managed efficiently.
- **Format that is Human-Readable**: Makes debugging and editing easy
- **Menu Based Command-Line Interface**: Maintains a simple and suitable interface for learning.

### ASSUMPTIONS - What we expect from the user.
- Every student, teacher and course must have a unique ID to prevent confusion and ensures they are all linked correctly.
- User only enters valid data formats
- Badges are generated as plain text files 
- Users have basic knowledge of command-line interface usage. 
- The JSON file will always be in the same directory as 'pst2_main.py'.

---

### File Structure (PST2):
MSMS-project/
- pst2_main.py        # PST2 entry point
-  msms.json           # Persistent storage file (auto-generated)
- student.py          # Student-related functions
- teacher.py          # Teacher-related functions
- course.py           # Course-related functions
- attendance.py       # Attendance tracking functions
- README.md           # Project documentation




