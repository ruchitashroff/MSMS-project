# Music School Management System (MSMS) – PST5

**FIT1056 – Introduction to Software Engineering**  
**Semester 2, 2025 – Problem-Solving Task 5 (PST5)**  
**Author:** Ruchita Haresh Shroff 
**Git Repository:** https://github.com/ruchitashroff

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Directory Structure](#directory-structure)  
3. [Project Stages (PST1–PST5)](#project-stages-pst1–pst5)  
4. [Running the Application](#running-the-application)  
5. [Automated Testing](#automated-testing)  
6. [Design Choices & Assumptions](#design-choices--assumptions)  
7. [Acknowledgements](#acknowledgements)  

---

## Project Overview

The **Music School Management System (MSMS)** is a Python-based application designed to manage student registrations, lesson scheduling, financial transactions, and reporting for a music school.  

The goal of **PST5** was to develop a fully functional, crash-proof system with:

- Persistent file storage  
- Professional OOP architecture  
- Streamlit-based GUI for ease of use  
- Finance and reporting features  
- Administrative utilities (logging, backups)  
- Automated tests for quality assurance  

This project demonstrates progressive software engineering practices, from simple scripts to a professional, testable, maintainable application.

---

## Directory Structure

msms-project/
│
├─ app/
│ ├─ schedule.py # Core logic: student/lesson management, finance
│ ├─ admin_utils.py # Logging & backup utilities
│
├─ gui/
│ ├─ main_dashboard.py # Main Streamlit dashboard
│ ├─ finance_pages.py # GUI pages for finance/payment features
│
├─ tests/
│ ├─ test_schedule_manager.py # Automated unit tests using pytest
│
├─ main.py # Entry point: launches GUI, logging, backups
└─ README.md
---

## Project Stages (PST1–PST5)

### **PST1: The Foundation**
- Implemented a simple in-memory prototype to manage students, lessons, and basic schedules.
- Used Python lists and dictionaries.
- Verified basic functionality through manual testing.

### **PST2: The Upgrade**
- Added file-based persistence using JSON storage.
- Implemented data validation for input integrity.
- Refactored code into functions for better organization.

### **PST3: The Architecture**
- Rebuilt the system using **Object-Oriented Programming (OOP)** principles.
- Introduced classes for `ScheduleManager`, `Student`, and `Lesson`.
- Encapsulated business logic within methods for maintainability.

### **PST4: The User Interface**
- Replaced console interface with **Streamlit GUI**.
- Implemented a dashboard with navigation for student management, lesson scheduling, and placeholders for finance.
- Improved usability and professional appearance.

### **PST5: The Quality & Finance Gate**
- **Finance & Reporting Engine:**  
  - `record_payment(student_id, amount, method)`  
  - `get_payment_history(student_id)`  
  - `export_report(kind, out_path)`  
  - Stored financial transactions in `self.finance_log`.
- **GUI for Finance:**  
  - Added `gui/finance_pages.py` for recording/viewing payments.  
  - Integrated with main dashboard.
- **Admin & Quality Utilities:**  
  - Logging (`init_logger(log_file)`) for critical events.  
  - Backup (`backup_data(data_path, backup_dir)`) to ensure data safety.
- **Integration:**  
  - Main application initializes logging and backups on startup.  
  - All key business actions are logged automatically.
- **Automated Tests:**  
  - Implemented using `pytest` in `tests/test_schedule_manager.py`.  
  - Tests follow **Arrange, Act, Assert** pattern for core methods (student registration, payments, scheduling).

---

## Running the Application

### 1. Install Dependencies
'''bash'''
pip install -r requirements.txt
Includes streamlit and pytest.

### 2. Launch the Application
- python main.py
- Opens the Streamlit GUI.Use the navigation panel to access students, lessons, and finance pages.
- "Backup Now" button ensures immediate data safety.

### 3. Automated Testing
Run tests with pytest:
- pytest
- Tests validate key functionalities such as:
    - Adding and removing students
    - Scheduling and canceling lessons
    - Recording payments
    - Exporting reports
- Test results appear in the terminal. All tests should pass for a fully working system.

## Design Choices & Assumptions
### 1. OOP Design:
- Encapsulated core logic within ScheduleManager for maintainability.
- Classes represent real-world entities (Student, Lesson).

### 2. Persistence:
- JSON storage chosen for simplicity and readability.
- Backup utility ensures data integrity.

### 3. GUI Design:
- Streamlit selected for rapid prototyping and professional appearance.
- Finance page split into "Record Payment" and "View History" for clarity.

### 4. Logging:
- Critical actions (registrations, payments, cancellations) are logged for traceability.

### 5. Testing:
- Unit tests ensure application correctness.
- Separate tests for each method allow easy debugging and future extension.

### 6. Assumptions:
- Each student has a unique student_id.
- Payments are assumed in local currency.
- System is intended for a single-user environment (no concurrent access handling).

## Acknowledgements
- FIT1056 PST5 case study materials for project requirements and templates.
- Streamlit documentation for GUI development.