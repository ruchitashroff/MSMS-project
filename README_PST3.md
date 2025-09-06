# MSMS v3 (Music School Management System)

## Overview
This project is the **PST3 refactor** of the Music School Management System (MSMS).  
Unlike PST1 and PST2, which were procedural and messy, **PST3 introduces a clean Object-Oriented Architecture** with separate layers:

- **Model Layer (`app/user.py`, `app/student.py`, `app/teacher.py`, `app/schedule.py`)**  
  Defines the core entities (students, teachers, courses) as Python classes.
- **Controller Layer (`app/schedule.py`)**  
  The `ScheduleManager` class is the central brain that manages all data, persistence, and business logic.
- **View Layer (`main.py`)**  
  Handles user interaction via menus and delegates all work to the `ScheduleManager`.

Data is stored persistently in `data/msms.json`.

--- 

## 📂 Project Structure
MSMS_PST3/
│
├── app/ # Application logic (Models + Controller)
│ ├── user.py # Base User class
│ ├── student.py # StudentUser class
│ ├── teacher.py # TeacherUser and Course classes
│ └── schedule.py # ScheduleManager (main controller)
│
├── data/
│ └── msms.json # Persistent data storage (students, teachers, courses, attendance)
│
├── main.py # Entry point (View Layer)
├── README.md # Documentation

yaml
Copy code

---

## How to Run
1. Clone this repository and navigate into it:
   ```bash
   cd MSMS_PST3
2. Make sure you are using Python 3:
    python3 --version
3. Run the main program:
    python3 main.py

---

## Program Menu
When you run the program, you’ll see: 
===== MSMS v3 (Object-Oriented) =====
1. View Daily Roster
2. Switch Student Course
3. List Students
4. List Teachers
5. List Courses
6. View Attendance
7. Enroll Student in Course
8. Add Student
9. Add Teacher
10. Add Course
11. Check-in Student
q. Quit

## Testing Guide

### 1. Add Data
- Option `8` → Add Student (`Alice`, instruments: `Piano`)  
- Option `9` → Add Teacher (`Mr. Smith`, speciality: `Piano`)  
- Option `10` → Add Course (`Beginner Piano`, instrument: `Piano`, teacher ID: `1`)

### 2. Enroll Students
- Option `7` → Enroll Student in Course (`Student ID: 1`, `Course ID: 1`)

### 3. List Entities
- Option `3` → List Students (should show Alice enrolled in Piano)  
- Option `4` → List Teachers (should show Mr. Smith, Piano)  
- Option `5` → List Courses (should show Beginner Piano with Alice enrolled)

### 4. Attendance
- Option `11` → Check-in Student (`Student ID: 1`, `Course ID: 1`)  
- Option `6` → View Attendance (should now show Alice’s attendance record with a timestamp).

### 5. Switching Courses
- Add another course (option `10`, e.g. `Intermediate Piano`).  
- Option `2` → Switch Student Course (move Alice from course 1 → 2).  

### 6. Daily Roster
- Option `1` → View Daily Roster.  
  *(Requires that courses in `msms.json` have `lessons` with `"day": "Monday"` etc.)*

---

## Design Choices & Assumptions
- **OOP Refactor**: Each entity (`User`, `StudentUser`, `TeacherUser`, `Course`) is a class → more scalable.  
- **Controller Layer**: All business logic is centralized in `ScheduleManager`. This avoids duplicated logic across files.  
- **Persistence**: JSON file (`data/msms.json`) holds all data. It is human-readable and version-controlled.  
- **Flexibility**: `get_lessons_by_day()` supports multiple lessons per course and checks both enrolled IDs and explicit `student_ids` in lessons.  
- **Graceful Defaults**: `.get()` is used when loading JSON to avoid crashes with older or incomplete data files.  
- **Menu Simplicity**: The `main.py` View layer is deliberately kept simple — it only calls manager methods and prints results.  

---

##  Future Improvements
- Add **Check-out / remove attendance** for flexibility.  
- Implement **scheduling UI** with times and conflict checking.  
- Add **unit tests** for business logic in `schedule.py`.  
- Enhance **reporting features** (e.g., attendance summaries, most popular courses).

